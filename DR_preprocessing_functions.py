# -*- coding: utf-8 -*-
#%% 
def plot_ws(filePath):
    # function for plotting a data in a wavesurfer file from console
    
    # import modules
    from pywavesurfer import ws
    import matplotlib.pyplot as plt
     
    # load data
    data = ws.loadDataFile(filename= filePath, format_string='single' )
    
    plt.figure()
    # plot data
    for iKey in data.items():
        if iKey[0] != 'header':
            plt.plot(iKey[1]['analogScans'][0,:], label = iKey[0]);
    plt.legend()
    plt.show()   
 
#%% 
def getGoodMean(badTraces, filePath, BLstart=None, BLstop=None):
    # this function will create one mean trace from all sweeps in the session except the 
    # sweeps indicated in "badTrace" list. Will also get experiment info from header.
    
    # Save the mean with a file name that allows precise identification of the 
    # mouse, cell and stim prameters. 
    # future scripts will load these files and automatically generates averages over cells/mice 
    # and make plots / output data tables for statistics 
    
    from pywavesurfer import ws
    import numpy as np
        
    badList = []
    for i in range(len(badTraces)):
        badList.append("sweep_%04d" % badTraces[i])
           
    data = ws.loadDataFile(filename= filePath, format_string='single' )  # load data
    
    # get header info and put in a dictionary
    Exp = {} # dict.fromkeys(['Class', 'MapName', 'TypeOfStim', 'StimName', 'StimAmp', 'StimTime', 'StimeDuration', 'StimISI'], [None]*5)
    Exp['Origin'] = [filePath]
    Exp['SampleRateAcq'] = int(np.asscalar(data['header']['AcquisitionSampleRate']))
    Exp['SampleRateStim'] = int(np.asscalar(data['header']['StimulationSampleRate']))
    Exp['sweepLength'] = int(np.asscalar(data['header']['ExpectedSweepScanCount']))
    Exp['SessionNo'] = int(np.asscalar(data['header']['SessionIndex']))
    Exp['Class'] = str(data['header']['StimulusLibrary']['SelectedOutputableClassName'], encoding = 'ascii')
    if 'Sequence' in Exp['Class']:
        StimSeqUsed = data['header']['StimulusLibrary']['SelectedOutputableIndex']
        Exp['SequenceName'] = str(data['header']['StimulusLibrary']['Sequences'][('element%d' %StimSeqUsed)]['Name'], encoding = 'ascii')
        MapsUsedInSeq = data['header']['StimulusLibrary']['Sequences'][('element%d' %StimSeqUsed)]['IndexOfEachMapInLibrary'] 
        for v in MapsUsedInSeq.values():
            StimMapUsed = v
            StimMapName = str(data['header']['StimulusLibrary']['Maps'][('element%d' %StimMapUsed)]['Name'], encoding = 'ascii')
            StimID = list(data['header']['StimulusLibrary']['Maps'][('element%d' %StimMapUsed)]['IndexOfEachStimulusInLibrary'].values())
            Exp[StimMapName] = {}
            Exp[StimMapName]['TypeOfStim'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % iStim)]['TypeString'], encoding='ascii') for idx, iStim in enumerate(StimID))
            Exp[StimMapName]['StimName'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Name'], encoding='ascii') for i in range(len(StimID)))
            Exp[StimMapName]['StimTime'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Delay'], encoding='ascii') for i in range(len(StimID)))
            Exp[StimMapName]['StimAmp'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Amplitude'], encoding='ascii')  
            if 'SquarePulse' == Exp[StimMapName]['TypeOfStim'][i] 
            else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['FirstPulseAmplitude'], encoding='ascii')
            for i in range(len(StimID)))
            Exp[StimMapName]['StimDuration'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Duration'], encoding='ascii') 
            if 'SquarePulse' == Exp[StimMapName]['TypeOfStim'][i]
            else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['FirstPulseDuration'], encoding='ascii')
            for i in range(len(StimID)))
            Exp[StimMapName]['StimISI'] = list('None' if 'SquarePulse' == Exp[StimMapName]['TypeOfStim'][i]
            else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['DelayBetweenPulses'], encoding='ascii') 
            for i in range(len(StimID)))
    elif 'Map' in Exp['Class']:
        StimMapUsed = data['header']['StimulusLibrary']['SelectedOutputableIndex']
        Exp['MapName'] = str(data['header']['StimulusLibrary']['Maps'][('element%d' %StimMapUsed)]['Name'], encoding = 'ascii')
        StimID = list(data['header']['StimulusLibrary']['Maps'][('element%d' %StimMapUsed)]['IndexOfEachStimulusInLibrary'].values())
        Exp['TypeOfStim'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % iStim)]['TypeString'], encoding='ascii') for idx, iStim in enumerate(StimID))
        Exp['StimName'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Name'], encoding='ascii') for i in range(len(StimID)))
        Exp['StimTime'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Delay'], encoding='ascii') for i in range(len(StimID)))
        Exp['StimAmp'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Amplitude'], encoding='ascii')  
        if 'SquarePulse' == Exp['TypeOfStim'][i] 
        else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['FirstPulseAmplitude'], encoding='ascii')
        for i in range(len(StimID)))
        Exp['StimDuration'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Duration'], encoding='ascii') 
        if 'SquarePulse' == Exp['TypeOfStim'][i]
        else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['FirstPulseDuration'], encoding='ascii')
        for i in range(len(StimID)))
        Exp['StimISI'] = list('None' if 'SquarePulse' == Exp['TypeOfStim'][i]
        else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['DelayBetweenPulses'], encoding='ascii') 
        for i in range(len(StimID)))
    
    del data['header']  # delete header
    
    dataArray = np.empty((Exp['SampleRateAcq'],0), dtype=np.float32)
    
    for k, v in data.items():
        if k in badList: continue
        dataVals = np.transpose(v["analogScans"])
        dataArray = np.append(dataArray, dataVals, 1) 
     
    # get baseline (if defined) then average
    if BLstart == None or BLstop == None:
        BLdataArray = dataArray
    else:
        baseline = np.mean(dataArray[BLstart:BLstop],0) 
        BLdataArray = dataArray - baseline
        
    dataMean = np.mean(BLdataArray,1)
    Exp['dataMean'] = dataMean    
    
    # save average into a wavedump
    import tkinter
    from tkinter.filedialog import asksaveasfilename
    tkinter.Tk().withdraw()
    saveAsFilename = asksaveasfilename()  # specify save folder and name,add .pkl if pickiling
    
    import pickle
    pickle.dump(Exp, open(saveAsFilename, 'wb')) # save whole dictionary as pkl file
