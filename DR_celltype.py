# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 13:26:09 2020

@author: Lur Lab 3
"""
#%%

def getRinput(savedLoc):
    import pickle
    from pathlib import Path
    
    path = Path(savedLoc)

    import os
    allnames = os.listdir(savedLoc)
    
    import numpy as np
    
    alldataDict = {}
    for i in allnames:
        # point at data file to view
        cellPath = path / i
        loadedData = pickle.load(open(cellPath, 'rb'))
        for k in loadedData.keys():
            if '_data' in k:
                alldataDict[i] = loadedData[k]
    
    RinputDict = {}
    for k, v in alldataDict.items():
        beforePulse = np.mean(v[900:999],0)
        duringPulse = np.mean(v[5000:6000],0)
        y = np.argmin(abs(duringPulse - beforePulse))
        
        try:
            stepsize = 150
            if stepsize == 100:
                pulse = 2
            if stepsize == 150:
                pulse = 3
            if stepsize == 200:
                pulse = 4
            
            if duringPulse[y-pulse] - beforePulse[y-pulse] > 0:
                step = duringPulse[y+pulse] - beforePulse[y+pulse]
            if duringPulse[y-pulse] - beforePulse[y-pulse] < 0:
                step = duringPulse[y-pulse] - beforePulse[y-pulse]   
                
            RinputDict[k] = abs(((step*0.001)/(stepsize*0.000000000001))/1000000)
        
        except:
            RinputDict[k] = np.nan
          

    return RinputDict    
    
    
#%%
    
def getAdaptation(savedLoc, closestSpike):
    
    import pickle
    from pathlib import Path
    
    path = Path(savedLoc)

    import os
    allnames = os.listdir(savedLoc)
    
    import numpy as np

    alldataDict = {}
    for i in allnames:
        # point at data file to view
        cellPath = path / i
        loadedData = pickle.load(open(cellPath, 'rb'))
        for k in loadedData.keys():
            if '_data' in k:
                alldataDict[i] = loadedData[k]
    
    from scipy import signal
    sweepDict = {}
    spikeDict = {}
    for k, v in alldataDict.items():
        peakvar = 100
        selectedsweep = np.nan
        selectedpeaks = np.nan
        for isweep in range(len(v[1])):
            peaks = signal.find_peaks(v[:,isweep],distance=40, prominence=10, height=-10)
            numofpeaks = len(peaks[0])
            #what this does is find the trace with number of spikes closest to but greater than designated number
            if numofpeaks - closestSpike < 0:
                continue
            if numofpeaks - closestSpike < peakvar:
                peakvar = numofpeaks - closestSpike
                selectedsweep = v[:,isweep]
                selectedpeaks = peaks[0]
                
            
        sweepDict[k] = selectedsweep
        spikeDict[k] = selectedpeaks
    
    
    from scipy import stats
    adaptationDict = {}
    for k, v in spikeDict.items():
        try:
            ISItoNormalize = 5
            ISIlist = v[ISItoNormalize:] - v[ISItoNormalize-1:-1]
            #normalizing to selected ISI
            ISIlistnorm = ISIlist / ISIlist[0]
            y = list(ISIlistnorm)
            x = list(range(0,len(ISIlistnorm)))
            regression = stats.linregress(x,y)
            adaptationIndex = regression[0]*100
            adaptationDict[k] = adaptationIndex
        except:
            adaptationDict[k] = np.nan


    return adaptationDict

#%%
    
def getSag(savedLoc, depolToHyperList, sagDepth):
    import pickle
    from pathlib import Path
    path = Path(savedLoc)

    import os
    allnames = os.listdir(savedLoc)

    import numpy as np
    
    alldataDict = {}
    for i in allnames:
        # point at data file to view
        cellPath = path / i
        loadedData = pickle.load(open(cellPath, 'rb'))
        for k in loadedData.keys():
            if '_data' in k:
                alldataDict[i] = loadedData[k]
    
    
    #get sag dict from same trace (same amount of neg current injection)
    sagDictST = {}
    singleTraceDict = {}
    for iCell in alldataDict.keys():
        if iCell in depolToHyperList:
            singleTraceDict[iCell] = alldataDict[iCell][:,-5]
        else:    
            singleTraceDict[iCell] = alldataDict[iCell][:,4]
        minLoc = np.argmin(singleTraceDict[iCell][1000:2000],axis = 0)
        sagST = np.mean(singleTraceDict[iCell][minLoc+997 : minLoc+1003])     
        steadystateST = np.mean(singleTraceDict[iCell][5500:6000],0) 
        sagDictST[iCell] = abs(sagST - steadystateST)
    
    
    
    #get sag dict from looking at trace that gets closest to x mV hyperpol steady state
    sagDict = {}
    for iCell in alldataDict.keys():
        columns = len(alldataDict[iCell][1])
        x = np.empty((1,columns))
        for i in range(columns):
            x[:,i] = np.mean(alldataDict[iCell][:,i][4000:6000])
        array = abs(x + sagDepth)
        index = np.argmin(array)
        minLoc = np.argmin(alldataDict[iCell][:,index][1000:2000],axis = 0)
        sag = np.mean(alldataDict[iCell][:,index][minLoc+997 : minLoc+1003])     
        steadystate = np.mean(alldataDict[iCell][:,index][5500:6000],0) 
        baseline = np.mean(alldataDict[iCell][:,index][0:900])
        sagChange = sag - baseline
        steadystateChange = steadystate - baseline
        sagDict[iCell] = 100*(steadystateChange - sagChange)/abs(sagChange)



    return sagDict , sagDictST
     



#%%
    
def getBurstiness(savedLoc, closestSpike, ISIspike):
    
    import pickle
    from pathlib import Path
    
    path = Path(savedLoc)

    import os
    allnames = os.listdir(savedLoc)
    
    import numpy as np

    alldataDict = {}
    for i in allnames:
        # point at data file to view
        cellPath = path / i
        loadedData = pickle.load(open(cellPath, 'rb'))
        for k in loadedData.keys():
            if '_data' in k:
                alldataDict[i] = loadedData[k]
    
    
    
    from scipy import signal
    #for choosing a single sweep closest to certain number of APs
    spikeDict = {}
    for i in alldataDict.keys():
        workspace = {}
        for isweep in range(len(alldataDict[i][0])):
            peaks = signal.find_peaks(alldataDict[i][:,isweep],distance=40, prominence=10, height=-10)
            workspace[isweep] = peaks[0]
        spikeDict[i] = workspace
        
    chosensweepSpikes = {}  

    for cell in spikeDict.keys():
        spikeNumDict = {}
        for k, v in spikeDict[cell].items():
            spikeNumDict[k] = len(v)
        lst = np.asarray(list(spikeNumDict.values())) 
        idx = (np.abs(lst - closestSpike)).argmin()
        chosensweepSpikes[cell] = spikeDict[cell][idx]
        
        
    burstinessDict = {}
    for k, v in chosensweepSpikes.items():
        try:
            burstinessDict[k] = (v[ISIspike - 1] - v[0])/np.mean([(v[-1] - v[-2]),(v[-2] - v[-3]),(v[-3] - v[-4])])
        except:
            burstinessDict[k] = np.nan
    
    



    
    return burstinessDict


#%%
def getMinimaDiff(savedLoc, closestSpike):

    import pickle
    from pathlib import Path
    
    path = Path(savedLoc)

    import os
    allnames = os.listdir(savedLoc)
    
    import numpy as np

    alldataDict = {}
    for i in allnames:
        # point at data file to view
        cellPath = path / i
        loadedData = pickle.load(open(cellPath, 'rb'))
        for k in loadedData.keys():
            if '_data' in k:
                alldataDict[i] = loadedData[k]
    
               
    #looks holistically at current steps
    from scipy import signal
    spikeDict = {}
    sweepDict = {}
    largestdifDict = {}
    for k, v in alldataDict.items():
        selectedsweep = np.nan
        ipeaks = np.nan
        choicedif = 0
        for itrace in range(len(v[1])):
            peaks = signal.find_peaks(v[:,itrace],distance=40, prominence=10, height=-10)
            numofpeaks = len(peaks[0])
            if any(peaks[0]>4000) == False:
                continue
            if numofpeaks < 4:
                continue
            if numofpeaks > 20:
                continue
            isweep = v[:,itrace]
            endmin = min(isweep[2000:6000])
            endmintime = np.argmin(isweep[2000:6000]) + 2000
            ipeaks = peaks[0][peaks[0] < endmintime]
            if len(ipeaks) < 2:
                continue
            mins = []
            for i in range(len(ipeaks)-1):
                mins.append(min(isweep[ipeaks[i]:ipeaks[i+1]]))  
            largestdif = max(mins-endmin)  
            if largestdif > choicedif:
                choicedif = largestdif
                selectedsweep = isweep
                selectedpeaks = ipeaks
                
        largestdifDict[k] = choicedif        
        sweepDict[k] = selectedsweep
        spikeDict[k] = selectedpeaks
        
        
    return largestdifDict    
        

#%%
def getISIratio(savedLoc):
    
    import pickle
    from pathlib import Path
    
    path = Path(savedLoc)

    import os
    allnames = os.listdir(savedLoc)
    
    import numpy as np

    alldataDict = {}
    for i in allnames:
        # point at data file to view
        cellPath = path / i
        loadedData = pickle.load(open(cellPath, 'rb'))
        for k in loadedData.keys():
            if '_data' in k:
                alldataDict[i] = loadedData[k]
    
    #averages from several traces between x and y number of spikes
    from scipy import signal
    spikeDict = {}
    sweepDict = {}
    maxISIratioDict = {}
    for k, v in alldataDict.items():
        selectedsweep = np.nan
        ipeaks = np.nan
        choiceratio = 0 #looks holistically at current steps
        averagingby = 0
        maxRatiosforAvg = 0
        
        for itrace in range(len(v[1])):
            peaks = signal.find_peaks(v[:,itrace], distance=40, prominence=10, height=-10)
            ipeaks = peaks[0]
            ipeaks = np.asarray([x for x in ipeaks if 1000<x<6000])
            numofpeaks = len(ipeaks)
            if any(peaks[0]>4000) == False:
                continue
            if numofpeaks < 6:
                continue
            if numofpeaks > 20:
                continue
            
            averagingby = averagingby + 1
            isweep = v[:,itrace]
            ISIs = ipeaks[1:] - ipeaks[0:-1] #ISIs for individual pairs of APs
            maxISIratio = max(ISIs)/min(ISIs)
            maxRatiosforAvg = maxRatiosforAvg + maxISIratio

            if maxISIratio > choiceratio: #looks holistically at current steps
                choiceratio = maxISIratio

            
        try:
            selectedratio = maxRatiosforAvg / averagingby
#            selectedratio = choiceratio
        except:
            selectedratio = np.nan
            
        maxISIratioDict[k] = selectedratio        

    
    return maxISIratioDict
    
       

#%%
def getISIvariance(savedLoc):
    
    import pickle
    from pathlib import Path
    
    path = Path(savedLoc)

    import os
    allnames = os.listdir(savedLoc)
    
    import numpy as np

    alldataDict = {}
    for i in allnames:
        # point at data file to view
        cellPath = path / i
        loadedData = pickle.load(open(cellPath, 'rb'))
        for k in loadedData.keys():
            if '_data' in k:
                alldataDict[i] = loadedData[k]
    
    #averages from several traces between x and y number of spikes
    from scipy import signal

    varianceDict = {}
    for k, v in alldataDict.items():
        ipeaks = np.nan
        averagingby = 0
        sumofsquaresforAvg = 0
        
        for itrace in range(len(v[1])):
            peaks = signal.find_peaks(v[:,itrace], distance=40, prominence=10, height=-10)
            numofpeaks = len(peaks[0])
            if any(peaks[0]>4000) == False:
                continue

            if numofpeaks < 5:
                continue
            if numofpeaks > 15:
                continue
            
            averagingby = averagingby + 1
            isweep = v[:,itrace]
            ipeaks = peaks[0]
            ISIs = [ipeaks[1:] - ipeaks[0:-1]][0:5] #first 5 ISIs for individual pairs of APs
            ISImean = np.mean(ISIs)
            ISIsquareddif = (ISIs - ISImean) * (ISIs - ISImean)
            ISIsumsquares = np.mean(ISIsquareddif)
            
            sumofsquaresforAvg  = sumofsquaresforAvg  + ISIsumsquares


        try:
            avgSumofSquares = sumofsquaresforAvg / averagingby
        except:
            avgSumofSquares = np.nan
            
        varianceDict[k] = avgSumofSquares        

    
    return varianceDict
    


#%%    
def getAHPslow(savedLoc):
    
    import pickle
    from pathlib import Path
    
    path = Path(savedLoc)

    import os
    allnames = os.listdir(savedLoc)
    
    import numpy as np
    
    alldataDict = {}
    for i in allnames:
        # point at data file to view
        cellPath = path / i
        loadedData = pickle.load(open(cellPath, 'rb'))
        for k in loadedData.keys():
            if '_data' in k:
                alldataDict[i] = loadedData[k]
    
    sAHPDict = {}
    for k, v in alldataDict.items():
        beforePulse = np.mean(v[900:999],0)
        duringPulse = np.mean(v[5000:6000],0)
        y = np.argmin(abs(duringPulse - beforePulse))
        if duringPulse[y-2] - beforePulse[y-2] > 0:
            afterPulse = np.mean(v[:,y-7][9500:10000]) #assuming step size is 50pA, grabs trace of 350 pA positive step and looks at 400ms after step ends
        if duringPulse[y-2] - beforePulse[y-2] < 0:
            afterPulse = np.mean(v[:,y+7][9500:10000])
        
        sAHPDict[k] = beforePulse[y] - afterPulse
        
        
    return sAHPDict


#%%
    
def getISratio(savedLoc,sweep, closestSpike, firstSpike):
    
    import pickle
    from pathlib import Path
    
    path = Path(savedLoc)

    import os
    allnames = os.listdir(savedLoc)
    
    import numpy as np

    alldataDict = {}
    for i in allnames:
        # point at data file to view
        cellPath = path / i
        loadedData = pickle.load(open(cellPath, 'rb'))
        for k in loadedData.keys():
            if '_data' in k:
                alldataDict[i] = loadedData[k]
    

    
    
    from scipy import signal

    spikeDict = {}
    for i in alldataDict.keys():
        workspace = {}
        for isweep in range(len(alldataDict[i][0])):
            peaks = signal.find_peaks(alldataDict[i][:,isweep],distance=40, prominence=10, height=-10)
            workspace[isweep] = peaks[0]
        spikeDict[i] = workspace
        

    chosensweepDict = {}  
    for cell in spikeDict.keys():
        spikeNumDict = {}
        for k, v in spikeDict[cell].items():
            spikeNumDict[k] = len(v)
        lst = np.asarray(list(spikeNumDict.values())) 
        idx = (np.abs(lst - closestSpike)).argmin()
        chosensweepDict[cell] = spikeDict[cell][idx]    
    
    
    ISratio = {}
    for icell in chosensweepDict.keys():
        try:
            if (chosensweepDict[icell][1]-chosensweepDict[icell][0]) / (chosensweepDict[icell][-1]-chosensweepDict[icell][-2]) == 1:
                ISratio[icell] = np.nan
            else:
                ISratio[icell] = (chosensweepDict[icell][-1]-chosensweepDict[icell][-2]) / (chosensweepDict[icell][firstSpike]-chosensweepDict[icell][firstSpike-1])
        except:
            ISratio[icell] = np.nan
               
        
        
    return ISratio
    
#%%
    
def getAHP(savedLoc, depolToHyperList, spikeNumAHP):
    import pickle
    from pathlib import Path
    path = Path(savedLoc)

    import os
    allnames = os.listdir(savedLoc)

    import numpy as np
    
    alldataDict = {}
    for i in allnames:
        # point at data file to view
        cellPath = path / i
        loadedData = pickle.load(open(cellPath, 'rb'))
        for k in loadedData.keys():
            if '_data' in k:
                alldataDict[i] = loadedData[k]
    
    
    from scipy import signal

    spikeDict = {}
    for i in alldataDict.keys():
        workspace = {}
        for isweep in range(len(alldataDict[i][0])):
            peaks = signal.find_peaks(alldataDict[i][:,isweep],distance=40, prominence=10, height=-10)
            workspace[isweep] = peaks[0]
        spikeDict[i] = workspace
        

    chosensweepDict = {}  
    for cell in spikeDict.keys():
        spikeNumDict = {}
        for k, v in spikeDict[cell].items():
            spikeNumDict[k] = len(v)
        lst = np.asarray(list(spikeNumDict.values())) 
        idx = (np.abs(lst - spikeNumAHP)).argmin()
        chosensweepDict[cell] = alldataDict[cell][:,idx]    
    


    AHPDict = {}
    for cell in chosensweepDict.keys():
        bl = np.mean(chosensweepDict[cell][700:900])
        ahp = chosensweepDict[cell][6000:8000].min()
        ahpAmp = np.abs(bl-ahp)
        AHPDict[cell] = ahpAmp


    return  AHPDict



#%%
    
def getSpikeShape(savedLoc, depolToHyperList, spikeNumAHP):
    import pickle
    from pathlib import Path
    path = Path(savedLoc)

    import os
    allnames = os.listdir(savedLoc)

    import numpy as np
    
    alldataDict = {}
    for i in allnames:
        # point at data file to view
        cellPath = path / i
        loadedData = pickle.load(open(cellPath, 'rb'))
        for k in loadedData.keys():
            if '_data' in k:
                alldataDict[i] = loadedData[k]
    
    
    from scipy import signal

    spikeDict = {}
    for i in alldataDict.keys():
        workspace = {}
        for isweep in range(len(alldataDict[i][0])):
            peaks = signal.find_peaks(alldataDict[i][:,isweep],distance=40, prominence=10, height=-10)
            workspace[isweep] = peaks[0]
        spikeDict[i] = workspace
        

    chosensweepDict = {}  
    for cell in spikeDict.keys():
        spikeNumDict = {}
        for k, v in spikeDict[cell].items():
            spikeNumDict[k] = len(v)
        lst = np.asarray(list(spikeNumDict.values()))
        minslst = np.abs(lst - spikeNumAHP)
        modlst = [999 if x == spikeNumAHP else x for x in minslst]
        idx = np.argmin(modlst)
        chosensweepDict[cell] = alldataDict[cell][:,idx]   
    


    spike = {}
    spikeAHP = {}
    spikeWidth = {}
    for k, v in chosensweepDict.items():
        peaks = signal.find_peaks(v,distance=40, prominence=10, height=-10)

        chosenAP = peaks[0][-1] 
        spikeShape = v[chosenAP-100:chosenAP+300]
        
        spikeBL = np.mean(v[chosenAP-15:chosenAP-10])
        spikeAmp = v[chosenAP]
        halfPoint = (spikeAmp+spikeBL) / 2
        for i in range(100,130):
            if spikeShape[i]<halfPoint:
                back = i
                break
        for i in reversed(range(70,100)):
            if spikeShape[i]<halfPoint:
                front = i
                break
            
        halfWidth = (back - front)/ 10

        spike[k] = spikeShape - np.mean(v[chosenAP-12:chosenAP-8])
        spikeAHP[k] = np.mean(v[chosenAP-15:chosenAP-10]) - np.min(v[chosenAP:chosenAP+200])
        spikeWidth[k] = halfWidth
    



    return  spike, spikeAHP, spikeWidth



#%%
    
def getAPsAfterThresh(savedLoc, depolToHyperList, time):
    
    #find first current step that gives AP
    #cound how many APs within 100 ms following first AP
    #repeat for every +50 pA steps after to make line graphs

    import pickle
    from pathlib import Path
    path = Path(savedLoc)

    import os
    allnames = os.listdir(savedLoc)
 
    import numpy as np
    alldataDict = {}
    for i in allnames:
        
        # point at data file to view
        cellPath = path / i
        loadedData = pickle.load(open(cellPath, 'rb'))
        for k in loadedData.keys():
            if '_data' in k:              
                alldataDict[i] = loadedData[k]
 

    from scipy import signal
 
    spikeDict = {}
    for i in alldataDict.keys():    
        workspace = {}
        for isweep in range(len(alldataDict[i][0])):           
            peaks = signal.find_peaks(alldataDict[i][:,isweep],distance=40, prominence=10, height=-10)
            workspace[isweep] = peaks[0]
        spikeDict[i] = workspace
    
    
    chosensweepDict = {}  
    for cell in spikeDict.keys():   
        
        if cell in depolToHyperList:
            x = reversed(range(len(spikeDict[cell].keys()))) 
        else:
            x = range(len(spikeDict[cell].keys()))
            
        for i in x: 

            if len(spikeDict[cell][i]) == 0:
                continue
            if len(spikeDict[cell][i]) > 0:
                chosensweepDict[cell] = spikeDict[cell][i+1]
                break
              
    
    spikeNumDict = {}
    latencyDict = {}
    for cell in chosensweepDict.keys():

        spikeNumDict[cell] = sum(chosensweepDict[cell]<(chosensweepDict[cell][0]+time))
        latencyDict[cell] = chosensweepDict[cell][0] - 1000

    return spikeNumDict, latencyDict

 #%%   
    
def getAHPNew(savedLoc, depolToHyperList, spikeNumAHP):
  
    #find trace with roughly equal number of APs
    #find min val after every spike (search range until next spike, if last spike then deal with that)
    #compare to pre-spike value (like 5-10 ms before spike)
    #that largest value is returned (largest AHP, for IB usually after the burst)

    
    import pickle
    from pathlib import Path
    path = Path(savedLoc)

    import os
    allnames = os.listdir(savedLoc)
 
    import numpy as np
    alldataDict = {}
    for i in allnames:
        
        # point at data file to view
        cellPath = path / i
        loadedData = pickle.load(open(cellPath, 'rb'))
        for k in loadedData.keys():
            if '_data' in k:              
                alldataDict[i] = loadedData[k]
 

    from scipy import signal
 
    spikeDict = {}
    for i in alldataDict.keys():    
        workspace = {}
        for isweep in range(len(alldataDict[i][0])):           
            peaks = signal.find_peaks(alldataDict[i][:,isweep],distance=40, prominence=10, height=-10)
            workspace[isweep] = peaks[0]
        spikeDict[i] = workspace
    
    
    chosensweepDict = {}  
    test = {}
    for cell in spikeDict.keys():   
        spikeNumDict = {}
        for k, v in spikeDict[cell].items():           
            spikeNumDict[k] = len(v)
        lst = np.asarray(list(spikeNumDict.values()))
        minslst = np.abs(lst - spikeNumAHP)
        modlst = [999 if x == spikeNumAHP else x for x in minslst]
        idx = np.argmin(modlst)
        chosensweepDict[cell] = alldataDict[cell][:,idx]
        test[cell] = list(spikeDict[cell][idx])


    ahpDict = {}
    for icell in test.keys():
        ahpList = []
        
    
        
        for spike in range(len(test[icell])):      
            #make list of min between each and immediately before, if last in list, compare to 6000
            if spike == len(test[icell])-1:       
                x = chosensweepDict[icell]
                y = test[icell][spike]
                ahp = np.abs(np.mean(x[y-15:y-10]) - np.min(x[y:6010]))
            else:             
                x = chosensweepDict[icell]
                y = test[icell][spike]
                z = test[icell][spike+1]
                ahp = np.abs(np.mean(x[y-15:y-10]) - np.min(x[y:z]))

            ahpList.append(ahp)
        
            #compare within list
            maxAHP = max(ahpList)
        
            #output largest val
            ahpDict[icell] = maxAHP
    

    return ahpDict

#%%
    
def getEnvelope(savedLoc, depolToHyperList, closestSpike):
    
    
    import pickle
    from pathlib import Path
    
    path = Path(savedLoc)

    import os
    allnames = os.listdir(savedLoc)
    
    import numpy as np

    alldataDict = {}
    for i in allnames:
        # point at data file to view
        cellPath = path / i
        loadedData = pickle.load(open(cellPath, 'rb'))
        for k in loadedData.keys():
            if '_data' in k:
                alldataDict[i] = loadedData[k]
    
    #averages from several traces between x and y number of spikes
    from scipy import signal

    maxAPheightdiffDict = {}
    for k, v in alldataDict.items():
        ipeaks = np.nan
#        choiceratio = 0 #looks holistically at current steps
        averagingby = 0
        peakHeightsforAvg = 0
        maxpeakHeightdiff = 100
        for itrace in range(len(v[1])):
            peaks = signal.find_peaks(v[:,itrace], distance=40, prominence=10, height=-10)
            numofpeaks = len(peaks[0])
            if any(peaks[0]>4000) == False:
                continue
            
            if numofpeaks < 5:
                continue
            if numofpeaks > 15:
                continue

            averagingby = averagingby + 1
            isweep = v[:,itrace]
            ipeaks = np.asarray([x for x in peaks[0] if x<(peaks[0][0]+1000)])
            if len(ipeaks) < 2:
                continue
            peakheights = isweep[ipeaks]
            bases = isweep[ipeaks-10]
            APheights = peakheights - bases
            
            maxheightdiff = min(APheights)/max(APheights)*100
            
             
            peakHeightsforAvg  = peakHeightsforAvg  + maxheightdiff

            if maxheightdiff < maxpeakHeightdiff:
                maxpeakHeightdiff = maxheightdiff

        try:
            maxdiffAPheight = peakHeightsforAvg / averagingby
#            maxdiffAPheight = maxpeakHeightdiff
        except:
            maxdiffAPheight = np.nan
            
        maxAPheightdiffDict[k] = maxdiffAPheight  
        


    
    return maxAPheightdiffDict


#%%
def gethowmanyAPs(savedLoc, depolToHyperList, closestSpike):
    
    
    import pickle
    from pathlib import Path
    
    path = Path(savedLoc)

    import os
    allnames = os.listdir(savedLoc)
    
    import numpy as np

    alldataDict = {}
    for i in allnames:
        # point at data file to view
        cellPath = path / i
        loadedData = pickle.load(open(cellPath, 'rb'))
        for k in loadedData.keys():
            if '_data' in k:
                alldataDict[i] = loadedData[k]
    
    #averages from several traces between x and y number of spikes
    from scipy import signal

    apDict = {}
    for k, v in alldataDict.items():
        ipeaks = np.nan
        averagingby = 0
        apsForAvg = 0
        maxAps = 0
        for itrace in range(len(v[1])):
            peaks = signal.find_peaks(v[:,itrace], distance=40, prominence=10, height=-10)
            numofpeaks = len(peaks[0])
            if any(peaks[0]>4000) == False:
                continue
            
            if numofpeaks < 5:
                continue
            if numofpeaks > 15:
                continue
            
            averagingby = averagingby + 1
            isweep = v[:,itrace]
            ipeaks = np.asarray([x for x in peaks[0] if x<(peaks[0][0]+400)])
            start = len(ipeaks)
            total = numofpeaks
            
            
            difference = start/total*100
            

            apsForAvg  = apsForAvg  + difference


        try:
            apDict[k] = apsForAvg / averagingby
        except:
            apDict[k] = np.nan
            
        


    
    return apDict


    
#%%

def getVrest(VrestLoc, savedLoc):
    
    import pickle
    from pathlib import Path
    
    path = Path(VrestLoc)

    import os
    allnames = os.listdir(VrestLoc)
    nameswithtype = os.listdir(savedLoc)
    
    import numpy as np

    alldataDict = {}
    for i in allnames:
        # point at data file to view
        cellPath = path / i
        loadedData = pickle.load(open(cellPath, 'rb'))
        for k in loadedData.keys():
            if '_data' in k:
                alldataDict[i] = loadedData[k]

    
    singlesweepDict = {}
    for i in nameswithtype:
        singlesweepDict[i] = np.nan
    
    for i in alldataDict.keys():
        sweepData = alldataDict[i]
        try:
            name = [x for x in nameswithtype if i[:-13] in x][0]
            singlesweepDict[name] = np.mean(sweepData[0:900])
        except:
            singlesweepDict[name] = np.nan
            
    return singlesweepDict



#%%
    
def getStat(IB, RS):
    
    import scipy.stats
    
    #independent samples t test
    # pVal = "%.3f" % scipy.stats.ttest_ind(IB, RS, nan_policy='omit')[1]
    
    # Mann Whitney U
    pVal = "%.3f" % scipy.stats.mannwhitneyu(IB, RS)[1]
    
    if float(pVal) < 0.05:
       color = 'red'
    else:
       color = 'black'
    
    return pVal, color
    
    
    

    
    