#    np.save(saveAsFilename,dataMean)   # save as npy file
    
#    to load:
#    data = pickle.load(open('filepath', 'rb'))


#%%     
def loadExpData(dataloc):
    
    # get folder
    import tkinter
    from tkinter.filedialog import askdirectory
    tkinter.Tk().withdraw()
    dirPath = askdirectory(initialdir = dataloc)   # point at data file to view

    # cycle through folder content (should be sessions)
    import os
    from pywavesurfer import ws
    import numpy as np
#    import GL_utilitis as utls
    
    Exp = {} # dict.fromkeys(['Class', 'MapName', 'TypeOfStim', 'StimName', 'StimAmp', 'StimTime', 'StimeDuration', 'StimISI'], [None]*5)
    
    for iFile in os.listdir(dirPath):    
        data = ws.loadDataFile(filename= dirPath + '/' + iFile, format_string='single' )  # load data from file
        
        # get header info and put in a dictionary
        Exp[iFile] = {}
        Exp[iFile]['Origin'] = [dirPath + '/' + iFile]
        Exp[iFile]['SampleRateAcq'] = int(np.asscalar(data['header']['AcquisitionSampleRate']))
        Exp[iFile]['SampleRateStim'] = int(np.asscalar(data['header']['StimulationSampleRate']))
        Exp[iFile]['sweepLength'] = int(np.asscalar(data['header']['ExpectedSweepScanCount']))
        Exp[iFile]['SessionNo'] = int(np.asscalar(data['header']['SessionIndex']))
        Exp[iFile]['Class'] = str(data['header']['StimulusLibrary']['SelectedOutputableClassName'], encoding = 'ascii')
        if 'Sequence' in Exp[iFile]['Class']:
            StimSeqUsed = data['header']['StimulusLibrary']['SelectedOutputableIndex']
            Exp[iFile]['StimSeqUsed'] = StimSeqUsed
            Exp[iFile]['SequenceName'] = str(data['header']['StimulusLibrary']['Sequences'][('element%d' %StimSeqUsed)]['Name'], encoding = 'ascii')
            MapsUsedInSeq = data['header']['StimulusLibrary']['Sequences'][('element%d' %StimSeqUsed)]['IndexOfEachMapInLibrary'] 
            Exp[iFile]['MapsInSeq'] = MapsUsedInSeq
            Exp[iFile]['AllMaps'] = []
            for v in MapsUsedInSeq.values():
                StimMapUsed = v
                StimMapName = str(data['header']['StimulusLibrary']['Maps'][('element%d' %StimMapUsed)]['Name'], encoding = 'ascii')
                StimID = list(data['header']['StimulusLibrary']['Maps'][('element%d' %StimMapUsed)]['IndexOfEachStimulusInLibrary'].values())
                Exp[iFile]['AllMaps'].append(StimMapName)
                Exp[iFile][StimMapName] = {}
                Exp[iFile][StimMapName]['TypeOfStim'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % iStim)]['TypeString'], encoding='ascii') for idx, iStim in enumerate(StimID))
                Exp[iFile][StimMapName]['StimName'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Name'], encoding='ascii') for i in range(len(StimID)))
                Exp[iFile][StimMapName]['StimTime'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Delay'], encoding='ascii') for i in range(len(StimID)))
                Exp[iFile][StimMapName]['StimAmp'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Amplitude'], encoding='ascii')  
                if 'SquarePulse' == Exp[iFile][StimMapName]['TypeOfStim'][i] 
                else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['FirstPulseAmplitude'], encoding='ascii')
                for i in range(len(StimID)))
                Exp[iFile][StimMapName]['StimDuration'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Duration'], encoding='ascii') 
                if 'SquarePulse' == Exp[iFile][StimMapName]['TypeOfStim'][i]
                else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['FirstPulseDuration'], encoding='ascii')
                for i in range(len(StimID)))
                Exp[iFile][StimMapName]['StimISI'] = list('None' if 'SquarePulse' == Exp[iFile][StimMapName]['TypeOfStim'][i]
                else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['DelayBetweenPulses'], encoding='ascii') 
                for i in range(len(StimID)))
        elif 'Map' in Exp[iFile]['Class']:
            StimMapUsed = data['header']['StimulusLibrary']['SelectedOutputableIndex']
            Exp[iFile]['MapName'] = str(data['header']['StimulusLibrary']['Maps'][('element%d' %StimMapUsed)]['Name'], encoding = 'ascii')
            StimID = list(data['header']['StimulusLibrary']['Maps'][('element%d' %StimMapUsed)]['IndexOfEachStimulusInLibrary'].values())
            Exp[iFile]['TypeOfStim'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % iStim)]['TypeString'], encoding='ascii') for idx, iStim in enumerate(StimID))
            Exp[iFile]['StimName'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Name'], encoding='ascii') for i in range(len(StimID)))
            Exp[iFile]['StimTime'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Delay'], encoding='ascii') for i in range(len(StimID)))
            
            if 'SquarePulseTrain' in Exp[iFile]['TypeOfStim']:
                Exp[iFile]['StimAmp'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Amplitude'], encoding='ascii')
                for i in range(len(StimID)))
                
                Exp[iFile]['StimTotalDuration'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Duration'], encoding='ascii') 
                for i in range(len(StimID)))
               
                Exp[iFile]['StimPeriod'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Period'], encoding='ascii') 
                for i in range(len(StimID)))
                
                Exp[iFile]['StimPulseDuration'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['PulseDuration'], encoding='ascii') 
                for i in range(len(StimID)))
                
            else:    
                Exp[iFile]['StimAmp'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Amplitude'], encoding='ascii') 
                if 'SquarePulse' == Exp[iFile]['TypeOfStim'][i] 
                else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['FirstPulseAmplitude'], encoding='ascii')
                for i in range(len(StimID)))
                
                Exp[iFile]['StimDuration'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Duration'], encoding='ascii') 
                if 'SquarePulse' == Exp[iFile]['TypeOfStim'][i]
                else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['FirstPulseDuration'], encoding='ascii')
                for i in range(len(StimID)))
               
                Exp[iFile]['StimISI'] = list('None' if 'SquarePulse' == Exp[iFile]['TypeOfStim'][i]
                else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['DelayBetweenPulses'], encoding='ascii') 
                for i in range(len(StimID)))
        
        
        dataArray = np.empty((Exp[iFile]['sweepLength'],0), dtype=np.float32)
 
        for k, v in data.items():
            if k == 'header':
                continue
            dataVals = np.transpose(v["analogScans"])
            try:
                dataArray = np.append(dataArray, dataVals, 1)
            except: continue
            
        if 'Map' in Exp[iFile]['Class']:
             Exp[iFile]['dataArray'] = dataArray
        elif 'Sequence' in Exp[iFile]['Class']:
             for iMap in range(len(Exp[iFile]['MapsInSeq'])):
                  elementVal = Exp[iFile]['MapsInSeq']['element'+str(int(iMap)+1)]
                  name = str(data['header']['StimulusLibrary']['Maps'][('element%d' % elementVal)]['Name'], encoding = 'ascii')
                  Exp[iFile][name + '_data'] = dataArray[:,iMap::len(Exp[iFile]['MapsInSeq'])]

    return Exp


#%%
def showSession(dataDict, sessionNum, baseline, BLstart, BLstop):
    from pywavesurfer import ws
    import matplotlib.pyplot as plt
    import numpy as np
    
    #set session name
    if len(list(dataDict.keys())[0]) > 30:
        firstSession = list(dataDict.keys())[0]
    else:
        #firstSession = list(dataDict.keys())[1]
        #changed to below on 220525 to handle experiments where only one session - but might be bug from GL code?
        firstSession = list(dataDict.keys())[0]
        
    # sessionBase = firstSession[0:13]
    #changed to below on 220526 to handle experiments where cell number is double digits (cell10 or more)
    instance = 0
    for counter, iChar in enumerate(firstSession):
       if iChar == '_':
           instance = instance + 1
           if instance == 2:
               sessionBase = firstSession[:counter+1]


    sameSessionList = list(k for k in dataDict.keys() if (sessionBase + '%03d' % sessionNum) in k)
    if len(sameSessionList) == 1:
        sessionName = sameSessionList[0]
    else:
        sessionChoice = input('define which of the %s sessions:' %len(sameSessionList))
        sessionName = sameSessionList[int(sessionChoice)-1]
            
    # load data
    filePath = dataDict[sessionName]['Origin'][0]
    data = ws.loadDataFile(filename= filePath, format_string='single' )
    
    # plot data    
    
    if 'Sequence' in dataDict[sessionName]['Class']:
        
        #make list with sweep names                 
        if 'header' in data.keys(): 
            sweep_list = list(data.keys())
            sweep_list.remove('header')
            
            #slice into groups for each map
            numMapsinSeq = len(dataDict[sessionName]['MapsInSeq'].keys())
            sweepDict = {}
            for i in range(numMapsinSeq):
                sweepDict['Map'+str(i+1)+'_sweeps'] = sweep_list[i::numMapsinSeq]      
                
            #put appropriate sweeps into subplots
            fig, axes = plt.subplots(numMapsinSeq, 1, sharey=True, sharex=True)
            for index, iKey in enumerate(sweepDict.keys()):
                for iSweep in sweepDict[iKey]:
                    if baseline == 0:
                        baselineData = data[iSweep]['analogScans'][0,:]
                    elif baseline == 1:
                        trace = data[iSweep]['analogScans'][0,:]
                        BL = np.mean(trace[BLstart:BLstop],0) 
                        baselineData = trace - BL
                    else:
                        baselineData = data[iSweep]['analogScans'][0,:]
                        print("it's a yes or no question, dummy")
                    axes[index].plot(baselineData, label = iSweep)
                    axes[index].legend(loc = 'upper right')
                    axes[index].set_title(str(iKey))
            fig.show() 
                
                
    else:
        if len(list(data.keys())) > 16:
            indexChunks = [list(data.keys())[i:i+10] for i in range(0, len(list(data.keys())), 10)]
        else:
            indexChunks = [list(data.keys())]
        # indexList_cut = np.array_split(indexList,5)
        
        
        for iChunk in indexChunks:
            plt.figure()
            dataChunk = {}
            for i in iChunk:
                dataChunk[i] = data[i]  
            
            for iKey in dataChunk.items():
                if iKey[0] != 'header':
                    # for each map in maps in seq start new fig (pl.figure(iMap))
                    # plot the analoguescans for the appropriate sweeps (add jumping from key0 to key 3 etc,)
                    if baseline == 0:
                        baselineDataChan1 = iKey[1]['analogScans'][0,:]
                        if len(iKey[1]['analogScans']) > 1:
                            baselineDataChan2 = iKey[1]['analogScans'][1,:]
                    elif baseline == 1:
                        traceChan1 = iKey[1]['analogScans'][0,:]
                        BLChan1 = np.mean(traceChan1[BLstart:BLstop],0)
                        baselineDataChan1 = traceChan1 - BLChan1
                        if len(iKey[1]['analogScans']) > 1:
                            traceChan2 = iKey[1]['analogScans'][1,:]
                            BLChan2 = np.mean(traceChan2[BLstart:BLstop],0)
                            baselineDataChan2 = traceChan2 - BLChan2
                    
                    if len(iKey[1]['analogScans']) > 1:
                        fig, (ax1, ax2) = plt.subplots(2, sharex=True)    
                        
                        ax1.plot(baselineDataChan1, label = iKey[0], linewidth=0.8)
                        ax2.plot(baselineDataChan2, label = iKey[0], linewidth=0.8);
                    else:    
                        plt.plot()
                        plt.plot(baselineDataChan1, label = iKey[0], linewidth=0.8);
            plt.legend(loc = 'upper right')
            plt.show() 
            
    
#%%
def saveSessionAvr(dataDict, sessionNum, badTraces, saveloc, date, genotype, mouseID, cellID, delay, imageloc, fig,  plotMin, plotMax, plotStart, plotStop, color, equivalentName, BLstart=None, BLstop=None):
    from pywavesurfer import ws
    import numpy as np
         
    # get file path    
    if len(list(dataDict.keys())[0]) > 30:
        firstSession = list(dataDict.keys())[0]
    else:
        firstSession = list(dataDict.keys())[1]
    
    # check if there ar identical sessions in the folder, if there are, pick which on to use    
    sessionBase = firstSession[0:13]
    sameSessionList = list(k for k in dataDict.keys() if (sessionBase + '%03d' % sessionNum) in k)
    if len(sameSessionList) == 1:
        sessionName = sameSessionList[0]
    else:
        sessionChoice = input('define which of the %s sessions:' %len(sameSessionList))
        sessionName = sameSessionList[int(sessionChoice)-1]
        
    filePath = dataDict[sessionName]['Origin'][0]
        
    badList = []
    for i in range(len(badTraces)):
        badList.append("sweep_%04d" % badTraces[i])
        
    data = ws.loadDataFile(filename= filePath, format_string='single' )  # load data
    
    # get header info and put in a dictionary
    Exp = {} # dict.fromkeys(['Class', 'MapName', 'TypeOfStim', 'StimName', 'StimAmp', 'StimTime', 'StimeDuration', 'StimISI'], [None]*5)
    Exp['Origin'] = [filePath]
    Exp['SampleRateAcq'] = int(np.asscalar(data['header']['AcquisitionSampleRate']))
    Exp['SampleRateStim'] = int(np.asscalar(data['header']['StimulationSampleRate']))
    Exp['sweepLength'] = int(np.asscalar(data['header']['ExpectedSweepScanCount']))
    Exp['SessionNo'] = int(np.asscalar(data['header']['SessionIndex']))
    Exp['Class'] = str(data['header']['StimulusLibrary']['SelectedOutputableClassName'], encoding = 'ascii')
    if 'Sequence' in Exp['Class']:
        StimSeqUsed = data['header']['StimulusLibrary']['SelectedOutputableIndex']
        Exp['SequenceName'] = str(data['header']['StimulusLibrary']['Sequences'][('element%d' %StimSeqUsed)]['Name'], encoding = 'ascii')
        MapsUsedInSeq = data['header']['StimulusLibrary']['Sequences'][('element%d' %StimSeqUsed)]['IndexOfEachMapInLibrary'] 
        for v in MapsUsedInSeq.values():
            StimMapUsed = v
            StimMapName = str(data['header']['StimulusLibrary']['Maps'][('element%d' %StimMapUsed)]['Name'], encoding = 'ascii')
            StimID = list(data['header']['StimulusLibrary']['Maps'][('element%d' %StimMapUsed)]['IndexOfEachStimulusInLibrary'].values())
            Exp[StimMapName] = {}
            Exp[StimMapName]['TypeOfStim'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % iStim)]['TypeString'], encoding='ascii') for idx, iStim in enumerate(StimID))
            Exp[StimMapName]['StimName'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Name'], encoding='ascii') for i in range(len(StimID)))
            Exp[StimMapName]['StimTime'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Delay'], encoding='ascii') for i in range(len(StimID)))
            Exp[StimMapName]['StimAmp'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Amplitude'], encoding='ascii')  
            if 'SquarePulse' == Exp[StimMapName]['TypeOfStim'][i] 
            else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['FirstPulseAmplitude'], encoding='ascii')
            for i in range(len(StimID)))
            Exp[StimMapName]['StimDuration'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Duration'], encoding='ascii') 
            if 'SquarePulse' == Exp[StimMapName]['TypeOfStim'][i]
            else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['FirstPulseDuration'], encoding='ascii')
            for i in range(len(StimID)))
            Exp[StimMapName]['StimISI'] = list('None' if 'SquarePulse' == Exp[StimMapName]['TypeOfStim'][i]
            else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['DelayBetweenPulses'], encoding='ascii') 
            for i in range(len(StimID)))
    elif 'Map' in Exp['Class']:
        StimMapUsed = data['header']['StimulusLibrary']['SelectedOutputableIndex']
        Exp['MapName'] = str(data['header']['StimulusLibrary']['Maps'][('element%d' %StimMapUsed)]['Name'], encoding = 'ascii')
        StimID = list(data['header']['StimulusLibrary']['Maps'][('element%d' %StimMapUsed)]['IndexOfEachStimulusInLibrary'].values())
        Exp['TypeOfStim'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % iStim)]['TypeString'], encoding='ascii') for idx, iStim in enumerate(StimID))
        Exp['StimName'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Name'], encoding='ascii') for i in range(len(StimID)))
        Exp['StimTime'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Delay'], encoding='ascii') for i in range(len(StimID)))
        Exp['StimAmp'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Amplitude'], encoding='ascii')  
        if 'SquarePulse' == Exp['TypeOfStim'][i] 
        else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['FirstPulseAmplitude'], encoding='ascii')
        for i in range(len(StimID)))
        Exp['StimDuration'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Duration'], encoding='ascii') 
        if 'SquarePulse' == Exp['TypeOfStim'][i]
        else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['FirstPulseDuration'], encoding='ascii')
        for i in range(len(StimID)))
        Exp['StimISI'] = list('None' if 'SquarePulse' == Exp['TypeOfStim'][i]
        else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['DelayBetweenPulses'], encoding='ascii') 
        for i in range(len(StimID)))
   
    
    #get map names
    mapNamesInSeq = {}
    for k, v in data['header']['StimulusLibrary']['Maps'].items():
        mapNamesInSeq[k] = str(v['Name'],'ASCII')
    
    
    del data['header']  # delete header
    
    
    ## if sequence
    if 'Sequence' in Exp['Class']:
        
        #make total sweep list
        numMapsinSeq = len(dataDict[sessionName]['MapsInSeq'].keys())
        sweep_list = list(data.keys())
        sweepDict = {}
        for i in range(numMapsinSeq):
            sweepDict['element'+str(i+1)] = sweep_list[i::numMapsinSeq]

        #assign map names to each group
        mapNamesUsedInSeq = {}
        for k, v in MapsUsedInSeq.items():
            mapNamesUsedInSeq[k] = mapNamesInSeq['element'+str(int(v))]
        
        #pair sweep numbers with map names
        sweepsInMap = {}
        for k, v in mapNamesUsedInSeq.items():
            sweepsInMap[v] = sweepDict[k]
        
        #make data array for each map with all sweeps, excluding bad ones
        mapData = {}        
        for k, v in sweepsInMap.items():
            dataArray = np.empty((Exp['SampleRateAcq'],0), dtype=np.float32)
            for i in v:
                if i in badList: continue
                dataVals = np.transpose(data[i]['analogScans'])
                dataArray = np.append(dataArray,dataVals,1)
            mapData[k+'_data'] = dataArray
        
        

        #makes an average to save figures that isnt baselined
        mapDataforFig = mapData.copy()
        mapDataMeanFig = {}  
        for k, v in mapDataforFig.items():
            mapDataMeanFig[k] = np.mean(v,1) 
            
        #plot and save figures into imageloc
        from matplotlib import pyplot as plt
        from pathlib import Path
        imagepath = Path(imageloc) 
        if fig == 1:
            for k, v in mapDataMeanFig.items():
                plt.figure()
                plt.plot(mapDataMeanFig[k])
                plt.ylim((plotMin,plotMax))
                plt.yticks(np.arange(plotMin+1, plotMax-1, 2))
                plt.xlim((plotStart,plotStop))
    
                imagename = str(date)+'_'+str(genotype)+'_'+str(mouseID)+'_cell'+str(cellID)+'_'+str(delay)+'ms_'+k.strip('_data')
                
                plt.savefig(imagepath / (imagename + '.png'))  # may not work
                plt.savefig(imagepath / (imagename + '.eps'), format='eps', dpi=1200)
                plt.close()
        
        
        #baseline data array if told to
        BLmapData = {}
        if BLstart == None or BLstop == None:
                BLmapData = mapData     
        else:
            for k, v in mapData.items():
                baseline = np.mean(v[BLstart:BLstop],0) 
                BLmapData[k] = v - baseline
                
        #average
        mapDataMean = {}  
        for k, v in BLmapData.items():
            mapDataMean[k] = np.mean(v,1)  
            
        #save each average as its own file, add to Exp
        import tkinter
        from tkinter.filedialog import asksaveasfilename
        tkinter.Tk().withdraw()
        import pickle
        
        for k, v in mapDataMean.items():
            Exp[k] = v
            name = str(date)+'_'+str(genotype)+'_'+str(mouseID)+'_cell'+str(cellID)+'_'+str(delay)+'ms_'+k.strip('_data')
            saveAsFilename = asksaveasfilename(initialdir = saveloc, initialfile = name)  # specify save folder and name,add .pkl if pickling
            pickle.dump(Exp, open(saveAsFilename, 'wb')) 
            # save whole dictionary as pkl file
            del Exp[k]
    
    
    
    ## if map
    if 'Map' in Exp['Class']:
        
        dataArray = np.empty((Exp['SampleRateAcq'],0), dtype=np.float32)
            
        for k, v in data.items():
            if k in badList: continue
            dataVals = np.transpose(v["analogScans"])
            dataArray = np.append(dataArray, dataVals, 1) 
    
        
        #makes an average to save figures that isnt baselined
        mapDataMeanFig = np.mean(dataArray.copy(),axis=1)
        
        #plot and save figures into imageloc
        from matplotlib import pyplot as plt
        from pathlib import Path
        imagepath = Path(imageloc) 
        if fig == 1:
            plt.figure()
            plt.plot(mapDataMeanFig)
            plt.ylim((plotMin,plotMax))
            plt.yticks(np.arange(plotMin+1, plotMax-1, 2))
            plt.xlim((plotStart,plotStop))

            imagename = str(date)+'_'+str(genotype)+'_'+str(mouseID)+'_cell'+str(cellID)+'_'+str(delay)+'ms_'+str(color)
            
            plt.savefig(imagepath / (imagename + '.png'))  # may not work
            plt.savefig(imagepath / (imagename + '.eps'), format='eps', dpi=1200)
            plt.close()
            
                
        # get baseline (if defined) then average
        if BLstart == None or BLstop == None:
            BLdataArray = dataArray
        else:
            baseline = np.mean(dataArray[BLstart:BLstop],0) 
            BLdataArray = dataArray - baseline
            
        dataMean = np.mean(BLdataArray,1)
        Exp[str(equivalentName)+'_data'] = dataMean    
        
        # save average into a wavedump
        import tkinter
        from tkinter.filedialog import asksaveasfilename
        tkinter.Tk().withdraw()
        name = str(date)+'_'+str(genotype)+'_'+str(mouseID)+'_cell'+str(cellID)+'_'+str(delay)+'ms_'+str(color)
        saveAsFilename = asksaveasfilename(initialdir = saveloc, initialfile = name)  # specify save folder and name,add .pkl if pickiling
        
        import pickle
        pickle.dump(Exp, open(saveAsFilename, 'wb')) # save whole dictionary as pkl file
        
#    np.save(saveAsFilename,dataMean)   # save as npy file
    
#    to load:
#    data = pickle.load(open('filepath', 'rb'))

#%%
        

def saveSessionAll(dataDict, sessionNum, badTraces, saveloc, date, genotype, mouseID, cellID, delay, imageloc, fig,  plotMin, plotMax, plotStart, plotStop, color, equivalentName):
    from pywavesurfer import ws
    import numpy as np
         
    # get file path    
    if len(list(dataDict.keys())[0]) > 30:
        firstSession = list(dataDict.keys())[0]
    else:
        firstSession = list(dataDict.keys())[1]
    
    # check if there ar identical sessions in the folder, if there are, pick which on to use    
    sessionBase = firstSession[0:13]
    sameSessionList = list(k for k in dataDict.keys() if (sessionBase + '%03d' % sessionNum) in k)
    if len(sameSessionList) == 1:
        sessionName = sameSessionList[0]
    else:
        sessionChoice = input('define which of the %s sessions:' %len(sameSessionList))
        sessionName = sameSessionList[int(sessionChoice)-1]
        
    filePath = dataDict[sessionName]['Origin'][0]
        
    badList = []
    for i in range(len(badTraces)):
        badList.append("sweep_%04d" % badTraces[i])
        
    data = ws.loadDataFile(filename= filePath, format_string='single' )  # load data
    
    # get header info and put in a dictionary
    Exp = {} # dict.fromkeys(['Class', 'MapName', 'TypeOfStim', 'StimName', 'StimAmp', 'StimTime', 'StimeDuration', 'StimISI'], [None]*5)
    Exp['Origin'] = [filePath]
    Exp['SampleRateAcq'] = int(np.asscalar(data['header']['AcquisitionSampleRate']))
    Exp['SampleRateStim'] = int(np.asscalar(data['header']['StimulationSampleRate']))
    Exp['sweepLength'] = int(np.asscalar(data['header']['ExpectedSweepScanCount']))
    Exp['SessionNo'] = int(np.asscalar(data['header']['SessionIndex']))
    Exp['Class'] = str(data['header']['StimulusLibrary']['SelectedOutputableClassName'], encoding = 'ascii')
    if 'Sequence' in Exp['Class']:
        StimSeqUsed = data['header']['StimulusLibrary']['SelectedOutputableIndex']
        Exp['SequenceName'] = str(data['header']['StimulusLibrary']['Sequences'][('element%d' %StimSeqUsed)]['Name'], encoding = 'ascii')
        MapsUsedInSeq = data['header']['StimulusLibrary']['Sequences'][('element%d' %StimSeqUsed)]['IndexOfEachMapInLibrary'] 
        for v in MapsUsedInSeq.values():
            StimMapUsed = v
            StimMapName = str(data['header']['StimulusLibrary']['Maps'][('element%d' %StimMapUsed)]['Name'], encoding = 'ascii')
            StimID = list(data['header']['StimulusLibrary']['Maps'][('element%d' %StimMapUsed)]['IndexOfEachStimulusInLibrary'].values())
            Exp[StimMapName] = {}
            Exp[StimMapName]['TypeOfStim'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % iStim)]['TypeString'], encoding='ascii') for idx, iStim in enumerate(StimID))
            Exp[StimMapName]['StimName'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Name'], encoding='ascii') for i in range(len(StimID)))
            Exp[StimMapName]['StimTime'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Delay'], encoding='ascii') for i in range(len(StimID)))
            Exp[StimMapName]['StimAmp'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Amplitude'], encoding='ascii')  
            if 'SquarePulse' == Exp[StimMapName]['TypeOfStim'][i] 
            else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['FirstPulseAmplitude'], encoding='ascii')
            for i in range(len(StimID)))
            Exp[StimMapName]['StimDuration'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Duration'], encoding='ascii') 
            if 'SquarePulse' == Exp[StimMapName]['TypeOfStim'][i]
            else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['FirstPulseDuration'], encoding='ascii')
            for i in range(len(StimID)))
            Exp[StimMapName]['StimISI'] = list('None' if 'SquarePulse' == Exp[StimMapName]['TypeOfStim'][i]
            else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['DelayBetweenPulses'], encoding='ascii') 
            for i in range(len(StimID)))
    elif 'Map' in Exp['Class']:
        StimMapUsed = data['header']['StimulusLibrary']['SelectedOutputableIndex']
        Exp['MapName'] = str(data['header']['StimulusLibrary']['Maps'][('element%d' %StimMapUsed)]['Name'], encoding = 'ascii')
        StimID = list(data['header']['StimulusLibrary']['Maps'][('element%d' %StimMapUsed)]['IndexOfEachStimulusInLibrary'].values())
        Exp['TypeOfStim'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % iStim)]['TypeString'], encoding='ascii') for idx, iStim in enumerate(StimID))
        Exp['StimName'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Name'], encoding='ascii') for i in range(len(StimID)))
        Exp['StimTime'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Delay'], encoding='ascii') for i in range(len(StimID)))
        Exp['StimAmp'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Amplitude'], encoding='ascii')  
        if 'SquarePulse' == Exp['TypeOfStim'][i] 
        else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['FirstPulseAmplitude'], encoding='ascii')
        for i in range(len(StimID)))
        Exp['StimDuration'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Duration'], encoding='ascii') 
        if 'SquarePulse' == Exp['TypeOfStim'][i]
        else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['FirstPulseDuration'], encoding='ascii')
        for i in range(len(StimID)))
        Exp['StimISI'] = list('None' if 'SquarePulse' == Exp['TypeOfStim'][i]
        else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['DelayBetweenPulses'], encoding='ascii') 
        for i in range(len(StimID)))
   
    
    #get map names
    mapNamesInSeq = {}
    for k, v in data['header']['StimulusLibrary']['Maps'].items():
        mapNamesInSeq[k] = str(v['Name'],'ASCII')
    
    
    del data['header']  # delete header
    
    
    ## if sequence
    if 'Sequence' in Exp['Class']:
        
        #make total sweep list
        numMapsinSeq = len(dataDict[sessionName]['MapsInSeq'].keys())
        sweep_list = list(data.keys())
        sweepDict = {}
        for i in range(numMapsinSeq):
            sweepDict['element'+str(i+1)] = sweep_list[i::numMapsinSeq]

        #assign map names to each group
        mapNamesUsedInSeq = {}
        for k, v in MapsUsedInSeq.items():
            mapNamesUsedInSeq[k] = mapNamesInSeq['element'+str(int(v))]
        
        #pair sweep numbers with map names
        sweepsInMap = {}
        for k, v in mapNamesUsedInSeq.items():
            sweepsInMap[v] = sweepDict[k]
        
        #make data array for each map with all sweeps, excluding bad ones
        mapData = {}        
        for k, v in sweepsInMap.items():
            dataArray = np.empty((Exp['SampleRateAcq'],0), dtype=np.float32)
            for i in v:
                if i in badList: continue
                dataVals = np.transpose(data[i]['analogScans'])
                dataArray = np.append(dataArray,dataVals,1)
            mapData[k+'_data'] = dataArray
        

                

            
        #save each average as its own file, add to Exp
        import tkinter
        from tkinter.filedialog import asksaveasfilename
        tkinter.Tk().withdraw()
        import pickle
        
        for k, v in mapData.items():
            Exp[k] = v
            name = str(date)+'_'+str(genotype)+'_'+str(mouseID)+'_cell'+str(cellID)+'_'+str(delay)+'ms_'+k.strip('_data')
            saveAsFilename = asksaveasfilename(initialdir = saveloc, initialfile = name)  # specify save folder and name,add .pkl if pickling
            pickle.dump(Exp, open(saveAsFilename, 'wb')) 
            # save whole dictionary as pkl file
            del Exp[k]
    
       
        
        
 #%%
def saveISteps(dataDict, sessionNum, badTraces, saveloc, date, genotype, mouseID, cellID, imageloc, fig,  plotMin, plotMax, plotStart, plotStop, Vm):
    from pywavesurfer import ws
    import numpy as np
         
    # get file path    
    if len(list(dataDict.keys())[0]) > 30:
        firstSession = list(dataDict.keys())[0]
    else:
        #firstSession = list(dataDict.keys())[1]
        #changed to below on 220525 to handle experiments where only one session - but might be bug from GL code?
        firstSession = list(dataDict.keys())[0]
        
    # check if there ar identical sessions in the folder, if there are, pick which on to use    
    # sessionBase = firstSession[0:13]
    #changed to below on 220526 to handle experiments where cell number is double digits (cell10 or more)
    instance = 0
    for counter, iChar in enumerate(firstSession):
       if iChar == '_':
           instance = instance + 1
           if instance == 2:
               sessionBase = firstSession[:counter+1]
               
    sameSessionList = list(k for k in dataDict.keys() if (sessionBase + '%03d' % sessionNum) in k)
    if len(sameSessionList) == 1:
        sessionName = sameSessionList[0]
    else:
        sessionChoice = input('define which of the %s sessions:' %len(sameSessionList))
        sessionName = sameSessionList[int(sessionChoice)-1]
        
    filePath = dataDict[sessionName]['Origin'][0]
        
    badList = []
    for i in range(len(badTraces)):
        badList.append("sweep_%04d" % badTraces[i])
        
    data = ws.loadDataFile(filename= filePath, format_string='single' )  # load data
    
    # get header info and put in a dictionary
    Exp = {} # dict.fromkeys(['Class', 'MapName', 'TypeOfStim', 'StimName', 'StimAmp', 'StimTime', 'StimeDuration', 'StimISI'], [None]*5)
    Exp['Origin'] = [filePath]
    Exp['SampleRateAcq'] = int(np.asscalar(data['header']['AcquisitionSampleRate']))
    Exp['SampleRateStim'] = int(np.asscalar(data['header']['StimulationSampleRate']))
    Exp['sweepLength'] = int(np.asscalar(data['header']['ExpectedSweepScanCount']))
    Exp['SessionNo'] = int(np.asscalar(data['header']['SessionIndex']))
    Exp['Class'] = str(data['header']['StimulusLibrary']['SelectedOutputableClassName'], encoding = 'ascii')
    if 'Sequence' in Exp['Class']:
        StimSeqUsed = data['header']['StimulusLibrary']['SelectedOutputableIndex']
        Exp['SequenceName'] = str(data['header']['StimulusLibrary']['Sequences'][('element%d' %StimSeqUsed)]['Name'], encoding = 'ascii')
        MapsUsedInSeq = data['header']['StimulusLibrary']['Sequences'][('element%d' %StimSeqUsed)]['IndexOfEachMapInLibrary'] 
        for v in MapsUsedInSeq.values():
            StimMapUsed = v
            StimMapName = str(data['header']['StimulusLibrary']['Maps'][('element%d' %StimMapUsed)]['Name'], encoding = 'ascii')
            StimID = list(data['header']['StimulusLibrary']['Maps'][('element%d' %StimMapUsed)]['IndexOfEachStimulusInLibrary'].values())
            Exp[StimMapName] = {}
            Exp[StimMapName]['TypeOfStim'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % iStim)]['TypeString'], encoding='ascii') for idx, iStim in enumerate(StimID))
            Exp[StimMapName]['StimName'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Name'], encoding='ascii') for i in range(len(StimID)))
            Exp[StimMapName]['StimTime'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Delay'], encoding='ascii') for i in range(len(StimID)))
            Exp[StimMapName]['StimAmp'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Amplitude'], encoding='ascii')  
            if 'SquarePulse' == Exp[StimMapName]['TypeOfStim'][i] 
            else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['FirstPulseAmplitude'], encoding='ascii')
            for i in range(len(StimID)))
            Exp[StimMapName]['StimDuration'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Duration'], encoding='ascii') 
            if 'SquarePulse' == Exp[StimMapName]['TypeOfStim'][i]
            else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['FirstPulseDuration'], encoding='ascii')
            for i in range(len(StimID)))
            Exp[StimMapName]['StimISI'] = list('None' if 'SquarePulse' == Exp[StimMapName]['TypeOfStim'][i]
            else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['DelayBetweenPulses'], encoding='ascii') 
            for i in range(len(StimID)))
    elif 'Map' in Exp['Class']:
        StimMapUsed = data['header']['StimulusLibrary']['SelectedOutputableIndex']
        Exp['MapName'] = str(data['header']['StimulusLibrary']['Maps'][('element%d' %StimMapUsed)]['Name'], encoding = 'ascii')
        StimID = list(data['header']['StimulusLibrary']['Maps'][('element%d' %StimMapUsed)]['IndexOfEachStimulusInLibrary'].values())
        Exp['TypeOfStim'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % iStim)]['TypeString'], encoding='ascii') for idx, iStim in enumerate(StimID))
        Exp['StimName'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Name'], encoding='ascii') for i in range(len(StimID)))
        Exp['StimTime'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Delay'], encoding='ascii') for i in range(len(StimID)))
        Exp['StimAmp'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Amplitude'], encoding='ascii')  
        if 'SquarePulse' == Exp['TypeOfStim'][i] 
        else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['FirstPulseAmplitude'], encoding='ascii')
        for i in range(len(StimID)))
        Exp['StimDuration'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Duration'], encoding='ascii') 
        if 'SquarePulse' == Exp['TypeOfStim'][i]
        else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['FirstPulseDuration'], encoding='ascii')
        for i in range(len(StimID)))
        Exp['StimISI'] = list('None' if 'SquarePulse' == Exp['TypeOfStim'][i]
        else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['DelayBetweenPulses'], encoding='ascii') 
        for i in range(len(StimID)))
   
    
    #get map names
    mapNamesInSeq = {}
    for k, v in data['header']['StimulusLibrary']['Maps'].items():
        mapNamesInSeq[k] = str(v['Name'],'ASCII')
    
    
    del data['header']  # delete header
    
    
    if 'Map' in Exp['Class']:
        
        dataArray = np.empty((Exp['sweepLength'],0), dtype=np.float32)
            
        for k, v in data.items():
            if k in badList: continue
            dataVals = np.transpose(v["analogScans"])
            dataArray = np.append(dataArray, dataVals, 1) 
    
        
        #plot and save figures into imageloc
        from matplotlib import pyplot as plt
        from pathlib import Path
        imagepath = Path(imageloc) 
        if fig == 1:
            plt.figure()
            plt.plot(dataArray)
            plt.ylim((plotMin,plotMax))
            plt.yticks(np.arange(plotMin, plotMax+1, 20))
            plt.xlim((plotStart,plotStop))

            imagename = str(date)+'_'+str(genotype)+'_'+str(mouseID)+'_cell'+str(cellID)+'_Isteps_'+Vm
            
            plt.savefig(imagepath / (imagename + '.png'))  # may not work
            plt.savefig(imagepath / (imagename + '.eps'), format='eps', dpi=1200)
            plt.close()
            
                
        Exp['Istep_data'] = dataArray    
        
        # save average into a wavedump
        import tkinter
        from tkinter.filedialog import asksaveasfilename
        tkinter.Tk().withdraw()
        name = str(date)+'_'+str(genotype)+'_'+str(mouseID)+'_cell'+str(cellID)+'_Isteps_'+Vm
        
        
        saveAsFilename = asksaveasfilename(initialdir = saveloc, initialfile = name)  # specify save folder and name,add .pkl if pickiling
        
        import pickle
        pickle.dump(Exp, open(saveAsFilename, 'wb')) # save whole dictionary as pkl file
    
    else:
        print('not a map???')   
     
     
#    np.save(saveAsFilename,dataMean)   # save as npy file
    
#    to load:
#    data = pickle.load(open('filepath', 'rb'))
 
 
     
#%%
def saveTTX(dataDict, sessionNum, badTraces, saveloc, date, genotype, mouseID, cellID, fiber1, fiber2, drug, BLstart = None, BLstop = None):
    
    
    from pywavesurfer import ws
    import numpy as np
         
    # get file path    
    if len(list(dataDict.keys())[0]) > 30:
        firstSession = list(dataDict.keys())[0]
    else:
        firstSession = list(dataDict.keys())[1]
    
    # check if there ar identical sessions in the folder, if there are, pick which on to use    
    sessionBase = firstSession[0:13]
    sameSessionList = list(k for k in dataDict.keys() if (sessionBase + '%03d' % sessionNum) in k)
    if len(sameSessionList) == 1:
        sessionName = sameSessionList[0]
    else:
        sessionChoice = input('define which of the %s sessions:' %len(sameSessionList))
        sessionName = sameSessionList[int(sessionChoice)-1]
        
    filePath = dataDict[sessionName]['Origin'][0]
        
    badList = []
    for i in range(len(badTraces)):
        badList.append("sweep_%04d" % badTraces[i])
        
    data = ws.loadDataFile(filename= filePath, format_string='single' )  # load data
    
    # get header info and put in a dictionary
    Exp = {} # dict.fromkeys(['Class', 'MapName', 'TypeOfStim', 'StimName', 'StimAmp', 'StimTime', 'StimeDuration', 'StimISI'], [None]*5)
    Exp['Origin'] = [filePath]
    Exp['SampleRateAcq'] = int(np.asscalar(data['header']['AcquisitionSampleRate']))
    Exp['SampleRateStim'] = int(np.asscalar(data['header']['StimulationSampleRate']))
    Exp['sweepLength'] = int(np.asscalar(data['header']['ExpectedSweepScanCount']))
    Exp['SessionNo'] = int(np.asscalar(data['header']['SessionIndex']))
    Exp['Class'] = str(data['header']['StimulusLibrary']['SelectedOutputableClassName'], encoding = 'ascii')

    StimMapUsed = data['header']['StimulusLibrary']['SelectedOutputableIndex']
    Exp['MapName'] = str(data['header']['StimulusLibrary']['Maps'][('element%d' %StimMapUsed)]['Name'], encoding = 'ascii')
    StimID = list(data['header']['StimulusLibrary']['Maps'][('element%d' %StimMapUsed)]['IndexOfEachStimulusInLibrary'].values())
    Exp['TypeOfStim'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % iStim)]['TypeString'], encoding='ascii') for idx, iStim in enumerate(StimID))
    Exp['StimName'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Name'], encoding='ascii') for i in range(len(StimID)))
    Exp['StimTime'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Delay'], encoding='ascii') for i in range(len(StimID)))
    Exp['StimAmp'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Amplitude'], encoding='ascii')  
    if 'SquarePulse' == Exp['TypeOfStim'][i] 
    else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['FirstPulseAmplitude'], encoding='ascii')
    for i in range(len(StimID)))
    Exp['StimDuration'] = list(str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['Duration'], encoding='ascii') 
    if 'SquarePulse' == Exp['TypeOfStim'][i]
    else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['FirstPulseDuration'], encoding='ascii')
    for i in range(len(StimID)))
    Exp['StimISI'] = list('None' if 'SquarePulse' == Exp['TypeOfStim'][i]
    else str(data['header']['StimulusLibrary']['Stimuli'][('element%d' % StimID[i])]['Delegate']['DelayBetweenPulses'], encoding='ascii') 
    for i in range(len(StimID)))
   
    

    
    
    del data['header']  # delete header
    

    dataArray = np.empty((Exp['sweepLength'],0), dtype=np.float32)
        
    for k, v in data.items():
        if k in badList: continue
        dataVals = np.transpose(v["analogScans"])
        dataArray = np.append(dataArray, dataVals, 1) 

    
            
    # get baseline (if defined) then average
    if BLstart == None or BLstop == None:
        BLdataArray = dataArray
    else:
        baseline = np.mean(dataArray[BLstart:BLstop],0) 
        BLdataArray = dataArray - baseline
        
    dataMean = np.mean(BLdataArray,1)
    
    Exp['TTX_data'] = dataMean    
    
    # save average into a wavedump
    import tkinter
    from tkinter.filedialog import asksaveasfilename
    tkinter.Tk().withdraw()
    name = str(date)+'_'+str(genotype)+'_'+str(mouseID)+'_cell'+str(cellID)+'_F1'+fiber1+'_F2'+fiber2+'_'+drug
    saveAsFilename = asksaveasfilename(initialdir = saveloc, initialfile = name)  # specify save folder and name,add .pkl if pickiling
    
    import pickle
    pickle.dump(Exp, open(saveAsFilename, 'wb')) # save whole dictionary as pkl file
    
    
    
    
    
    
    
        
 #%%
 
 
 
 