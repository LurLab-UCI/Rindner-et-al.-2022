# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 18:22:14 2020

@author: Lur Lab 3
"""

#%%
def opsinSwapList():
        
    opsinSwapList = ['200219_wt_901_cell1_IB','200219_wt_901_cell2_IB','200224_wt_924_cell2_RS','200226_wt_916_cell1_RS',
                     '200226_wt_916_cell2_IB','200226_wt_916_cell3_RS','200228_wt_921_cell1_RS','200228_wt_921_cell2_RS',
                     '200305_wt_940_cell1_RS','200305_wt_940_cell2_RS','200316_wt_949_cell3_RS','200313_wt_962_cell2_RS',
                     '200317_wt_959_cell1_RS','200317_wt_959_cell2_RS','200318_wt_961_cell1_RS','200320_wt_960_cell1_RS',
                     '200320_wt_960_cell2_RS','200324_wt_964_cell1_RS','200330_wt_970_cell1_RS','200330_wt_970_cell4_RS',
                     '200403_wt_982_cell1_RS','200406_wt_980_cell1_IB','200524_wt_1045_cell1_IB','200524_wt_1053_cell2_RS',
                     '200527_pvai_205_cell1_RS','200529_pvai_208_cell1_IB','200529_pvai_207_cell2_IB','200603_pvai_206_cell1_RS',
                     '200603_pvai_206_cell2_IB','200612_wt_1062_cell2_IB','200612_wt_1062_cell3_IB', '200616_wt_1069_cell3_IB',
                     '200703_wt_1096_cell2_IB','200703_wt_1096_cell3_IB','200703_wt_1096_cell4_IB','200707_wt_1115_cell2_IB',
                     '200707_wt_1115_cell3_RS', '200707_wt_1115_cell5_IB','200709_wt_1116_cell1_IB','200709_wt_1116_cell2_IB',
                     '200715_pv_142_cell1_IB','200729_wt_1137_cell2_IB','200729_wt_1137_cell3_IB','200806_wt_1135_cell4_IB',
                     '200806_wt_1135_cell3_IB','200807_wt_1136_cell3_IB','200807_pvai_223_cell5_RS','200908_wt_1208_cell2_RS',
                     '200908_wt_1208_cell3_IB','200909_wt_1207_cell1_IB','200909_wt_1207_cell2_IB','200915_wt_1216_cell4_IB',
                     '200915_wt_1216_cell5_RS','200916_wt_1215_cell3_RS', '200917_wt_1214_cell1_RS','201020_wt_1272_cell1_RS',
                     '201020_wt_1272_cell2_RS','201020_wt_1271_cell3_RS','201021_wt_1270_cell2_RS','201021_wt_1270_cell3_RS',
                     '201102_wt_1294_cell1_RS','201103_wt_1293_cell1_RS','201103_wt_1293_cell2_RS', '210302_wt_1457_cell1_RS',
                     '210302_wt_1457_cell2_IB','210303_wt_1460_cell1_RS','210303_wt_1460_cell2_RS','210303_wt_1460_cell3_RS',
                     '210304_wt_1459_cell2_RS','210305_wt_1458_cell1_RS','210305_wt_1458_cell2_IB',
                        
                     '200219_wt_901_cell1_RS','200219_wt_901_cell2_RS','200224_wt_924_cell2_IB','200226_wt_916_cell1_IB',
                     '200226_wt_916_cell2_RS','200226_wt_916_cell3_IB','200228_wt_921_cell1_IB','200228_wt_921_cell2_IB',
                     '200305_wt_940_cell1_IB','200305_wt_940_cell2_IB','200316_wt_949_cell3_IB','200313_wt_962_cell2_IB',
                     '200317_wt_959_cell1_IB','200317_wt_959_cell2_IB','200318_wt_961_cell1_IB','200320_wt_960_cell1_IB',
                     '200320_wt_960_cell2_IB','200324_wt_964_cell1_IB','200330_wt_970_cell1_IB','200330_wt_970_cell4_IB',
                     '200403_wt_982_cell1_IB','200406_wt_980_cell1_RS','200524_wt_1045_cell1_RS','200524_wt_1053_cell2_IB',
                     '200527_pvai_205_cell1_IB','200529_pvai_208_cell1_RS','200529_pvai_207_cell2_RS','200603_pvai_206_cell1_IB',
                     '200603_pvai_206_cell2_RS','200612_wt_1062_cell2_RS','200612_wt_1062_cell3_RS','200616_wt_1069_cell3_RS',
                     '200703_wt_1096_cell2_RS','200703_wt_1096_cell3_RS','200703_wt_1096_cell4_RS','200707_wt_1115_cell2_RS',
                     '200707_wt_1115_cell3_IB', '200707_wt_1115_cell5_RS','200709_wt_1116_cell1_RS','200709_wt_1116_cell2_RS',
                     '200715_pv_142_cell1_RS','200729_wt_1137_cell2_RS','200729_wt_1137_cell3_RS','200806_wt_1135_cell4_RS',
                     '200806_wt_1135_cell3_RS','200807_wt_1136_cell3_RS','200807_pvai_223_cell5_IB','200908_wt_1208_cell2_IB',
                     '200908_wt_1208_cell3_RS','200909_wt_1207_cell1_RS','200909_wt_1207_cell2_RS','200915_wt_1216_cell4_RS',
                     '200915_wt_1216_cell5_IB','200916_wt_1215_cell3_IB', '200917_wt_1214_cell1_IB','201020_wt_1272_cell1_IB',
                     '201020_wt_1272_cell2_IB','201020_wt_1271_cell3_IB','201021_wt_1270_cell2_IB','201021_wt_1270_cell3_IB',
                     '201102_wt_1294_cell1_IB','201103_wt_1293_cell1_IB','201103_wt_1293_cell2_IB','210302_wt_1457_cell1_IB',
                     '210302_wt_1457_cell2_RS','210303_wt_1460_cell1_IB','210303_wt_1460_cell2_IB','210303_wt_1460_cell3_IB',
                     '210304_wt_1459_cell2_IB', '210305_wt_1458_cell1_IB','210305_wt_1458_cell2_RS']
    
    oneMapCells = ['190702_pvai_46_cell1_IB','190708_wt_562_cell1_RS','190708_wt_562_cell2_IB','190708_wt_562_cell3_IB','190719_ai_67_cell1_RS',
                   '190722_pvai_50_cell1_RS','190722_pvai_50_cell2_RS','190722_pvai_50_cell3_IB','190724_ai_66_cell1_IB',
                   '190725_wt_572_cell1_IB','190725_wt_572_cell2_IB','190731_pvai_58_cell1_RS','190731_pvai_58_cell2_IB',
                   '190731_pvai_58_cell3_IB','190731_pvai_58_cell4_RS','190801_wt_569_cell1_RS','190801_wt_569_cell2_IB','190926_wt_650_cell1_RS',
                   '190702_pvai_46_cell1_RS','190708_wt_562_cell1_IB','190708_wt_562_cell2_RS','190708_wt_562_cell3_RS','190719_ai_67_cell1_IB',
                   '190722_pvai_50_cell1_IB','190722_pvai_50_cell2_IB','190722_pvai_50_cell3_RS','190724_ai_66_cell1_RS',
                   '190725_wt_572_cell1_RS','190725_wt_572_cell2_RS','190731_pvai_58_cell1_IB','190731_pvai_58_cell2_RS',
                   '190731_pvai_58_cell3_RS','190731_pvai_58_cell4_IB','190801_wt_569_cell1_IB','190801_wt_569_cell2_RS','190926_wt_650_cell1_IB']
    
    return opsinSwapList, oneMapCells

#%% do the analysis, subtraction and peak data - change for every experiment as necessary!!!

def mousemixedPulseAnalysis(fiberTypes, cellType, delay1, delay2, delay3, delay4, opsinSwapList, imageloc, show, oneMapCells):

    import tkinter
    from tkinter.filedialog import askopenfilename
    import pickle

    delayList = [delay1,delay2,delay3,delay4]
    
    from pathlib import Path

    if 'A1' in fiberTypes and 'V1' in fiberTypes:
        savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration A1_V1")
    if 'A1' in fiberTypes and 'ACC' in fiberTypes:
        savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration A1_ACC")
    if 'V1' in fiberTypes and 'ACC' in fiberTypes:
        savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration V1_ACC")
         
           
    # make a list with all folder names including cellType:
    import os
    allnames = os.listdir(savedLoc)
    selectednames = [x for x in allnames if cellType in x]
    
    
    import pandas as pd
    import numpy as np
    frontalsensoryData = pd.DataFrame()
    sensoryfrontalData = pd.DataFrame()
    coincidentData = pd.DataFrame()
    
    peakData = pd.DataFrame({'cell ID':[*selectednames]}).set_index('cell ID')
    
    peakData['0ms_frontal single']=""
    peakData['0ms_frontal paired']=""
    peakData['0ms_sensory single']=""
    peakData['0ms_sensory paired']=""
    peakData['50ms_frontal single']=""
    peakData['50ms_frontal paired']=""
    peakData['50ms_sensory single']=""
    peakData['50ms_sensory paired']=""
    peakData['100ms_frontal single']=""
    peakData['100ms_frontal paired']=""
    peakData['100ms_sensory single']=""
    peakData['100ms_sensory paired']=""
    peakData['250ms_frontal single']=""
    peakData['250ms_frontal paired']=""
    peakData['250ms_sensory single']=""
    peakData['250ms_sensory paired']=""
    
    
    
    for i in selectednames:
        print('processing...'+str(i)) 
        # point at data file to view
        cellPath = savedLoc / i
        workspacedf = pd.DataFrame()
        
        if i in oneMapCells:
            
          for file in os.listdir(cellPath):      
                for delay in delayList:
                    if '_'+str(delay)+'ms_blue' in file and 'bluered' not in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                workspacedf[str(delay)+'_'+'pulse 1 map_data'] = loadedData[k] 
                                
                    if '_'+str(delay)+'ms_bluered' in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                workspacedf[str(delay)+'_'+'paired pulse map_data'] = loadedData[k] 
                                
                    if '_'+str(delay)+'ms_red' in file and 'redblue' not in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                workspacedf[str(delay)+'_'+'pulse 2 map_data'] = loadedData[k]          
                                
                    if '_'+str(delay)+'ms_redblue' in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                workspacedf[str(delay)+'_'+'paired pulse map_swap_data'] = loadedData[k] 
                                
        else:
            
            for file in os.listdir(cellPath):      
                for delay in delayList:
                    if '_'+str(delay)+'ms' in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                workspacedf[str(delay)+'_'+str(k)] = loadedData[k]
                               
    
                        
        # this is where we MANUALLY change which pulse stimulates which fiber pop!!!
        
        for delay in delayList:        
            if delay == 0:
                if i in opsinSwapList:
                    
                    coincidentData['actualCoincident'] = workspacedf[str(delay)+'_'+'paired pulse map_data']
                    coincidentData['arithmeticSum'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf[str(delay)+'_'+'pulse 1 map_data']
                
                if i not in opsinSwapList: # same as above if in opsinSwapList
                    
                   coincidentData['actualCoincident'] = workspacedf[str(delay)+'_'+'paired pulse map_data']
                   coincidentData['arithmeticSum'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf[str(delay)+'_'+'pulse 1 map_data']
                    
                   
                #for both
                maxLocActual = np.argmax(coincidentData['actualCoincident'][1000:1300],axis = 0)
                maxValActual = []
                actualBL = np.mean(coincidentData['actualCoincident'][990:999],axis = 0)
                maxValActual = np.mean(coincidentData['actualCoincident'][maxLocActual-3 : maxLocActual+3], 0) - actualBL       
                
                maxLocSum = np.argmax(coincidentData['arithmeticSum'][1000:1300],axis = 0)
                maxValSum = []
                sumBL = np.mean(coincidentData['arithmeticSum'][990:999],axis = 0)
                maxValSum = np.mean(coincidentData['arithmeticSum'][maxLocSum-3 : maxLocSum+3], 0) - sumBL
              
                
                
                peakData.at[str(i),str(delay)+'ms_sensory single'] = maxValSum #now has to equal arithmetic addition of traces peak
                peakData.at[str(i),str(delay)+'ms_sensory paired'] = maxValActual #now has to equal coincident
                peakData.at[str(i),str(delay)+'ms_frontal single'] = maxValSum # same as above
                peakData.at[str(i),str(delay)+'ms_frontal paired'] = maxValActual # same as above
                
                
            else:   
                try:
                    if i in opsinSwapList:
                   
                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_swap_data']                        
                        workspacedf['zeros'] = np.zeros(len(workspacedf))
                        workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 1 map_data'][1000:2000]
                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf['zeros']

                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_data']                        
                        workspacedf['zeros'] = np.zeros(len(workspacedf))
                        workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 2 map_data'][1000:2000]
                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 1 map_data'] + workspacedf['zeros']


                    if i not in opsinSwapList:
                        
                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_data']                        
                        workspacedf['zeros'] = np.zeros(len(workspacedf))
                        workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 2 map_data'][1000:2000]
                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 1 map_data'] + workspacedf['zeros']

                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_swap_data']                        
                        workspacedf['zeros'] = np.zeros(len(workspacedf))
                        workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 1 map_data'][1000:2000]
                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf['zeros']
                        
                        
                        
                    #for all
                        
                    maxLocSensoryActual = np.argmax(frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'][1000+(delay*10):1300+(delay*10)],axis = 0)
                    maxValSensoryActual = []
                    sensoryActualPeak = abs(np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'][maxLocSensoryActual-3 : maxLocSensoryActual+3], 0))        
                    sensoryActualBL = abs(np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'][990+(delay*10):999+(delay*10)], 0))
                    peakValSensoryActual = sensoryActualPeak - sensoryActualBL    
                        
                    maxLocSensoryArithmetic = np.argmax(frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'][1000+(delay*10):1300+(delay*10)],axis = 0)
                    maxValSensoryArithmetic = []
                    sensoryArithmeticPeak = abs(np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'][maxLocSensoryArithmetic-3 : maxLocSensoryArithmetic+3], 0))        
                    sensoryArithmeticBL = abs(np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'][990+(delay*10):999+(delay*10)], 0))
                    peakValSensoryArithmetic = sensoryArithmeticPeak - sensoryArithmeticBL                         

                    maxLocFrontalActual = np.argmax(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'][1000+(delay*10):1300+(delay*10)],axis = 0)
                    maxValFrontalActual = []
                    frontalActualPeak = abs(np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'][maxLocFrontalActual-3 : maxLocFrontalActual+3], 0))        
                    frontalActualBL = abs(np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'][990+(delay*10):999+(delay*10)], 0))
                    peakValFrontalActual = frontalActualPeak - frontalActualBL    
                        
                    maxLocFrontalArithmetic = np.argmax(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'][1000+(delay*10):1300+(delay*10)],axis = 0)
                    maxValFrontalArithmetic = []
                    frontalArithmeticPeak = abs(np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'][maxLocFrontalArithmetic-3 : maxLocFrontalArithmetic+3], 0))        
                    frontalArithmeticBL = abs(np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'][990+(delay*10):999+(delay*10)], 0))
                    peakValFrontalArithmetic = frontalArithmeticPeak - frontalArithmeticBL                         
                    
                    
                
                    
                    #get peak amplitudes
                    peakData.at[str(i),str(delay)+'ms_sensory single'] = peakValSensoryArithmetic
                    peakData.at[str(i),str(delay)+'ms_sensory paired'] = peakValSensoryActual
                    peakData.at[str(i),str(delay)+'ms_frontal single'] = peakValFrontalArithmetic
                    peakData.at[str(i),str(delay)+'ms_frontal paired'] = peakValFrontalActual
                    
                
                except:
                    print('missing delay points detected in '+str(i))
                    frontalsensoryData['delay '+str(delay)+'ms_sensory paired pulse'] = np.nan
                    frontalsensoryData['delay '+str(delay)+'ms_sensory single pulse'] = np.nan
                    
                    sensoryfrontalData['delay '+str(delay)+'ms_frontal paired pulse'] = np.nan
                    sensoryfrontalData['delay '+str(delay)+'ms_frontal single pulse'] = np.nan
    
       
                    peakData.at[str(i),str(delay)+'ms_sensory single'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_sensory paired'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_frontal single'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_frontal paired'] = np.nan
   
    #get ratios
        
    pairedpeakRatio = pd.DataFrame(index=peakData.index)
    
    pairedpeakRatio['0ms_frontal']=""
    pairedpeakRatio['0ms_sensory']=""
    pairedpeakRatio['50ms_frontal']=""
    pairedpeakRatio['50ms_sensory']=""
    pairedpeakRatio['100ms_frontal']=""
    pairedpeakRatio['100ms_sensory']=""
    pairedpeakRatio['250ms_frontal']=""
    pairedpeakRatio['250ms_sensory']=""
    
    for iIndex in selectednames:
        pairedpeakRatio.at[str(iIndex),'0ms_frontal']= peakData.at[str(iIndex),'0ms_frontal paired'] / peakData.at[str(iIndex),'0ms_frontal single']
        pairedpeakRatio.at[str(iIndex),'0ms_sensory']= peakData.at[str(iIndex),'0ms_sensory paired'] / peakData.at[str(iIndex),'0ms_sensory single']
        pairedpeakRatio.at[str(iIndex),'50ms_frontal']= peakData.at[str(iIndex),'50ms_frontal paired'] / peakData.at[str(iIndex),'50ms_frontal single']
        pairedpeakRatio.at[str(iIndex),'50ms_sensory']= peakData.at[str(iIndex),'50ms_sensory paired'] / peakData.at[str(iIndex),'50ms_sensory single']
        pairedpeakRatio.at[str(iIndex),'100ms_frontal']= peakData.at[str(iIndex),'100ms_frontal paired'] / peakData.at[str(iIndex),'100ms_frontal single']
        pairedpeakRatio.at[str(iIndex),'100ms_sensory']= peakData.at[str(iIndex),'100ms_sensory paired'] / peakData.at[str(iIndex),'100ms_sensory single']
        pairedpeakRatio.at[str(iIndex),'250ms_frontal']= peakData.at[str(iIndex),'250ms_frontal paired'] / peakData.at[str(iIndex),'250ms_frontal single']
        pairedpeakRatio.at[str(iIndex),'250ms_sensory']= peakData.at[str(iIndex),'250ms_sensory paired'] / peakData.at[str(iIndex),'250ms_sensory single']
    
    
    
    #make figure from paired peak ratios
    if show == 0:     
        import matplotlib.pyplot as plt
        plt.figure()
        for cell in selectednames:
            names = [str(0),str(50),str(100),str(250)]
            values = [pairedpeakRatio.at[cell,'0ms_frontal'],pairedpeakRatio.at[cell,'50ms_frontal'],pairedpeakRatio.at[cell,'100ms_frontal'],pairedpeakRatio.at[cell,'250ms_frontal']]
            linevalues = [1,1,1,1]
            plt.ylim((0.3,2.5))
            if len(values) - sum(np.isnan(values)) > 1:
                plt.plot(names,values,label=cell)
            elif len(values) - sum(np.isnan(values)) == 1:
                plt.plot(names,values,label=cell, marker = 'o')
            plt.legend(loc='center left', bbox_to_anchor=(1.04,0.5))
            plt.title(fiberTypes[0]+'_'+fiberTypes[1]+' sensory-frontal')   
            plt.plot(names,linevalues,'k--')
            plt.tight_layout()
            plt.show()
            
            
        plt.figure()
        for cell in selectednames:
            names = [str(0),str(50),str(100),str(250)]
            values = [pairedpeakRatio.at[cell,'0ms_sensory'],pairedpeakRatio.at[cell,'50ms_sensory'],pairedpeakRatio.at[cell,'100ms_sensory'],pairedpeakRatio.at[cell,'250ms_sensory']]
            linevalues = [1,1,1,1]
            plt.ylim((0.3,2.5))
            if len(values) - sum(np.isnan(values)) > 1:
                plt.plot(names,values,label=cell)
            elif len(values) - sum(np.isnan(values)) == 1:
                plt.plot(names,values,label=cell, marker = 'o')
            plt.legend(loc='center left', bbox_to_anchor=(1.04,0.5))    
            plt.title(fiberTypes[0]+'_'+fiberTypes[1]+' frontal-sensory') 
            plt.plot(names,linevalues,'k--')
            plt.tight_layout()
            plt.show()
            
    if show == 1:      
        import matplotlib.pyplot as plt
        plt.figure()
        for cell in selectednames:
            names = [str(0),str(50),str(100),str(250)]
            values = [pairedpeakRatio.at[cell,'0ms_frontal'],pairedpeakRatio.at[cell,'50ms_frontal'],pairedpeakRatio.at[cell,'100ms_frontal'],pairedpeakRatio.at[cell,'250ms_frontal']]
            linevalues = [1,1,1,1]
            if len(values) - sum(np.isnan(values)) > 1:
                plt.plot(names,values,label=cell)
            elif len(values) - sum(np.isnan(values)) == 1:
                plt.plot(names,values,label=cell, marker = '.')
            plt.legend(loc='center left', bbox_to_anchor=(1.04,0.5))
            plt.title(fiberTypes[0]+'_'+fiberTypes[1]+' sensory-frontal')   
            plt.plot(names,linevalues,'k--')
            plt.show()
            plt.ylim((0.3,2.5))
            imagename = str(cell)+'_frontal'
            imagepath = Path(imageloc)
            
            plt.savefig(imagepath / (imagename + '.png'), bbox_inches = "tight")
            plt.close()
            
            
        plt.figure()
        for cell in selectednames:
            names = [str(0),str(50),str(100),str(250)]
            values = [pairedpeakRatio.at[cell,'0ms_sensory'],pairedpeakRatio.at[cell,'50ms_sensory'],pairedpeakRatio.at[cell,'100ms_sensory'],pairedpeakRatio.at[cell,'250ms_sensory']]
            linevalues = [1,1,1,1]
            if len(values) - sum(np.isnan(values)) > 1:
                plt.plot(names,values,label=cell)
            elif len(values) - sum(np.isnan(values)) == 1:
                plt.plot(names,values,label=cell, marker = '.')
            plt.legend(loc='center left', bbox_to_anchor=(1.04,0.5))    
            plt.title(fiberTypes[0]+'_'+fiberTypes[1]+' frontal-sensory') 
            plt.plot(names,linevalues,'k--')
            plt.show()
            plt.ylim((0.3,2.5))
            imagename = str(cell)+'_sensory'
            imagepath = Path(imageloc)
            
            plt.savefig(imagepath / (imagename + '.png'), bbox_inches = "tight")
            plt.close()
    
    
    return pairedpeakRatio
   


#%% do the analysis, subtraction and peak data - change for every experiment as necessary!!!

def plotmouseCI(fiberTypes, cellType, delay1, delay2, delay3, delay4, opsinSwapList, confidence, oneMapCells, quality, show, imageloc, complete, average, plots):

    import tkinter
    from tkinter.filedialog import askopenfilename
    import pickle

    delayList = [delay1,delay2,delay3,delay4]
    
    from pathlib import Path
    if quality == 'EPSP':
        if 'A1' in fiberTypes and 'V1' in fiberTypes:
            savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration A1_V1")
        if 'A1' in fiberTypes and 'ACC' in fiberTypes:
            savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration A1_ACC")
        if 'V1' in fiberTypes and 'ACC' in fiberTypes:
            savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration V1_ACC")
            

    if quality == 'IPSC':
        savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\IPSC")
    
    
    # make a list with all folder names including cellType:
    import os
    allnames = os.listdir(savedLoc)
    selectednames = [x for x in allnames if cellType in x]
    
    
    import pandas as pd
    import numpy as np
    frontalsensoryData = pd.DataFrame()
    sensoryfrontalData = pd.DataFrame()
    coincidentData = pd.DataFrame()
    
    peakData = pd.DataFrame({'cell ID':[*selectednames]}).set_index('cell ID')
    
    peakData['0ms_frontal single']=""
    peakData['0ms_frontal paired']=""
    peakData['0ms_sensory single']=""
    peakData['0ms_sensory paired']=""
    peakData['50ms_frontal single']=""
    peakData['50ms_frontal paired']=""
    peakData['50ms_sensory single']=""
    peakData['50ms_sensory paired']=""
    peakData['100ms_frontal single']=""
    peakData['100ms_frontal paired']=""
    peakData['100ms_sensory single']=""
    peakData['100ms_sensory paired']=""
    peakData['250ms_frontal single']=""
    peakData['250ms_frontal paired']=""
    peakData['250ms_sensory single']=""
    peakData['250ms_sensory paired']=""
    
    
    
    for i in selectednames:
        print('processing...'+str(i)) 
        # point at data file to view
        cellPath = savedLoc / i
        workspacedf = pd.DataFrame()
        
        if i in oneMapCells:
            
          for file in os.listdir(cellPath):      
                for delay in delayList:
                    if '_'+str(delay)+'ms_blue' in file and 'bluered' not in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                workspacedf[str(delay)+'_'+'pulse 1 map_data'] = loadedData[k] 
                                
                    if '_'+str(delay)+'ms_bluered' in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                workspacedf[str(delay)+'_'+'paired pulse map_data'] = loadedData[k] 
                                
                    if '_'+str(delay)+'ms_red' in file and 'redblue' not in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                workspacedf[str(delay)+'_'+'pulse 2 map_data'] = loadedData[k]          
                                
                    if '_'+str(delay)+'ms_redblue' in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                workspacedf[str(delay)+'_'+'paired pulse map_swap_data'] = loadedData[k] 
                                
        else:
            
            for file in os.listdir(cellPath):      
                for delay in delayList:
                    if '_'+str(delay)+'ms' in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                workspacedf[str(delay)+'_'+str(k)] = loadedData[k]
                               
    
                        
        # this is where we MANUALLY change which pulse stimulates which fiber pop!!!
        
        for delay in delayList:        
            if delay == 0:
                try:
                    if i in opsinSwapList:
                        
                        coincidentData['actualCoincident'] = workspacedf[str(delay)+'_'+'paired pulse map_data']
                        coincidentData['arithmeticSum'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf[str(delay)+'_'+'pulse 1 map_data']
                    
                    if i not in opsinSwapList: # same as above if in opsinSwapList
                        
                       coincidentData['actualCoincident'] = workspacedf[str(delay)+'_'+'paired pulse map_data']
                       coincidentData['arithmeticSum'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf[str(delay)+'_'+'pulse 1 map_data']
                        
                       
                    #for both
                    maxLocActual = np.argmax(coincidentData['actualCoincident'][1000:1300],axis = 0) + 1000
                    maxValActual = []
                    actualBL = np.mean(coincidentData['actualCoincident'][990:999],axis = 0)
                    maxValActual = np.mean(coincidentData['actualCoincident'][maxLocActual-3 : maxLocActual+3], 0) - actualBL       
                    
                    maxLocSum = np.argmax(coincidentData['arithmeticSum'][1000:1300],axis = 0) + 1000
                    maxValSum = []
                    sumBL = np.mean(coincidentData['arithmeticSum'][990:999],axis = 0)
                    maxValSum = np.mean(coincidentData['arithmeticSum'][maxLocSum-3 : maxLocSum+3], 0) - sumBL
                   
                    
                    
                    peakData.at[str(i),str(delay)+'ms_sensory single'] = maxValSum #now has to equal arithmetic addition of traces peak
                    peakData.at[str(i),str(delay)+'ms_sensory paired'] = maxValActual #now has to equal coincident
                    peakData.at[str(i),str(delay)+'ms_frontal single'] = maxValSum # same as above
                    peakData.at[str(i),str(delay)+'ms_frontal paired'] = maxValActual # same as above
                    
                except:
                    print('missing delay points detected in '+str(i))
                    frontalsensoryData['delay '+str(delay)+'ms_sensory paired pulse'] = np.nan
                    frontalsensoryData['delay '+str(delay)+'ms_sensory single pulse'] = np.nan
                    
                    sensoryfrontalData['delay '+str(delay)+'ms_frontal paired pulse'] = np.nan
                    sensoryfrontalData['delay '+str(delay)+'ms_frontal single pulse'] = np.nan
    
       
                    peakData.at[str(i),str(delay)+'ms_sensory single'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_sensory paired'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_frontal single'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_frontal paired'] = np.nan
                    
            else:   
                try:
                    if i in opsinSwapList:
                   
                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_swap_data']                        
                        workspacedf['zeros'] = np.zeros(len(workspacedf))
                        workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 1 map_data'][1000:2000]
                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf['zeros']

                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_data']                        
                        workspacedf['zeros'] = np.zeros(len(workspacedf))
                        workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 2 map_data'][1000:2000]
                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 1 map_data'] + workspacedf['zeros']


                    if i not in opsinSwapList:
                        
                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_data']                        
                        workspacedf['zeros'] = np.zeros(len(workspacedf))
                        workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 2 map_data'][1000:2000]
                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 1 map_data'] + workspacedf['zeros']

                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_swap_data']                        
                        workspacedf['zeros'] = np.zeros(len(workspacedf))
                        workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 1 map_data'][1000:2000]
                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf['zeros']
                        
                        
                        
                    #for all
                        
                    maxLocSensoryActual = np.argmax(frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'][1000+(delay*10):1300+(delay*10)],axis = 0) + 1000 +(delay*10)
                    maxValSensoryActual = []
                    sensoryActualPeak = abs(np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'][maxLocSensoryActual-3 : maxLocSensoryActual+3], 0))        
                    sensoryActualBL = abs(np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'][990+(delay*10):999+(delay*10)], 0))
                    peakValSensoryActual = sensoryActualPeak - sensoryActualBL    
                        
                    maxLocSensoryArithmetic = np.argmax(frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'][1000+(delay*10):1300+(delay*10)],axis = 0) + 1000 +(delay*10)
                    maxValSensoryArithmetic = []
                    sensoryArithmeticPeak = abs(np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'][maxLocSensoryArithmetic-3 : maxLocSensoryArithmetic+3], 0))        
                    sensoryArithmeticBL = abs(np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'][990+(delay*10):999+(delay*10)], 0))
                    peakValSensoryArithmetic = sensoryArithmeticPeak - sensoryArithmeticBL                         

                    maxLocFrontalActual = np.argmax(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'][1000+(delay*10):1300+(delay*10)],axis = 0) + 1000 +(delay*10)
                    maxValFrontalActual = []
                    frontalActualPeak = abs(np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'][maxLocFrontalActual-3 : maxLocFrontalActual+3], 0))        
                    frontalActualBL = abs(np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'][990+(delay*10):999+(delay*10)], 0))
                    peakValFrontalActual = frontalActualPeak - frontalActualBL    
                        
                    maxLocFrontalArithmetic = np.argmax(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'][1000+(delay*10):1300+(delay*10)],axis = 0) + 1000 +(delay*10)
                    maxValFrontalArithmetic = []
                    frontalArithmeticPeak = abs(np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'][maxLocFrontalArithmetic-3 : maxLocFrontalArithmetic+3], 0))        
                    frontalArithmeticBL = abs(np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'][990+(delay*10):999+(delay*10)], 0))
                    peakValFrontalArithmetic = frontalArithmeticPeak - frontalArithmeticBL                         
                    
                    
                
                    
                    #get peak amplitudes
                    peakData.at[str(i),str(delay)+'ms_sensory single'] = peakValSensoryArithmetic
                    peakData.at[str(i),str(delay)+'ms_sensory paired'] = peakValSensoryActual
                    peakData.at[str(i),str(delay)+'ms_frontal single'] = peakValFrontalArithmetic
                    peakData.at[str(i),str(delay)+'ms_frontal paired'] = peakValFrontalActual
                    
                
                except:
                    print('missing delay points detected in '+str(i))
                    frontalsensoryData['delay '+str(delay)+'ms_sensory paired pulse'] = np.nan
                    frontalsensoryData['delay '+str(delay)+'ms_sensory single pulse'] = np.nan
                    
                    sensoryfrontalData['delay '+str(delay)+'ms_frontal paired pulse'] = np.nan
                    sensoryfrontalData['delay '+str(delay)+'ms_frontal single pulse'] = np.nan
    
       
                    peakData.at[str(i),str(delay)+'ms_sensory single'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_sensory paired'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_frontal single'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_frontal paired'] = np.nan
   
    #get ratios
        
    pairedpeakRatio = pd.DataFrame(index=peakData.index)
    
    pairedpeakRatio['0ms_frontal']=""
    pairedpeakRatio['0ms_sensory']=""
    pairedpeakRatio['50ms_frontal']=""
    pairedpeakRatio['50ms_sensory']=""
    pairedpeakRatio['100ms_frontal']=""
    pairedpeakRatio['100ms_sensory']=""
    pairedpeakRatio['250ms_frontal']=""
    pairedpeakRatio['250ms_sensory']=""
    
    for iIndex in selectednames:
        pairedpeakRatio.at[str(iIndex),'0ms_frontal']= peakData.at[str(iIndex),'0ms_frontal paired'] / peakData.at[str(iIndex),'0ms_frontal single']
        pairedpeakRatio.at[str(iIndex),'0ms_sensory']= peakData.at[str(iIndex),'0ms_sensory paired'] / peakData.at[str(iIndex),'0ms_sensory single']
        pairedpeakRatio.at[str(iIndex),'50ms_frontal']= peakData.at[str(iIndex),'50ms_frontal paired'] / peakData.at[str(iIndex),'50ms_frontal single']
        pairedpeakRatio.at[str(iIndex),'50ms_sensory']= peakData.at[str(iIndex),'50ms_sensory paired'] / peakData.at[str(iIndex),'50ms_sensory single']
        pairedpeakRatio.at[str(iIndex),'100ms_frontal']= peakData.at[str(iIndex),'100ms_frontal paired'] / peakData.at[str(iIndex),'100ms_frontal single']
        pairedpeakRatio.at[str(iIndex),'100ms_sensory']= peakData.at[str(iIndex),'100ms_sensory paired'] / peakData.at[str(iIndex),'100ms_sensory single']
        pairedpeakRatio.at[str(iIndex),'250ms_frontal']= peakData.at[str(iIndex),'250ms_frontal paired'] / peakData.at[str(iIndex),'250ms_frontal single']
        pairedpeakRatio.at[str(iIndex),'250ms_sensory']= peakData.at[str(iIndex),'250ms_sensory paired'] / peakData.at[str(iIndex),'250ms_sensory single']
    
    
    
    #mouse averaging
    if average == 'mouse':
        pairedpeakRatio.index = pairedpeakRatio.index.map(lambda x: str(x)[:-9])
        workspaceMousedf = pairedpeakRatio.copy()
        workspaceMousedf = workspaceMousedf.astype(float)
        strippedID = []
        for i in selectednames:
            strippedID.append(i[0:-9])
        workspaceMousedf['stripped Names']=strippedID
        grp_mouse = workspaceMousedf.groupby(['stripped Names'])
        pairedpeakMouseRatio = grp_mouse.mean()
        
        opsinSwapMice = list(map(lambda x: str(x)[:-9],opsinSwapList))
        opsinSwapRatios = pairedpeakMouseRatio[pairedpeakMouseRatio.index.isin(opsinSwapMice) == True]
        nonSwapRatios = pairedpeakMouseRatio[pairedpeakMouseRatio.index.isin(opsinSwapMice) == False]
        
    elif average == 'cell':
        pairedpeakMouseRatio = pairedpeakRatio.copy().astype(float)
        opsinSwapRatios = pairedpeakMouseRatio[pairedpeakMouseRatio.index.isin(opsinSwapList) == True]
        nonSwapRatios = pairedpeakMouseRatio[pairedpeakMouseRatio.index.isin(opsinSwapList) == False]
    
    
    
    if 'A1' in fiberTypes and 'V1' in fiberTypes:
        nonSwapRatios = pairedpeakMouseRatio.copy()
    
    
    if complete == 1:
        nonSwapRatios = nonSwapRatios.dropna()
        opsinSwapRatios = opsinSwapRatios.dropna()
  
    
    import numpy as np      
    import scipy.stats
    
    if plots == 'yes':
        nameList = ['opsin swap','default']
        for name, iRatios in enumerate([opsinSwapRatios, nonSwapRatios]):     
            
            if len(iRatios) == 0:
                continue
            
            opsinConfig = nameList[name]
            
            
            #get CI stats
            CIstats = pd.DataFrame(index=['95% CI','mean','upper bound','lower bound'])
            
            CIstats['0ms_frontal']=""
            CIstats['0ms_sensory']=""
            CIstats['50ms_frontal']=""
            CIstats['50ms_sensory']=""
            CIstats['100ms_frontal']=""
            CIstats['100ms_sensory']=""
            CIstats['250ms_frontal']=""
            CIstats['250ms_sensory']=""
        
            import scipy.stats as stats
        
            for col in list(CIstats.columns): 
                a = iRatios[col].values
                float_arr = np.vstack(a[:]).astype(np.float)
                # n = len(float_arr)
                n = np.count_nonzero(~np.isnan(float_arr))
                m = iRatios[col].mean()
                se = scipy.stats.sem(float_arr, nan_policy = 'omit')
                h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
                #h = np.nanstd(float_arr) for standard dev
                CIstats.at['95% CI',col]= h
                CIstats.at['mean',col]= m
                CIstats.at['upper bound',col]= m + h     
                CIstats.at['lower bound',col]= m - h
                CIstats.at['one sample t-test p val',col] = stats.ttest_1samp(a,1.0,nan_policy='omit')[1]
                if CIstats.at['one sample t-test p val',col] < 0.05:
                    CIstats.at['significant?',col] = 'red'
                else:
                    CIstats.at['significant?',col] = 'black'
                    
            from matplotlib import pyplot as plt
            
            plt.figure(figsize=(3.5,5))
            names = np.asarray([0,50,100,250])
            values = np.asarray([CIstats.at['mean','0ms_frontal'],CIstats.at['mean','50ms_frontal'],CIstats.at['mean','100ms_frontal'],CIstats.at['mean','250ms_frontal']])
            linevalues = [1,1,1,1]
            plt.ylim((0.3,2.6))
            plt.plot(names,values,'darkorange')
            yerrUpper = np.asarray([CIstats.at['upper bound','0ms_frontal'],CIstats.at['upper bound','50ms_frontal'],CIstats.at['upper bound','100ms_frontal'],CIstats.at['upper bound','250ms_frontal']])
            yerrLower = np.asarray([CIstats.at['lower bound','0ms_frontal'],CIstats.at['lower bound','50ms_frontal'],CIstats.at['lower bound','100ms_frontal'],CIstats.at['lower bound','250ms_frontal']])
            flat_yerrUpper = yerrUpper.flatten()
            flat_yerrLower = yerrLower.flatten()
            plt.fill_between(names, flat_yerrUpper, flat_yerrLower,alpha=0.5,interpolate=True,color='navajowhite')
            if 'A1' in fiberTypes and 'V1' in fiberTypes:
                plt.title(fiberTypes[0]+'_'+fiberTypes[1]+' auditory-visual '+cellType+' both opsin configurations')  
            else: 
                plt.title(fiberTypes[0]+'_'+fiberTypes[1]+' sensory-frontal '+cellType+'  '+opsinConfig)   
            plt.plot(names,linevalues,'k--',alpha=0.7)
            plt.text(205, 2.3, 'n = '+str(len(iRatios['0ms_frontal'])), fontsize=14)
    
            plt.show()
                
         
            for cell in list(iRatios.index):
                names = np.asarray([0,50,100,250])
                values = np.asarray([iRatios.at[cell,'0ms_frontal'],iRatios.at[cell,'50ms_frontal'],iRatios.at[cell,'100ms_frontal'],iRatios.at[cell,'250ms_frontal']])
                linevalues = [1,1,1,1]
                plt.ylim((0.3,2.6))
                if len(values) - sum(np.isnan(values)) > 1:
                    plt.plot(names,values,'lightgrey',linewidth=1,alpha=0.5)
                elif len(values) - sum(np.isnan(values)) == 1:
                    plt.plot(names,values,'lightgrey',alpha=0.5, marker = '.')
                plt.show()
          
    
          
            plt.text(0, 2.8, "%.3f" % CIstats.at['one sample t-test p val','0ms_frontal'], color = CIstats.at['significant?','0ms_frontal'])
            plt.text(45, 2.8, "%.3f" % CIstats.at['one sample t-test p val','50ms_frontal'], color = CIstats.at['significant?','50ms_frontal'])
            plt.text(90, 2.8, "%.3f" % CIstats.at['one sample t-test p val','100ms_frontal'], color = CIstats.at['significant?','100ms_frontal'])
            plt.text(230, 2.8, "%.3f" % CIstats.at['one sample t-test p val','250ms_frontal'], color = CIstats.at['significant?','250ms_frontal'])
        
             
            if show == 1:
                imagename = fiberTypes[0]+'_'+fiberTypes[1]+' sensory-frontal '+cellType+'  '+opsinConfig
                imagepath = Path(imageloc)
                
                plt.savefig(imagepath / (imagename + '.eps'), format='eps', dpi=1200)
        
                
            
            
            plt.figure(figsize=(3.5,5))
            names = np.asarray([0,50,100,250])
            values = np.asarray([CIstats.at['mean','0ms_sensory'],CIstats.at['mean','50ms_sensory'],CIstats.at['mean','100ms_sensory'],CIstats.at['mean','250ms_sensory']])
            linevalues = [1,1,1,1]
            plt.ylim((0.3,2.6))
            plt.plot(names,values,'darkorange')
            yerrUpper = np.asarray([CIstats.at['upper bound','0ms_sensory'],CIstats.at['upper bound','50ms_sensory'],CIstats.at['upper bound','100ms_sensory'],CIstats.at['upper bound','250ms_sensory']])
            yerrLower = np.asarray([CIstats.at['lower bound','0ms_sensory'],CIstats.at['lower bound','50ms_sensory'],CIstats.at['lower bound','100ms_sensory'],CIstats.at['lower bound','250ms_sensory']])
            flat_yerrUpper = yerrUpper.flatten()
            flat_yerrLower = yerrLower.flatten()
            plt.fill_between(names, flat_yerrUpper, flat_yerrLower,alpha=0.5,interpolate=True,color='navajowhite')
            if 'A1' in fiberTypes and 'V1' in fiberTypes:
                plt.title(fiberTypes[0]+'_'+fiberTypes[1]+' visual-auditory '+cellType+' both opsin configurations')   
            else:
                plt.title(fiberTypes[0]+'_'+fiberTypes[1]+' frontal-sensory '+cellType+'  '+opsinConfig)   
            plt.plot(names,linevalues,'k--',alpha=0.7)
            plt.text(205, 2.3, 'n = '+str(len(iRatios['0ms_sensory'])), fontsize=14)
            plt.show()
            
                    
               
            for cell in list(iRatios.index):
                names = np.asarray([0,50,100,250])
                values = np.asarray([iRatios.at[cell,'0ms_sensory'],iRatios.at[cell,'50ms_sensory'],iRatios.at[cell,'100ms_sensory'],iRatios.at[cell,'250ms_sensory']])
                linevalues = [1,1,1,1]
                plt.ylim((0.3,2.6))
                if len(values) - sum(np.isnan(values)) > 1:
                    plt.plot(names,values,'lightgrey',linewidth=1,alpha=0.5)
                elif len(values) - sum(np.isnan(values)) == 1:
                    plt.plot(names,values,'lightgrey',alpha=0.5, marker = '.')
                plt.show()
                
            plt.text(0, 2.8, "%.3f" % CIstats.at['one sample t-test p val','0ms_sensory'], color = CIstats.at['significant?','0ms_sensory'])
            plt.text(45, 2.8, "%.3f" % CIstats.at['one sample t-test p val','50ms_sensory'], color = CIstats.at['significant?','50ms_sensory'])
            plt.text(90, 2.8, "%.3f" % CIstats.at['one sample t-test p val','100ms_sensory'], color = CIstats.at['significant?','100ms_sensory'])
            plt.text(230, 2.8, "%.3f" % CIstats.at['one sample t-test p val','250ms_sensory'], color = CIstats.at['significant?','250ms_sensory'])   
             
            if show == 1:
                imagename = fiberTypes[0]+'_'+fiberTypes[1]+' frontal-sensory '+cellType+'  '+opsinConfig
                imagepath = Path(imageloc)
                
                plt.savefig(imagepath / (imagename + '.eps'), format='eps', dpi=1200)
                    

    return    opsinSwapRatios, nonSwapRatios 



#%%

def IPSCpeakanalysis(fiberTypes, cellType, delay1, delay2, delay3, delay4, opsinSwapList, confidence, oneMapCells, show, imageloc, complete, method):

    import tkinter
    from tkinter.filedialog import askopenfilename
    import pickle
    from matplotlib import pyplot as plt

    delayList = [delay1,delay2,delay3,delay4]
    
    from pathlib import Path
    savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\IPSC")
    
    
    # make a list with all folder names including cellType:
    import os
    allnames = os.listdir(savedLoc)
    selectednames = [x for x in allnames if cellType in x]

    
    import pandas as pd
    import numpy as np
    frontalsensoryData = pd.DataFrame()
    sensoryfrontalData = pd.DataFrame()
    coincidentData = pd.DataFrame()
    
    peakData = pd.DataFrame({'cell ID':[*selectednames]}).set_index('cell ID')
    
    peakData['0ms_frontal single']=""
    peakData['0ms_frontal paired']=""
    peakData['0ms_sensory single']=""
    peakData['0ms_sensory paired']=""
    peakData['50ms_frontal single']=""
    peakData['50ms_frontal paired']=""
    peakData['50ms_sensory single']=""
    peakData['50ms_sensory paired']=""
    peakData['100ms_frontal single']=""
    peakData['100ms_frontal paired']=""
    peakData['100ms_sensory single']=""
    peakData['100ms_sensory paired']=""
    peakData['250ms_frontal single']=""
    peakData['250ms_frontal paired']=""
    peakData['250ms_sensory single']=""
    peakData['250ms_sensory paired']=""

    if method == 'paired pulse':

        pairedpeakRatio = pd.DataFrame(index=peakData.index)
        
        pairedpeakRatio['0ms_frontal']=""
        pairedpeakRatio['0ms_sensory']=""
        pairedpeakRatio['50ms_frontal']=""
        pairedpeakRatio['50ms_sensory']=""
        pairedpeakRatio['100ms_frontal']=""
        pairedpeakRatio['100ms_sensory']=""
        pairedpeakRatio['250ms_frontal']=""
        pairedpeakRatio['250ms_sensory']=""
        
        
        
        for i in selectednames:

            print('processing...'+str(i)) 
            # point at data file to view
            cellPath = savedLoc / i
            workspacedf = pd.DataFrame()
            
           
            for file in os.listdir(cellPath):      
                for delay in delayList:
                    if '_'+str(delay)+'ms' in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                workspacedf[str(delay)+'_'+str(k)] = loadedData[k]
                               
    
                        
            # this is where we MANUALLY change which pulse stimulates which fiber pop!!!
            
            for delay in delayList:        
                if delay == 0:

                    # print('chose not to analyze 0ms')
                    pairedpeakRatio.at[str(i),'0ms_sensory'] = np.nan
                    pairedpeakRatio.at[str(i),'0ms_frontal'] = np.nan

                        
    
                else:   
                    try:
                        

                        for inputOrder in ['_paired pulse map','_paired pulse map_swap']:
                            if inputOrder == '_paired pulse map':
                                single = '_pulse 1 map'
                                pairedSub1 = workspacedf[str(delay)+inputOrder+'_data'] - workspacedf[str(delay)+single+'_data']
                                peak2BL = np.mean(pairedSub1[990+(delay*10):999+(delay*10)])
                                peak2Loc = np.argmax(pairedSub1[1000+(delay*10):1300+(delay*10)]) + 1000 +(delay*10)  
                                peak2 = np.mean(pairedSub1[peak2Loc-3:peak2Loc+3]) - peak2BL
                                peak1BL =  np.mean(workspacedf[str(delay)+inputOrder+'_data'][900:999])
                                peak1Loc = np.argmax(workspacedf[str(delay)+inputOrder+'_data'][1000:1300]) + 1000
                                peak1 = np.mean(workspacedf[str(delay)+inputOrder+'_data'][peak1Loc-3:peak1Loc+3]) - peak1BL                            
                                
                                PPR = peak2/peak1

                                pairedpeakRatio.at[str(i),str(delay)+'ms_sensory'] = PPR
                                
                                # pulse1.plot(workspacedf[str(delay)+single+'_data'])
                            
                            elif inputOrder == '_paired pulse map_swap':
                                single = '_pulse 2 map'
                                pairedSub1 = workspacedf[str(delay)+inputOrder+'_data'] - workspacedf[str(delay)+single+'_data']
                                peak2BL = np.mean(pairedSub1[990+(delay*10):999+(delay*10)])
                                peak2Loc = np.argmax(pairedSub1[1000+(delay*10):1300+(delay*10)]) + 1000 +(delay*10)  
                                peak2 = np.mean(pairedSub1[peak2Loc-3:peak2Loc+3]) - peak2BL
                                peak1BL =  np.mean(workspacedf[str(delay)+inputOrder+'_data'][900:999])
                                peak1Loc = np.argmax(workspacedf[str(delay)+inputOrder+'_data'][1000:1300]) + 1000
                                peak1 = np.mean(workspacedf[str(delay)+inputOrder+'_data'][peak1Loc-3:peak1Loc+3]) - peak1BL
                            
                                PPR = peak2/peak1
    
                                pairedpeakRatio.at[str(i),str(delay)+'ms_frontal'] = PPR
                                
                                # pulse2.plot(workspacedf[str(delay)+single+'_data'])
                                
                            # if delay == 50:
                            #     plt.figure()
                            #     plt.plot(workspacedf[str(delay)+inputOrder+'_data'])
                            #     plt.plot(workspacedf[str(delay)+'_paired pulse map_data'])
                            #     plt.plot(workspacedf[str(delay)+'_paired pulse map_swap_data'])
                            #     plt.title(str(i) + '  '+inputOrder)

                    except:
                        
                        print('missing delay points detected in '+str(i))

                        pairedpeakRatio.at[str(i),str(delay)+'ms_frontal'] = np.nan
                        pairedpeakRatio.at[str(i),str(delay)+'ms_sensory'] = np.nan

       
        
       
        
       
        
       
        
    if method == 'mixed pulse':
        for i in selectednames:
            print('processing...'+str(i)) 
            # point at data file to view
            cellPath = savedLoc / i
            workspacedf = pd.DataFrame()
            
           
            for file in os.listdir(cellPath):      
                for delay in delayList:
                    if '_'+str(delay)+'ms' in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                workspacedf[str(delay)+'_'+str(k)] = loadedData[k]
                               
            
            #to remove noise
            test = pd.DataFrame()
            for icol in workspacedf.columns:
                test[icol] = np.asarray(workspacedf.loc[:9998,icol]) - np.asarray(workspacedf.loc[1:9999,icol])
            mask = test > 20

            for column in workspacedf.columns:
                
                # print(mask.index[mask[column] == True].tolist())
                
                for spike in mask.index[mask[column] == True].tolist():
                    # print(workspacedf.at[spike,column])
                    workspacedf.at[spike,column] = np.mean([workspacedf[column].loc[spike-3],workspacedf[column].loc[spike+3]])
                    workspacedf.at[spike-1,column] = np.mean([workspacedf[column].loc[spike-3],workspacedf[column].loc[spike+3]])
                    workspacedf.at[spike+1,column] = np.mean([workspacedf[column].loc[spike-3],workspacedf[column].loc[spike+3]])
                

                        
            # this is where we MANUALLY change which pulse stimulates which fiber pop!!!
            
            for delay in delayList:        
                if delay == 0:
                    try:
                        if i in opsinSwapList:
                            
                            coincidentData['actualCoincident'] = workspacedf[str(delay)+'_'+'paired pulse map_data']
                            coincidentData['arithmeticSum'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf[str(delay)+'_'+'pulse 1 map_data']
                        
                        if i not in opsinSwapList: # same as above if in opsinSwapList
                            
                           coincidentData['actualCoincident'] = workspacedf[str(delay)+'_'+'paired pulse map_data']
                           coincidentData['arithmeticSum'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf[str(delay)+'_'+'pulse 1 map_data']
                            
                           
                        #for both
                        #peaks
                        maxLocActual = np.argmax(coincidentData['actualCoincident'][1000:1300],axis = 0) +1000
                        maxValActual = []
                        actualBL = np.mean(coincidentData['actualCoincident'][990:999],axis = 0)
                        maxValActual = np.mean(coincidentData['actualCoincident'][maxLocActual-3 : maxLocActual+3], 0) - actualBL       
                        
                        maxLocSum = np.argmax(coincidentData['arithmeticSum'][1000:1300],axis = 0) +1000
                        maxValSum = []
                        sumBL = np.mean(coincidentData['arithmeticSum'][990:999],axis = 0)
                        maxValSum = np.mean(coincidentData['arithmeticSum'][maxLocSum-3 : maxLocSum+3], 0) - sumBL
                        
                        peakData.at[str(i),str(delay)+'ms_sensory single'] = maxValSum #now has to equal arithmetic addition of traces peak
                        peakData.at[str(i),str(delay)+'ms_sensory paired'] = maxValActual #now has to equal coincident
                        peakData.at[str(i),str(delay)+'ms_frontal single'] = maxValSum # same as above
                        peakData.at[str(i),str(delay)+'ms_frontal paired'] = maxValActual # same as above
                        
    
                        
                        
                    except:
                        #peaks
                        print('missing delay points detected in '+str(i))
                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired pulse'] = np.nan
                        frontalsensoryData['delay '+str(delay)+'ms_sensory single pulse'] = np.nan
                        
                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired pulse'] = np.nan
                        sensoryfrontalData['delay '+str(delay)+'ms_frontal single pulse'] = np.nan
        
                        peakData.at[str(i),str(delay)+'ms_sensory single'] = np.nan
                        peakData.at[str(i),str(delay)+'ms_sensory paired'] = np.nan
                        peakData.at[str(i),str(delay)+'ms_frontal single'] = np.nan
                        peakData.at[str(i),str(delay)+'ms_frontal paired'] = np.nan
                        
    
                else:   
                    try:
                        if i in opsinSwapList:
                       
                            frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_swap_data']                        
                            workspacedf['zeros'] = np.zeros(len(workspacedf))
                            workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 1 map_data'][1000:2000]
                            frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf['zeros']
    
                            sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_data']                        
                            workspacedf['zeros'] = np.zeros(len(workspacedf))
                            workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 2 map_data'][1000:2000]
                            sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 1 map_data'] + workspacedf['zeros']
    
    
                        if i not in opsinSwapList:
                            
                            frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_data']                        
                            workspacedf['zeros'] = np.zeros(len(workspacedf))
                            workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 2 map_data'][1000:2000]
                            frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 1 map_data'] + workspacedf['zeros']
    
                            sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_swap_data']                        
                            workspacedf['zeros'] = np.zeros(len(workspacedf))
                            workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 1 map_data'][1000:2000]
                            sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf['zeros']
                            
                          
                        #for all
                            
                        maxLocSensoryActual = np.argmax(frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'][1000+(delay*10):1300+(delay*10)],axis = 0) + 1000 +(delay*10)  
                        sensoryActualPeak = np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'][maxLocSensoryActual-3 : maxLocSensoryActual+3], 0)       
                        sensoryActualBL = np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'][990+(delay*10):999+(delay*10)], 0)
                        peakValSensoryActual = sensoryActualPeak - sensoryActualBL    
                            
                        maxLocSensoryArithmetic = np.argmax(frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'][1000+(delay*10):1300+(delay*10)],axis = 0) + 1000 +(delay*10)  
                        sensoryArithmeticPeak = np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'][maxLocSensoryArithmetic-3 : maxLocSensoryArithmetic+3], 0)        
                        sensoryArithmeticBL = np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'][990+(delay*10):999+(delay*10)], 0)
                        peakValSensoryArithmetic = sensoryArithmeticPeak - sensoryArithmeticBL                         
    
                        maxLocFrontalActual = np.argmax(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'][1000+(delay*10):1300+(delay*10)],axis = 0)   + 1000 +(delay*10) 
                        frontalActualPeak = np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'][maxLocFrontalActual-3 : maxLocFrontalActual+3], 0)        
                        frontalActualBL = np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'][990+(delay*10):999+(delay*10)], 0)
                        peakValFrontalActual = frontalActualPeak - frontalActualBL    
                            
                        maxLocFrontalArithmetic = np.argmax(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'][1000+(delay*10):1300+(delay*10)],axis = 0)  + 1000 +(delay*10) 
                        frontalArithmeticPeak = np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'][maxLocFrontalArithmetic-3 : maxLocFrontalArithmetic+3], 0)        
                        frontalArithmeticBL = np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'][990+(delay*10):999+(delay*10)], 0)
                        peakValFrontalArithmetic = frontalArithmeticPeak - frontalArithmeticBL                         
                        
                 
                        #get peak amplitudes
                        peakData.at[str(i),str(delay)+'ms_sensory single'] = peakValSensoryArithmetic
                        peakData.at[str(i),str(delay)+'ms_sensory paired'] = peakValSensoryActual
                        peakData.at[str(i),str(delay)+'ms_frontal single'] = peakValFrontalArithmetic
                        peakData.at[str(i),str(delay)+'ms_frontal paired'] = peakValFrontalActual
                    
                    
                    except:
                        
                        print('missing delay points detected in '+str(i))
                        #peaks
                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired pulse'] = np.nan
                        frontalsensoryData['delay '+str(delay)+'ms_sensory single pulse'] = np.nan
                        
                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired pulse'] = np.nan
                        sensoryfrontalData['delay '+str(delay)+'ms_frontal single pulse'] = np.nan
        
           
                        peakData.at[str(i),str(delay)+'ms_sensory single'] = np.nan
                        peakData.at[str(i),str(delay)+'ms_sensory paired'] = np.nan
                        peakData.at[str(i),str(delay)+'ms_frontal single'] = np.nan
                        peakData.at[str(i),str(delay)+'ms_frontal paired'] = np.nan

        pairedpeakRatio = pd.DataFrame(index=peakData.index)
        
        pairedpeakRatio['0ms_frontal']=""
        pairedpeakRatio['0ms_sensory']=""
        pairedpeakRatio['50ms_frontal']=""
        pairedpeakRatio['50ms_sensory']=""
        pairedpeakRatio['100ms_frontal']=""
        pairedpeakRatio['100ms_sensory']=""
        pairedpeakRatio['250ms_frontal']=""
        pairedpeakRatio['250ms_sensory']=""        

        for iIndex in selectednames:
                    pairedpeakRatio.at[str(iIndex),'0ms_frontal']= peakData.at[str(iIndex),'0ms_frontal paired'] / peakData.at[str(iIndex),'0ms_frontal single']
                    pairedpeakRatio.at[str(iIndex),'0ms_sensory']= peakData.at[str(iIndex),'0ms_sensory paired'] / peakData.at[str(iIndex),'0ms_sensory single']
                    pairedpeakRatio.at[str(iIndex),'50ms_frontal']= peakData.at[str(iIndex),'50ms_frontal paired'] / peakData.at[str(iIndex),'50ms_frontal single']
                    pairedpeakRatio.at[str(iIndex),'50ms_sensory']= peakData.at[str(iIndex),'50ms_sensory paired'] / peakData.at[str(iIndex),'50ms_sensory single']
                    pairedpeakRatio.at[str(iIndex),'100ms_frontal']= peakData.at[str(iIndex),'100ms_frontal paired'] / peakData.at[str(iIndex),'100ms_frontal single']
                    pairedpeakRatio.at[str(iIndex),'100ms_sensory']= peakData.at[str(iIndex),'100ms_sensory paired'] / peakData.at[str(iIndex),'100ms_sensory single']
                    pairedpeakRatio.at[str(iIndex),'250ms_frontal']= peakData.at[str(iIndex),'250ms_frontal paired'] / peakData.at[str(iIndex),'250ms_frontal single']
                    pairedpeakRatio.at[str(iIndex),'250ms_sensory']= peakData.at[str(iIndex),'250ms_sensory paired'] / peakData.at[str(iIndex),'250ms_sensory single']
        

    #mouse averaging and plotting
    for ratiodf in [pairedpeakRatio]:
    
        ratiodf.index = ratiodf.index.map(lambda x: str(x)[:-9])
        workspaceMousedf = ratiodf.copy()
        workspaceMousedf = workspaceMousedf.astype(float)
        strippedID = []
        for i in selectednames:
            strippedID.append(i[0:-9])
        workspaceMousedf['stripped Names']=strippedID
        grp_mouse = workspaceMousedf.groupby(['stripped Names'])
        pairedMouseRatio = grp_mouse.mean()
        

 
        
        opsinSwapMice = list(map(lambda x: str(x)[:-9],opsinSwapList))
        opsinSwapRatios = pairedMouseRatio[pairedMouseRatio.index.isin(opsinSwapMice) == True]
        nonSwapRatios = pairedMouseRatio[pairedMouseRatio.index.isin(opsinSwapMice) == False]
        if 'A1' in fiberTypes and 'V1' in fiberTypes:
            nonSwapRatios = pairedMouseRatio.copy()
        
        
        if complete == 1:
            nonSwapRatios = nonSwapRatios.dropna()
            opsinSwapRatios = opsinSwapRatios.dropna()
      
        
        import numpy as np      
        import scipy.stats
        
        
        nameList = ['opsin swap','default']
        for name, iRatios in enumerate([opsinSwapRatios, nonSwapRatios]):     
            
            if len(iRatios) == 0:
                continue
            
            opsinConfig = nameList[name]
            
            
            #get CI stats
            CIstats = pd.DataFrame(index=['95% CI','mean','upper bound','lower bound'])
            
            CIstats['0ms_frontal']=""
            CIstats['0ms_sensory']=""
            CIstats['50ms_frontal']=""
            CIstats['50ms_sensory']=""
            CIstats['100ms_frontal']=""
            CIstats['100ms_sensory']=""
            CIstats['250ms_frontal']=""
            CIstats['250ms_sensory']=""
        
            import scipy.stats as stats
        
            for col in list(CIstats.columns): 
                a = iRatios[col].values
                float_arr = np.vstack(a[:]).astype(np.float)
                n = len(float_arr)
                m = iRatios[col].mean()
                se = scipy.stats.sem(float_arr, nan_policy = 'omit')
                h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
                #h = np.nanstd(float_arr) for standard dev
                CIstats.at['95% CI',col]= h
                CIstats.at['mean',col]= m
                CIstats.at['upper bound',col]= m + h     
                CIstats.at['lower bound',col]= m - h
                CIstats.at['one sample t-test p val',col] = stats.ttest_1samp(a,1.0,nan_policy='omit')[1]
                if CIstats.at['one sample t-test p val',col] < 0.05:
                    CIstats.at['significant?',col] = 'red'
                else:
                    CIstats.at['significant?',col] = 'black'
                    
            from matplotlib import pyplot as plt
            
            plt.figure(figsize=(3.5,5))
            names = np.asarray([50,100,250])
            values = np.asarray([CIstats.at['mean','50ms_frontal'],CIstats.at['mean','100ms_frontal'],CIstats.at['mean','250ms_frontal']])
            linevalues = [1,1,1]
            plt.ylim((0.3,2.6))
            plt.xlim((0,300))
            plt.plot(names,values,'darkorange')
            yerrUpper = np.asarray([CIstats.at['upper bound','50ms_frontal'],CIstats.at['upper bound','100ms_frontal'],CIstats.at['upper bound','250ms_frontal']])
            yerrLower = np.asarray([CIstats.at['lower bound','50ms_frontal'],CIstats.at['lower bound','100ms_frontal'],CIstats.at['lower bound','250ms_frontal']])
            flat_yerrUpper = yerrUpper.flatten()
            flat_yerrLower = yerrLower.flatten()
            plt.fill_between(names, flat_yerrUpper, flat_yerrLower,alpha=0.5,interpolate=True,color='navajowhite')
            if 'A1' in fiberTypes and 'V1' in fiberTypes:
                plt.title(fiberTypes[0]+'_'+fiberTypes[1]+' auditory-visual '+cellType+' both opsin configurations')  
            else: 
                plt.title(fiberTypes[0]+'_'+fiberTypes[1]+' sensory-frontal '+cellType+'  '+opsinConfig)   
            plt.plot(names,linevalues,'k--',alpha=0.7)
            plt.text(205, 2.3, 'n = '+str(len(iRatios['50ms_frontal'])), fontsize=14)
            if ratiodf.equals(pairedpeakRatio):
                plt.text(205, 2, 'peak', fontsize=14)
            else:
                plt.text(205, 2, 'charge transfer', fontsize=14)
            plt.show()
                
         
            for cell in list(iRatios.index):
                names = np.asarray([50,100,250])
                values = np.asarray([iRatios.at[cell,'50ms_frontal'],iRatios.at[cell,'100ms_frontal'],iRatios.at[cell,'250ms_frontal']])
                linevalues = [1,1,1]
                plt.ylim((0.3,2.6))
                plt.xlim((0,300))
                if len(values) - sum(np.isnan(values)) > 1:
                    plt.plot(names,values,'lightgrey',linewidth=1,alpha=0.5)
                elif len(values) - sum(np.isnan(values)) == 1:
                    plt.plot(names,values,'lightgrey',alpha=0.5, marker = '.')
                plt.show()
          
            plt.text(45, 2.8, "%.3f" % CIstats.at['one sample t-test p val','50ms_frontal'], color = CIstats.at['significant?','50ms_frontal'])
            plt.text(90, 2.8, "%.3f" % CIstats.at['one sample t-test p val','100ms_frontal'], color = CIstats.at['significant?','100ms_frontal'])
            plt.text(230, 2.8, "%.3f" % CIstats.at['one sample t-test p val','250ms_frontal'], color = CIstats.at['significant?','250ms_frontal'])
        
             
            if show == 1:
                imagename = fiberTypes[0]+'_'+fiberTypes[1]+' sensory-frontal '+cellType+'  '+opsinConfig
                imagepath = Path(imageloc)
                
                plt.savefig(imagepath / (imagename + '.eps'), format='eps', dpi=1200)
        
                
            
            
            plt.figure(figsize=(3.5,5))
            names = np.asarray([50,100,250])
            values = np.asarray([CIstats.at['mean','50ms_sensory'],CIstats.at['mean','100ms_sensory'],CIstats.at['mean','250ms_sensory']])
            linevalues = [1,1,1]
            plt.ylim((0.3,2.6))
            plt.xlim((0,300))
            plt.plot(names,values,'darkorange')
            yerrUpper = np.asarray([CIstats.at['upper bound','50ms_sensory'],CIstats.at['upper bound','100ms_sensory'],CIstats.at['upper bound','250ms_sensory']])
            yerrLower = np.asarray([CIstats.at['lower bound','50ms_sensory'],CIstats.at['lower bound','100ms_sensory'],CIstats.at['lower bound','250ms_sensory']])
            flat_yerrUpper = yerrUpper.flatten()
            flat_yerrLower = yerrLower.flatten()
            plt.fill_between(names, flat_yerrUpper, flat_yerrLower,alpha=0.5,interpolate=True,color='navajowhite')
            if 'A1' in fiberTypes and 'V1' in fiberTypes:
                plt.title(fiberTypes[0]+'_'+fiberTypes[1]+' visual-auditory '+cellType+' both opsin configurations')   
            else:
                plt.title(fiberTypes[0]+'_'+fiberTypes[1]+' frontal-sensory '+cellType+'  '+opsinConfig)   
            plt.plot(names,linevalues,'k--',alpha=0.7)
            plt.text(205, 2.3, 'n = '+str(len(iRatios['50ms_sensory'])), fontsize=14)
            if ratiodf.equals(pairedpeakRatio):
                plt.text(205, 2, 'peak', fontsize=14)
            else:
                plt.text(205, 2, 'charge transfer', fontsize=14)
            plt.show()
            
                    
               
            for cell in list(iRatios.index):
                names = np.asarray([50,100,250])
                values = np.asarray([iRatios.at[cell,'50ms_sensory'],iRatios.at[cell,'100ms_sensory'],iRatios.at[cell,'250ms_sensory']])
                linevalues = [1,1,1]
                plt.ylim((0.3,2.6))
                plt.xlim((0,300))
                if len(values) - sum(np.isnan(values)) > 1:
                    plt.plot(names,values,'lightgrey',linewidth=1,alpha=0.5)
                elif len(values) - sum(np.isnan(values)) == 1:
                    plt.plot(names,values,'lightgrey',alpha=0.5, marker = '.')
                plt.show()
                
            plt.text(45, 2.8, "%.3f" % CIstats.at['one sample t-test p val','50ms_sensory'], color = CIstats.at['significant?','50ms_sensory'])
            plt.text(90, 2.8, "%.3f" % CIstats.at['one sample t-test p val','100ms_sensory'], color = CIstats.at['significant?','100ms_sensory'])
            plt.text(230, 2.8, "%.3f" % CIstats.at['one sample t-test p val','250ms_sensory'], color = CIstats.at['significant?','250ms_sensory'])   
             
            if show == 1:
                imagename = fiberTypes[0]+'_'+fiberTypes[1]+' frontal-sensory '+cellType+'  '+opsinConfig
                imagepath = Path(imageloc)
                
                plt.savefig(imagepath / (imagename + '.eps'), format='eps', dpi=1200)
                    

    return    opsinSwapRatios, nonSwapRatios 
 
#%%

def IPSCpeakanalysis2(fiberTypes, cellType, delay1, delay2, delay3, delay4, opsinSwapList, confidence, oneMapCells, show, imageloc, complete):

    import tkinter
    from tkinter.filedialog import askopenfilename
    import pickle
    from matplotlib import pyplot as plt

    delayList = [delay1,delay2,delay3,delay4]
    
    from pathlib import Path
    savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\IPSC")
    
    
    # make a list with all folder names including cellType:
    import os
    allnames = os.listdir(savedLoc)
    selectednames = [x for x in allnames if cellType in x]
    
    # selectednames.remove('210426_wt_1580_cell6_RS')
    # selectednames.remove('210426_wt_1579_cell1_RS')
    selectednames.remove('210420_wt_1570_cell1_RS')
    
    import pandas as pd
    import numpy as np
    frontalsensoryData = pd.DataFrame()
    sensoryfrontalData = pd.DataFrame()
    coincidentData = pd.DataFrame()
    
    peakData = pd.DataFrame({'cell ID':[*selectednames]}).set_index('cell ID')
    
    peakData['0ms_frontal single']=""
    peakData['0ms_frontal paired']=""
    peakData['0ms_sensory single']=""
    peakData['0ms_sensory paired']=""
    peakData['50ms_frontal single']=""
    peakData['50ms_frontal paired']=""
    peakData['50ms_sensory single']=""
    peakData['50ms_sensory paired']=""
    peakData['100ms_frontal single']=""
    peakData['100ms_frontal paired']=""
    peakData['100ms_sensory single']=""
    peakData['100ms_sensory paired']=""
    peakData['250ms_frontal single']=""
    peakData['250ms_frontal paired']=""
    peakData['250ms_sensory single']=""
    peakData['250ms_sensory paired']=""


    for i in selectednames:
        print('processing...'+str(i)) 
        # point at data file to view
        cellPath = savedLoc / i
        workspacedf = pd.DataFrame()
        
       
        for file in os.listdir(cellPath):      
            for delay in delayList:
                if '_'+str(delay)+'ms' in file:
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    for k in loadedData.keys():
                        if '_data' in k:
                            workspacedf[str(delay)+'_'+str(k)] = loadedData[k]
                           

        #to remove noise
        test = pd.DataFrame()
        for icol in workspacedf.columns:
            test[icol] = np.asarray(workspacedf.loc[:9998,icol]) - np.asarray(workspacedf.loc[1:9999,icol])
        mask = test > 20

        for column in workspacedf.columns:
            
            # print(mask.index[mask[column] == True].tolist())
            
            for spike in mask.index[mask[column] == True].tolist():
                # print(workspacedf.at[spike,column])
                workspacedf.at[spike,column] = np.mean([workspacedf[column].loc[spike-3],workspacedf[column].loc[spike+3]])
                workspacedf.at[spike-1,column] = np.mean([workspacedf[column].loc[spike-3],workspacedf[column].loc[spike+3]])
                workspacedf.at[spike+1,column] = np.mean([workspacedf[column].loc[spike-3],workspacedf[column].loc[spike+3]])
                        
        # this is where we MANUALLY change which pulse stimulates which fiber pop!!!
        
        for delay in delayList:        
            if delay == 0:

                #peaks
                # print('missing delay points detected in '+str(i))
                frontalsensoryData['delay '+str(delay)+'ms_sensory paired pulse'] = np.nan
                frontalsensoryData['delay '+str(delay)+'ms_sensory single pulse'] = np.nan
                
                sensoryfrontalData['delay '+str(delay)+'ms_frontal paired pulse'] = np.nan
                sensoryfrontalData['delay '+str(delay)+'ms_frontal single pulse'] = np.nan

                peakData.at[str(i),str(delay)+'ms_sensory single'] = np.nan
                peakData.at[str(i),str(delay)+'ms_sensory paired'] = np.nan
                peakData.at[str(i),str(delay)+'ms_frontal single'] = np.nan
                peakData.at[str(i),str(delay)+'ms_frontal paired'] = np.nan
                

            else:   
                try:
                
                        
                    frontalsensoryData['delay '+str(delay)+'ms_sensory single'] = workspacedf[str(delay)+'_'+'pulse 2 map_data']                        
                    frontalsensoryData['delay '+str(delay)+'ms_sensory paired'] = workspacedf[str(delay)+'_'+'paired pulse map_data'] - workspacedf[str(delay)+'_'+'pulse 1 map_data']
                   
                    sensoryfrontalData['delay '+str(delay)+'ms_frontal single'] = workspacedf[str(delay)+'_'+'pulse 1 map_data']                        
                    sensoryfrontalData['delay '+str(delay)+'ms_frontal paired'] = workspacedf[str(delay)+'_'+'paired pulse map_swap_data'] - workspacedf[str(delay)+'_'+'pulse 2 map_data']

                    #for all
                        
                    maxLocSensorySingle = np.argmax(frontalsensoryData['delay '+str(delay)+'ms_sensory single'][1000:1300],axis = 0) + 1000
                    sensorySinglePeak = np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory single'][ maxLocSensorySingle-3 : maxLocSensorySingle+3], 0)        
                    sensorySingleBL = np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory single'][990:999], 0)
                    peakValSensorySingle = sensorySinglePeak - sensorySingleBL    
                   
                    maxLocSensoryPaired = np.argmax(frontalsensoryData['delay '+str(delay)+'ms_sensory paired'][1000+(delay*10):1300+(delay*10)],axis = 0) + 1000 + (delay*10)
                    sensoryPairedPeak = np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired'][ maxLocSensoryPaired-3 : maxLocSensoryPaired+3], 0)        
                    sensoryPairedBL = np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired'][990+(delay*10):999+(delay*10)], 0)
                    peakValSensoryPaired = sensoryPairedPeak - sensoryPairedBL                            
                    
                    maxLocFrontalSingle = np.argmax(sensoryfrontalData['delay '+str(delay)+'ms_frontal single'][1000:1300],axis = 0) + 1000
                    frontalSinglePeak = np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal single'][ maxLocFrontalSingle-3 : maxLocFrontalSingle+3], 0)        
                    frontalSingleBL = np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal single'][990:999], 0)
                    peakValFrontalSingle = frontalSinglePeak - frontalSingleBL    
                   
                    maxLocFrontalPaired = np.argmax(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired'][1000+(delay*10):1300+(delay*10)],axis = 0) + 1000 + (delay*10)
                    frontalPairedPeak = np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired'][ maxLocFrontalPaired-3 : maxLocFrontalPaired+3], 0)        
                    frontalPairedBL = np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired'][990+(delay*10):999+(delay*10)], 0)
                    peakValFrontalPaired = frontalPairedPeak - frontalPairedBL                    
                    
                    

                    #get peak amplitudes
                    peakData.at[str(i),str(delay)+'ms_sensory single'] = peakValSensorySingle
                    peakData.at[str(i),str(delay)+'ms_sensory paired'] = peakValSensoryPaired
                    peakData.at[str(i),str(delay)+'ms_frontal single'] = peakValFrontalSingle
                    peakData.at[str(i),str(delay)+'ms_frontal paired'] = peakValFrontalPaired
                
                
                except:
                    
                    print('missing delay points detected in '+str(i))
                    #peaks
                    frontalsensoryData['delay '+str(delay)+'ms_sensory paired'] = np.nan
                    frontalsensoryData['delay '+str(delay)+'ms_sensory single'] = np.nan
                    
                    sensoryfrontalData['delay '+str(delay)+'ms_frontal paired'] = np.nan
                    sensoryfrontalData['delay '+str(delay)+'ms_frontal single'] = np.nan
    
       
                    peakData.at[str(i),str(delay)+'ms_sensory single'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_sensory paired'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_frontal single'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_frontal paired'] = np.nan

    pairedpeakRatio = pd.DataFrame(index=peakData.index)
    
    pairedpeakRatio['0ms_frontal']=""
    pairedpeakRatio['0ms_sensory']=""
    pairedpeakRatio['50ms_frontal']=""
    pairedpeakRatio['50ms_sensory']=""
    pairedpeakRatio['100ms_frontal']=""
    pairedpeakRatio['100ms_sensory']=""
    pairedpeakRatio['250ms_frontal']=""
    pairedpeakRatio['250ms_sensory']=""        

    for iIndex in selectednames:
                pairedpeakRatio.at[str(iIndex),'0ms_frontal']= peakData.at[str(iIndex),'0ms_frontal paired'] / peakData.at[str(iIndex),'0ms_frontal single']
                pairedpeakRatio.at[str(iIndex),'0ms_sensory']= peakData.at[str(iIndex),'0ms_sensory paired'] / peakData.at[str(iIndex),'0ms_sensory single']
                pairedpeakRatio.at[str(iIndex),'50ms_frontal']= peakData.at[str(iIndex),'50ms_frontal paired'] / peakData.at[str(iIndex),'50ms_frontal single']
                pairedpeakRatio.at[str(iIndex),'50ms_sensory']= peakData.at[str(iIndex),'50ms_sensory paired'] / peakData.at[str(iIndex),'50ms_sensory single']
                pairedpeakRatio.at[str(iIndex),'100ms_frontal']= peakData.at[str(iIndex),'100ms_frontal paired'] / peakData.at[str(iIndex),'100ms_frontal single']
                pairedpeakRatio.at[str(iIndex),'100ms_sensory']= peakData.at[str(iIndex),'100ms_sensory paired'] / peakData.at[str(iIndex),'100ms_sensory single']
                pairedpeakRatio.at[str(iIndex),'250ms_frontal']= peakData.at[str(iIndex),'250ms_frontal paired'] / peakData.at[str(iIndex),'250ms_frontal single']
                pairedpeakRatio.at[str(iIndex),'250ms_sensory']= peakData.at[str(iIndex),'250ms_sensory paired'] / peakData.at[str(iIndex),'250ms_sensory single']
    

    #mouse averaging and plotting
    for ratiodf in [pairedpeakRatio]:
    
        ratiodf.index = ratiodf.index.map(lambda x: str(x)[:-9])
        workspaceMousedf = ratiodf.copy()
        workspaceMousedf = workspaceMousedf.astype(float)
        strippedID = []
        for i in selectednames:
            strippedID.append(i[0:-9])
        workspaceMousedf['stripped Names']=strippedID
        grp_mouse = workspaceMousedf.groupby(['stripped Names'])
        pairedMouseRatio = grp_mouse.mean()
        

 
        
        opsinSwapMice = list(map(lambda x: str(x)[:-9],opsinSwapList))
        opsinSwapRatios = pairedMouseRatio[pairedMouseRatio.index.isin(opsinSwapMice) == True]
        nonSwapRatios = pairedMouseRatio[pairedMouseRatio.index.isin(opsinSwapMice) == False]
        if 'A1' in fiberTypes and 'V1' in fiberTypes:
            nonSwapRatios = pairedMouseRatio.copy()
        
        
        if complete == 1:
            nonSwapRatios = nonSwapRatios.dropna()
            opsinSwapRatios = opsinSwapRatios.dropna()
      
        
        import numpy as np      
        import scipy.stats
        
        
        nameList = ['opsin swap','default']
        for name, iRatios in enumerate([opsinSwapRatios, nonSwapRatios]):     
            
            if len(iRatios) == 0:
                continue
            
            opsinConfig = nameList[name]
            
            
            #get CI stats
            CIstats = pd.DataFrame(index=['95% CI','mean','upper bound','lower bound'])
            
            CIstats['0ms_frontal']=""
            CIstats['0ms_sensory']=""
            CIstats['50ms_frontal']=""
            CIstats['50ms_sensory']=""
            CIstats['100ms_frontal']=""
            CIstats['100ms_sensory']=""
            CIstats['250ms_frontal']=""
            CIstats['250ms_sensory']=""
        
            import scipy.stats as stats
        
            for col in list(CIstats.columns): 
                a = iRatios[col].values
                float_arr = np.vstack(a[:]).astype(np.float)
                n = len(float_arr)
                m = iRatios[col].mean()
                se = scipy.stats.sem(float_arr, nan_policy = 'omit')
                h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
                #h = np.nanstd(float_arr) for standard dev
                CIstats.at['95% CI',col]= h
                CIstats.at['mean',col]= m
                CIstats.at['upper bound',col]= m + h     
                CIstats.at['lower bound',col]= m - h
                CIstats.at['one sample t-test p val',col] = stats.ttest_1samp(a,1.0,nan_policy='omit')[1]
                if CIstats.at['one sample t-test p val',col] < 0.05:
                    CIstats.at['significant?',col] = 'red'
                else:
                    CIstats.at['significant?',col] = 'black'
                    
            from matplotlib import pyplot as plt
            
            plt.figure(figsize=(3.5,5))
            names = np.asarray([50,100,250])
            values = np.asarray([CIstats.at['mean','50ms_frontal'],CIstats.at['mean','100ms_frontal'],CIstats.at['mean','250ms_frontal']])
            linevalues = [1,1,1]
            plt.ylim((0.3,2.6))
            plt.xlim((0,300))
            plt.plot(names,values,'darkorange')
            yerrUpper = np.asarray([CIstats.at['upper bound','50ms_frontal'],CIstats.at['upper bound','100ms_frontal'],CIstats.at['upper bound','250ms_frontal']])
            yerrLower = np.asarray([CIstats.at['lower bound','50ms_frontal'],CIstats.at['lower bound','100ms_frontal'],CIstats.at['lower bound','250ms_frontal']])
            flat_yerrUpper = yerrUpper.flatten()
            flat_yerrLower = yerrLower.flatten()
            plt.fill_between(names, flat_yerrUpper, flat_yerrLower,alpha=0.5,interpolate=True,color='navajowhite')
            if 'A1' in fiberTypes and 'V1' in fiberTypes:
                plt.title(fiberTypes[0]+'_'+fiberTypes[1]+' auditory-visual '+cellType+' both opsin configurations')  
            else: 
                plt.title(fiberTypes[0]+'_'+fiberTypes[1]+' sensory-frontal '+cellType+'  '+opsinConfig)   
            plt.plot(names,linevalues,'k--',alpha=0.7)
            plt.text(205, 2.3, 'n = '+str(len(iRatios['50ms_frontal'])), fontsize=14)
            if ratiodf.equals(pairedpeakRatio):
                plt.text(205, 2, 'peak', fontsize=14)
            else:
                plt.text(205, 2, 'charge transfer', fontsize=14)
            plt.show()
                
         
            for cell in list(iRatios.index):
                names = np.asarray([50,100,250])
                values = np.asarray([iRatios.at[cell,'50ms_frontal'],iRatios.at[cell,'100ms_frontal'],iRatios.at[cell,'250ms_frontal']])
                linevalues = [1,1,1]
                plt.ylim((0.3,2.6))
                plt.xlim((0,300))
                if len(values) - sum(np.isnan(values)) > 1:
                    plt.plot(names,values,'lightgrey',linewidth=1,alpha=0.5)
                elif len(values) - sum(np.isnan(values)) == 1:
                    plt.plot(names,values,'lightgrey',alpha=0.5, marker = '.')
                plt.show()
          
            plt.text(45, 2.8, "%.3f" % CIstats.at['one sample t-test p val','50ms_frontal'], color = CIstats.at['significant?','50ms_frontal'])
            plt.text(90, 2.8, "%.3f" % CIstats.at['one sample t-test p val','100ms_frontal'], color = CIstats.at['significant?','100ms_frontal'])
            plt.text(230, 2.8, "%.3f" % CIstats.at['one sample t-test p val','250ms_frontal'], color = CIstats.at['significant?','250ms_frontal'])
        
             
            if show == 1:
                imagename = fiberTypes[0]+'_'+fiberTypes[1]+' sensory-frontal '+cellType+'  '+opsinConfig
                imagepath = Path(imageloc)
                
                plt.savefig(imagepath / (imagename + '.eps'), format='eps', dpi=1200)
        
                
            
            
            plt.figure(figsize=(3.5,5))
            names = np.asarray([50,100,250])
            values = np.asarray([CIstats.at['mean','50ms_sensory'],CIstats.at['mean','100ms_sensory'],CIstats.at['mean','250ms_sensory']])
            linevalues = [1,1,1]
            plt.ylim((0.3,2.6))
            plt.xlim((0,300))
            plt.plot(names,values,'darkorange')
            yerrUpper = np.asarray([CIstats.at['upper bound','50ms_sensory'],CIstats.at['upper bound','100ms_sensory'],CIstats.at['upper bound','250ms_sensory']])
            yerrLower = np.asarray([CIstats.at['lower bound','50ms_sensory'],CIstats.at['lower bound','100ms_sensory'],CIstats.at['lower bound','250ms_sensory']])
            flat_yerrUpper = yerrUpper.flatten()
            flat_yerrLower = yerrLower.flatten()
            plt.fill_between(names, flat_yerrUpper, flat_yerrLower,alpha=0.5,interpolate=True,color='navajowhite')
            if 'A1' in fiberTypes and 'V1' in fiberTypes:
                plt.title(fiberTypes[0]+'_'+fiberTypes[1]+' visual-auditory '+cellType+' both opsin configurations')   
            else:
                plt.title(fiberTypes[0]+'_'+fiberTypes[1]+' frontal-sensory '+cellType+'  '+opsinConfig)   
            plt.plot(names,linevalues,'k--',alpha=0.7)
            plt.text(205, 2.3, 'n = '+str(len(iRatios['50ms_sensory'])), fontsize=14)
            if ratiodf.equals(pairedpeakRatio):
                plt.text(205, 2, 'peak', fontsize=14)
            else:
                plt.text(205, 2, 'charge transfer', fontsize=14)
            plt.show()
            
                    
               
            for cell in list(iRatios.index):
                names = np.asarray([50,100,250])
                values = np.asarray([iRatios.at[cell,'50ms_sensory'],iRatios.at[cell,'100ms_sensory'],iRatios.at[cell,'250ms_sensory']])
                linevalues = [1,1,1]
                plt.ylim((0.3,2.6))
                plt.xlim((0,300))
                if len(values) - sum(np.isnan(values)) > 1:
                    plt.plot(names,values,'lightgrey',linewidth=1,alpha=0.5)
                elif len(values) - sum(np.isnan(values)) == 1:
                    plt.plot(names,values,'lightgrey',alpha=0.5, marker = '.')
                plt.show()
                
            plt.text(45, 2.8, "%.3f" % CIstats.at['one sample t-test p val','50ms_sensory'], color = CIstats.at['significant?','50ms_sensory'])
            plt.text(90, 2.8, "%.3f" % CIstats.at['one sample t-test p val','100ms_sensory'], color = CIstats.at['significant?','100ms_sensory'])
            plt.text(230, 2.8, "%.3f" % CIstats.at['one sample t-test p val','250ms_sensory'], color = CIstats.at['significant?','250ms_sensory'])   
             
            if show == 1:
                imagename = fiberTypes[0]+'_'+fiberTypes[1]+' frontal-sensory '+cellType+'  '+opsinConfig
                imagepath = Path(imageloc)
                
                plt.savefig(imagepath / (imagename + '.eps'), format='eps', dpi=1200)
                    

    return    opsinSwapRatios, nonSwapRatios 
 

#%%
   
def IPSCintegralanalysis(fiberTypes, cellType, delay1, delay2, delay3, delay4, opsinSwapList, confidence, oneMapCells, show, imageloc, complete):

    import tkinter
    from tkinter.filedialog import askopenfilename
    import pickle

    delayList = [delay1,delay2,delay3,delay4]
    
    from pathlib import Path
    savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\IPSC")
    
    
    # make a list with all folder names including cellType:
    import os
    allnames = os.listdir(savedLoc)
    selectednames = [x for x in allnames if cellType in x]
    
    
    import pandas as pd
    import numpy as np
    frontalsensoryData = pd.DataFrame()
    sensoryfrontalData = pd.DataFrame()
    coincidentData = pd.DataFrame()

    
    integralData = pd.DataFrame({'cell ID':[*selectednames]}).set_index('cell ID')
    
    integralData['0ms_frontal single']=""
    integralData['0ms_frontal paired']=""
    integralData['0ms_sensory single']=""
    integralData['0ms_sensory paired']=""
    integralData['50ms_frontal single']=""
    integralData['50ms_frontal paired']=""
    integralData['50ms_sensory single']=""
    integralData['50ms_sensory paired']=""
    integralData['100ms_frontal single']=""
    integralData['100ms_frontal paired']=""
    integralData['100ms_sensory single']=""
    integralData['100ms_sensory paired']=""
    integralData['250ms_frontal single']=""
    integralData['250ms_frontal paired']=""
    integralData['250ms_sensory single']=""
    integralData['250ms_sensory paired']=""    
    
    for i in selectednames:
        print('processing...'+str(i)) 
        # point at data file to view
        cellPath = savedLoc / i
        workspacedf = pd.DataFrame()
        
       
        for file in os.listdir(cellPath):      
            for delay in delayList:
                if '_'+str(delay)+'ms' in file:
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    for k in loadedData.keys():
                        if '_data' in k:
                            workspacedf[str(delay)+'_'+str(k)] = loadedData[k]
                           

                    
        # this is where we MANUALLY change which pulse stimulates which fiber pop!!!
        
        for delay in delayList:        
            if delay == 0:
                try:
                    if i in opsinSwapList:
                        
                        coincidentData['actualCoincident'] = workspacedf[str(delay)+'_'+'paired pulse map_data']
                        coincidentData['arithmeticSum'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf[str(delay)+'_'+'pulse 1 map_data']
                    
                    if i not in opsinSwapList: # same as above if in opsinSwapList
                        
                       coincidentData['actualCoincident'] = workspacedf[str(delay)+'_'+'paired pulse map_data']
                       coincidentData['arithmeticSum'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf[str(delay)+'_'+'pulse 1 map_data']
                        
                       

                    #integrals for IPSC analysis (charge transfer)
                    intCoincidentActual = sum(coincidentData['actualCoincident'][1000:3000])
                    intCoincidentSum = sum(coincidentData['arithmeticSum'][1000:3000])
                    
                    integralData.at[str(i),str(delay)+'ms_sensory single'] = intCoincidentSum
                    integralData.at[str(i),str(delay)+'ms_sensory paired'] = intCoincidentActual
                    integralData.at[str(i),str(delay)+'ms_frontal single'] = intCoincidentSum
                    integralData.at[str(i),str(delay)+'ms_frontal paired'] = intCoincidentActual
                    
                    
                    
                except:
                    
                    #integrals for IPSC analysis (charge transfer)
                    print('missing delay points detected in '+str(i))
                    integralData.at[str(i),str(delay)+'ms_sensory single'] = np.nan
                    integralData.at[str(i),str(delay)+'ms_sensory paired'] = np.nan
                    integralData.at[str(i),str(delay)+'ms_frontal single'] = np.nan
                    integralData.at[str(i),str(delay)+'ms_frontal paired'] = np.nan
                    
            else:   
                try:
                    if i in opsinSwapList:
                   
                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_swap_data'] - workspacedf[str(delay)+'_'+'pulse 2 map_data']              
                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 1 map_data']

                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_data'] - workspacedf[str(delay)+'_'+'pulse 1 map_data']              
                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 2 map_data']




                    if i not in opsinSwapList:
                        
                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_swap_data'] - workspacedf[str(delay)+'_'+'pulse 2 map_data']              
                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 1 map_data']

                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_data'] - workspacedf[str(delay)+'_'+'pulse 1 map_data']              
                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 2 map_data']
                        
                        
                
                    
                    #integrals for IPSC analysis (charge transfer)
                    intFrontalActual = sum(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'][1000+(delay*10):3000+(delay*10)] -
                                                              np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'][990+(delay*10):999+(delay*10)]))
                    intFrontalSum = sum(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'][1000:3000] -
                                                           np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'][990:999]))
                    intSensoryActual = sum(frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'][1000+(delay*10):3000+(delay*10)] - 
                                                              np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'][990+(delay*10):999+(delay*10)]))
                    intSensorySum = sum(frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'][1000:3000] -
                                                           np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'][990:999]))
                    
                    integralData.at[str(i),str(delay)+'ms_sensory single'] = intSensorySum
                    integralData.at[str(i),str(delay)+'ms_sensory paired'] = intSensoryActual
                    integralData.at[str(i),str(delay)+'ms_frontal single'] = intFrontalSum
                    integralData.at[str(i),str(delay)+'ms_frontal paired'] = intFrontalActual
                
                
                
                except:
                    
                    print('missing delay points detected in '+str(i))

                    integralData.at[str(i),str(delay)+'ms_sensory single'] = np.nan
                    integralData.at[str(i),str(delay)+'ms_sensory paired'] = np.nan
                    integralData.at[str(i),str(delay)+'ms_frontal single'] = np.nan
                    integralData.at[str(i),str(delay)+'ms_frontal paired'] = np.nan
    
    
    #get ratios
    pairedintRatio = pd.DataFrame(index=integralData.index)
    
    pairedintRatio['0ms_frontal']=""
    pairedintRatio['0ms_sensory']=""
    pairedintRatio['50ms_frontal']=""
    pairedintRatio['50ms_sensory']=""
    pairedintRatio['100ms_frontal']=""
    pairedintRatio['100ms_sensory']=""
    pairedintRatio['250ms_frontal']=""
    pairedintRatio['250ms_sensory']=""
    
    for iIndex in selectednames:
        pairedintRatio.at[str(iIndex),'0ms_frontal']= integralData.at[str(iIndex),'0ms_frontal paired'] / integralData.at[str(iIndex),'0ms_frontal single']
        pairedintRatio.at[str(iIndex),'0ms_sensory']= integralData.at[str(iIndex),'0ms_sensory paired'] / integralData.at[str(iIndex),'0ms_sensory single']
        pairedintRatio.at[str(iIndex),'50ms_frontal']= integralData.at[str(iIndex),'50ms_frontal paired'] / integralData.at[str(iIndex),'50ms_frontal single']
        pairedintRatio.at[str(iIndex),'50ms_sensory']= integralData.at[str(iIndex),'50ms_sensory paired'] / integralData.at[str(iIndex),'50ms_sensory single']
        pairedintRatio.at[str(iIndex),'100ms_frontal']= integralData.at[str(iIndex),'100ms_frontal paired'] / integralData.at[str(iIndex),'100ms_frontal single']
        pairedintRatio.at[str(iIndex),'100ms_sensory']= integralData.at[str(iIndex),'100ms_sensory paired'] / integralData.at[str(iIndex),'100ms_sensory single']
        pairedintRatio.at[str(iIndex),'250ms_frontal']= integralData.at[str(iIndex),'250ms_frontal paired'] / integralData.at[str(iIndex),'250ms_frontal single']
        pairedintRatio.at[str(iIndex),'250ms_sensory']= integralData.at[str(iIndex),'250ms_sensory paired'] / integralData.at[str(iIndex),'250ms_sensory single']
    
        
    
    #mouse averaging and plotting
    for ratiodf in [pairedintRatio]:
    
    
        ratiodf.index = ratiodf.index.map(lambda x: str(x)[:-9])
        workspaceMousedf = ratiodf.copy()
        workspaceMousedf = workspaceMousedf.astype(float)
        strippedID = []
        for i in selectednames:
            strippedID.append(i[0:-9])
        workspaceMousedf['stripped Names']=strippedID
        grp_mouse = workspaceMousedf.groupby(['stripped Names'])
        pairedMouseRatio = grp_mouse.mean()
        

 
        
        opsinSwapMice = list(map(lambda x: str(x)[:-9],opsinSwapList))
        opsinSwapRatios = pairedMouseRatio[pairedMouseRatio.index.isin(opsinSwapMice) == True]
        nonSwapRatios = pairedMouseRatio[pairedMouseRatio.index.isin(opsinSwapMice) == False]
        if 'A1' in fiberTypes and 'V1' in fiberTypes:
            nonSwapRatios = pairedMouseRatio.copy()
        
        
        if complete == 1:
            nonSwapRatios = nonSwapRatios.dropna()
            opsinSwapRatios = opsinSwapRatios.dropna()
      
        
        import numpy as np      
        import scipy.stats
        
        
        nameList = ['opsin swap','default']
        for name, iRatios in enumerate([opsinSwapRatios, nonSwapRatios]):     
            
            if len(iRatios) == 0:
                continue
            
            opsinConfig = nameList[name]
            
            
            #get CI stats
            CIstats = pd.DataFrame(index=['95% CI','mean','upper bound','lower bound'])
            
            CIstats['0ms_frontal']=""
            CIstats['0ms_sensory']=""
            CIstats['50ms_frontal']=""
            CIstats['50ms_sensory']=""
            CIstats['100ms_frontal']=""
            CIstats['100ms_sensory']=""
            CIstats['250ms_frontal']=""
            CIstats['250ms_sensory']=""
        
            import scipy.stats as stats
        
            for col in list(CIstats.columns): 
                a = iRatios[col].values
                float_arr = np.vstack(a[:]).astype(np.float)
                # n = len(float_arr)
                n = np.count_nonzero(~np.isnan(float_arr))
                m = iRatios[col].mean()
                se = scipy.stats.sem(float_arr, nan_policy = 'omit')
                h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
                #h = np.nanstd(float_arr) for standard dev
                CIstats.at['95% CI',col]= h
                CIstats.at['mean',col]= m
                CIstats.at['upper bound',col]= m + h     
                CIstats.at['lower bound',col]= m - h
                CIstats.at['one sample t-test p val',col] = stats.ttest_1samp(a,1.0,nan_policy='omit')[1]
                if CIstats.at['one sample t-test p val',col] < 0.05:
                    CIstats.at['significant?',col] = 'red'
                else:
                    CIstats.at['significant?',col] = 'black'
                    
            from matplotlib import pyplot as plt
            
            plt.figure(figsize=(3.5,5))
            names = np.asarray([0,50,100,250])
            values = np.asarray([CIstats.at['mean','0ms_frontal'], CIstats.at['mean','50ms_frontal'],CIstats.at['mean','100ms_frontal'],CIstats.at['mean','250ms_frontal']])
            linevalues = [1,1,1,1]
            plt.ylim((0.3,2.6))
            plt.xlim((0,300))
            plt.plot(names,values,'darkorange')
            yerrUpper = np.asarray([CIstats.at['upper bound','0ms_frontal'],CIstats.at['upper bound','50ms_frontal'],CIstats.at['upper bound','100ms_frontal'],CIstats.at['upper bound','250ms_frontal']])
            yerrLower = np.asarray([CIstats.at['lower bound','0ms_frontal'],CIstats.at['lower bound','50ms_frontal'],CIstats.at['lower bound','100ms_frontal'],CIstats.at['lower bound','250ms_frontal']])
            flat_yerrUpper = yerrUpper.flatten()
            flat_yerrLower = yerrLower.flatten()
            plt.fill_between(names, flat_yerrUpper, flat_yerrLower,alpha=0.5,interpolate=True,color='navajowhite')
            if 'A1' in fiberTypes and 'V1' in fiberTypes:
                plt.title(fiberTypes[0]+'_'+fiberTypes[1]+' auditory-visual '+cellType+' both opsin configurations')  
            else: 
                plt.title(fiberTypes[0]+'_'+fiberTypes[1]+' sensory-frontal '+cellType+'  '+opsinConfig)   
            plt.plot(names,linevalues,'k--',alpha=0.7)
            plt.text(205, 2.3, 'n = '+str(len(iRatios['50ms_frontal'])), fontsize=14)
            plt.text(205, 2, 'charge transfer', fontsize=14)
         
            plt.show()
                
         
            for cell in list(iRatios.index):
                names = np.asarray([0,50,100,250])
                values = np.asarray([iRatios.at[cell,'0ms_frontal'],iRatios.at[cell,'50ms_frontal'],iRatios.at[cell,'100ms_frontal'],iRatios.at[cell,'250ms_frontal']])
                linevalues = [1,1,1]
                plt.ylim((0.3,2.6))
                plt.xlim((0,300))
                if len(values) - sum(np.isnan(values)) > 1:
                    plt.plot(names,values,'lightgrey',linewidth=1,alpha=0.5)
                elif len(values) - sum(np.isnan(values)) == 1:
                    plt.plot(names,values,'lightgrey',alpha=0.5, marker = '.')
                plt.show()
            
            plt.text(5, 2.8, "%.3f" % CIstats.at['one sample t-test p val','0ms_frontal'], color = CIstats.at['significant?','0ms_frontal'])
            plt.text(45, 2.8, "%.3f" % CIstats.at['one sample t-test p val','50ms_frontal'], color = CIstats.at['significant?','50ms_frontal'])
            plt.text(90, 2.8, "%.3f" % CIstats.at['one sample t-test p val','100ms_frontal'], color = CIstats.at['significant?','100ms_frontal'])
            plt.text(230, 2.8, "%.3f" % CIstats.at['one sample t-test p val','250ms_frontal'], color = CIstats.at['significant?','250ms_frontal'])
        
             
            if show == 1:
                imagename = fiberTypes[0]+'_'+fiberTypes[1]+' sensory-frontal '+cellType+'  '+opsinConfig
                imagepath = Path(imageloc)
                
                plt.savefig(imagepath / (imagename + '.eps'), format='eps', dpi=1200)
        
                
            
            
            plt.figure(figsize=(3.5,5))
            names = np.asarray([0,50,100,250])
            values = np.asarray([CIstats.at['mean','0ms_sensory'],CIstats.at['mean','50ms_sensory'],CIstats.at['mean','100ms_sensory'],CIstats.at['mean','250ms_sensory']])
            linevalues = [1,1,1,1]
            plt.ylim((0.3,2.6))
            plt.xlim((0,300))
            plt.plot(names,values,'darkorange')
            yerrUpper = np.asarray([CIstats.at['upper bound','0ms_sensory'],CIstats.at['upper bound','50ms_sensory'],CIstats.at['upper bound','100ms_sensory'],CIstats.at['upper bound','250ms_sensory']])
            yerrLower = np.asarray([CIstats.at['lower bound','0ms_sensory'],CIstats.at['lower bound','50ms_sensory'],CIstats.at['lower bound','100ms_sensory'],CIstats.at['lower bound','250ms_sensory']])
            flat_yerrUpper = yerrUpper.flatten()
            flat_yerrLower = yerrLower.flatten()
            plt.fill_between(names, flat_yerrUpper, flat_yerrLower,alpha=0.5,interpolate=True,color='navajowhite')
            if 'A1' in fiberTypes and 'V1' in fiberTypes:
                plt.title(fiberTypes[0]+'_'+fiberTypes[1]+' visual-auditory '+cellType+' both opsin configurations')   
            else:
                plt.title(fiberTypes[0]+'_'+fiberTypes[1]+' frontal-sensory '+cellType+'  '+opsinConfig)   
            plt.plot(names,linevalues,'k--',alpha=0.7)
            plt.text(205, 2.3, 'n = '+str(len(iRatios['50ms_sensory'])), fontsize=14)

            plt.text(205, 2, 'charge transfer', fontsize=14)

            plt.show()
            
                    
               
            for cell in list(iRatios.index):
                names = np.asarray([0,50,100,250])
                values = np.asarray([iRatios.at[cell,'0ms_sensory'],iRatios.at[cell,'50ms_sensory'],iRatios.at[cell,'100ms_sensory'],iRatios.at[cell,'250ms_sensory']])
                linevalues = [1,1,1,1]
                plt.ylim((0.3,2.6))
                plt.xlim((0,300))
                if len(values) - sum(np.isnan(values)) > 1:
                    plt.plot(names,values,'lightgrey',linewidth=1,alpha=0.5)
                elif len(values) - sum(np.isnan(values)) == 1:
                    plt.plot(names,values,'lightgrey',alpha=0.5, marker = '.')
                plt.show()
                
            plt.text(5, 2.8, "%.3f" % CIstats.at['one sample t-test p val','0ms_sensory'], color = CIstats.at['significant?','0ms_sensory'])                
            plt.text(45, 2.8, "%.3f" % CIstats.at['one sample t-test p val','50ms_sensory'], color = CIstats.at['significant?','50ms_sensory'])
            plt.text(90, 2.8, "%.3f" % CIstats.at['one sample t-test p val','100ms_sensory'], color = CIstats.at['significant?','100ms_sensory'])
            plt.text(230, 2.8, "%.3f" % CIstats.at['one sample t-test p val','250ms_sensory'], color = CIstats.at['significant?','250ms_sensory'])   
             
            if show == 1:
                imagename = fiberTypes[0]+'_'+fiberTypes[1]+' frontal-sensory '+cellType+'  '+opsinConfig
                imagepath = Path(imageloc)
                
                plt.savefig(imagepath / (imagename + '.eps'), format='eps', dpi=1200)
                    

    return    opsinSwapRatios, nonSwapRatios 
 

#%%
def singleCellTrace(cell, fiberTypes, delay1, delay2, delay3, delay4, opsinSwapList, oneMapCells, order):
    
    import tkinter
    from tkinter.filedialog import askopenfilename
    import pickle

    delayList = [delay1,delay2,delay3,delay4]
    
    from pathlib import Path
    
    if 'A1' in fiberTypes and 'V1' in fiberTypes:
        savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration A1_V1")
    if 'A1' in fiberTypes and 'ACC' in fiberTypes:
        savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration A1_ACC")
    if 'V1' in fiberTypes and 'ACC' in fiberTypes:
        savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration V1_ACC")
        
    # make a list with all folder names including cellType:
    import os
    
    import pandas as pd
    import numpy as np
    frontalsensoryData = pd.DataFrame()
    sensoryfrontalData = pd.DataFrame()
    coincidentData = pd.DataFrame()


    i = cell
    print('processing...'+str(i)) 
    # point at data file to view
    cellPath = savedLoc / i
    workspacedf = pd.DataFrame()
    
    
    if i in oneMapCells:
        
      for file in os.listdir(cellPath):      
            for delay in delayList:
                if '_'+str(delay)+'ms_blue' in file and 'bluered' not in file:
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    for k in loadedData.keys():
                        if '_data' in k:
                            workspacedf[str(delay)+'_'+'pulse 1 map_data'] = loadedData[k] 
                            
                if '_'+str(delay)+'ms_bluered' in file:
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    for k in loadedData.keys():
                        if '_data' in k:
                            workspacedf[str(delay)+'_'+'paired pulse map_data'] = loadedData[k] 
                            
                if '_'+str(delay)+'ms_red' in file and 'redblue' not in file:
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    for k in loadedData.keys():
                        if '_data' in k:
                            workspacedf[str(delay)+'_'+'pulse 2 map_data'] = loadedData[k]          
                            
                if '_'+str(delay)+'ms_redblue' in file:
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    for k in loadedData.keys():
                        if '_data' in k:
                            workspacedf[str(delay)+'_'+'paired pulse map_swap_data'] = loadedData[k] 
                            
    else:
        
        for file in os.listdir(cellPath):      
            for delay in delayList:
                if '_'+str(delay)+'ms' in file:
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    for k in loadedData.keys():
                        if '_data' in k:
                            workspacedf[str(delay)+'_'+str(k)] = loadedData[k]
                           

                    
    # this is where we MANUALLY change which pulse stimulates which fiber pop!!!
    
    for delay in delayList:       
        
        if delay == 0:
            
            coincidentData['actualCoincident'] = np.array(workspacedf[str(delay)+'_'+'paired pulse map_data'])
            coincidentData['arithmeticSum'] = np.array(workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf[str(delay)+'_'+'pulse 1 map_data'])
            
            if i in opsinSwapList:
                
                fiber1 = 'sensory'
                color1 = 'blue'
                fiber2 = 'frontal'
                color2 = 'red'    
              
            else:
                
                fiber1 = 'frontal'
                color1 = 'blue'
                fiber2 = 'sensory'
                color2 = 'red'
                   
                   
            from matplotlib import pyplot as plt
            
            plt.figure()
            plt.plot(workspacedf[str(delay)+'_'+'pulse 1 map_data'], label = fiber1+' '+str(delay), color = color1)
            plt.xlim(900,4100)
            plt.ylim(-3,17)
            plt.legend()
              
            plt.figure()
            plt.plot(workspacedf[str(delay)+'_'+'pulse 2 map_data'], label = fiber2+' '+str(delay), color = color2)
            plt.xlim(900,4100)
            plt.ylim(-3,17)
            plt.legend()
              
            plt.figure()
            plt.plot(coincidentData['arithmeticSum'], color = 'black', label='arithmetic sum')
            plt.plot(coincidentData['actualCoincident'], color = 'fuchsia', label = 'recorded')
            plt.xlim(900,4100)
            plt.ylim(-3,17)
            plt.legend()
            
               

          
        else:   
            try:
                if i in opsinSwapList:
               
                    frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_swap_data']                        
                    workspacedf['zeros'] = np.zeros(len(workspacedf))
                    workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 1 map_data'][1000:2000]
                    frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf['zeros']

                    sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_data']                        
                    workspacedf['zeros'] = np.zeros(len(workspacedf))
                    workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 2 map_data'][1000:2000]
                    sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 1 map_data'] + workspacedf['zeros']


                if i not in opsinSwapList:
                    
                    frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_data']                        
                    workspacedf['zeros'] = np.zeros(len(workspacedf))
                    workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 2 map_data'][1000:2000]
                    frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 1 map_data'] + workspacedf['zeros']

                    sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_swap_data']                        
                    workspacedf['zeros'] = np.zeros(len(workspacedf))
                    workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 1 map_data'][1000:2000]
                    sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf['zeros']
                        

                    
                from matplotlib import pyplot as plt

                
                if order == 'FS':
                    
                    plt.figure()
                    plt.plot(frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'], color = 'black', label='arithmetic sum')
                    plt.plot(frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'], color = 'fuchsia', label = 'recorded')
                    plt.xlim(900,4100)
                    plt.ylim(-3,17)
                    plt.legend()
                
                if order == 'SF': 
                    
                    plt.figure()
                    plt.plot(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'], color = 'black', label='arithmetic sum')
                    plt.plot(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'], color = 'fuchsia', label = 'recorded')
                    plt.xlim(900,4100)
                    plt.ylim(-3,17)
                    plt.legend()
                
            
            except:
                print('missing delay points detected in '+str(i))
                frontalsensoryData['delay '+str(delay)+'ms_sensory paired pulse'] = np.nan
                frontalsensoryData['delay '+str(delay)+'ms_sensory single pulse'] = np.nan
                
                sensoryfrontalData['delay '+str(delay)+'ms_frontal paired pulse'] = np.nan
                sensoryfrontalData['delay '+str(delay)+'ms_frontal single pulse'] = np.nan


    return


#%%

def plottrace(fiberTypes, cellType, IPSC, delay1, delay2, delay3, delay4, opsinSwapList, confidence, oneMapCells, error, order, show, imageloc, redblue, opsinConfig, delayBase):
    
    
    import tkinter
    from tkinter.filedialog import askopenfilename
    import pickle

    delayList = [delay1,delay2,delay3,delay4]
    
    from pathlib import Path

    if 'A1' in fiberTypes and 'V1' in fiberTypes:
        savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration A1_V1")
    if 'A1' in fiberTypes and 'ACC' in fiberTypes:
        savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration A1_ACC")
    if 'V1' in fiberTypes and 'ACC' in fiberTypes:
        savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration V1_ACC")
    
    if IPSC == 1:
        savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\IPSC")
        
    # make a list with all folder names including cellType:
    import os
    allnames = os.listdir(savedLoc)
    selectednames = [x for x in allnames if cellType in x]
    
    
    import pandas as pd
    import numpy as np
    frontalsensoryData = pd.DataFrame()
    sensoryfrontalData = pd.DataFrame()
    coincidentData = pd.DataFrame()
    
    coincidenttraceData = pd.DataFrame()
    delay2FStraceData = pd.DataFrame()
    delay2SFtraceData = pd.DataFrame()    
    delay3FStraceData = pd.DataFrame()
    delay3SFtraceData = pd.DataFrame()
    delay4FStraceData = pd.DataFrame()
    delay4SFtraceData = pd.DataFrame()
    
    justBlue = pd.DataFrame()
    justRed = pd.DataFrame()
    
    
    for i in selectednames:
        
        if opsinConfig == 'default':
            if i in opsinSwapList:
                continue
        if opsinConfig == 'swap':
            if i not in opsinSwapList:
                continue
            
        print('processing...'+str(i)) 
        # point at data file to view
        cellPath = savedLoc / i
        workspacedf = pd.DataFrame()
        
        if i in oneMapCells:
            
          for file in os.listdir(cellPath):      
                for delay in delayList:
                    if '_'+str(delay)+'ms_blue' in file and 'bluered' not in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                workspacedf[str(delay)+'_'+'pulse 1 map_data'] = loadedData[k]
                                justBlue[i] = loadedData[k]
                                
                    if '_'+str(delay)+'ms_bluered' in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                workspacedf[str(delay)+'_'+'paired pulse map_data'] = loadedData[k] 
                                
                    if '_'+str(delay)+'ms_red' in file and 'redblue' not in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                workspacedf[str(delay)+'_'+'pulse 2 map_data'] = loadedData[k]          
                                justRed[i] = loadedData[k]
                                
                    if '_'+str(delay)+'ms_redblue' in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                workspacedf[str(delay)+'_'+'paired pulse map_swap_data'] = loadedData[k] 
                                
                        
        else:
            
            for file in os.listdir(cellPath):      
                for delay in delayList:
                    if '_'+str(delay)+'ms' in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                workspacedf[str(delay)+'_'+str(k)] = loadedData[k]
                                if '_'+str(delay)+'ms_blue' in file and 'bluered' not in file:
                                    justBlue[i] = loadedData[k]
                                if '_'+str(delay)+'ms_red' in file and 'redblue' not in file:
                                    justRed[i] = loadedData[k]
                        
        # this is where we MANUALLY change which pulse stimulates which fiber pop!!!
        
        for delay in delayList:        
            try:
                if delay == 0:
                    if i in opsinSwapList:
                            
                        coincidenttraceData[str(i)+'_'+str(delay)+'_actual'] = workspacedf[str(delay)+'_'+'paired pulse map_data']
                        coincidenttraceData[str(i)+'_'+str(delay)+'_sum'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf[str(delay)+'_'+'pulse 1 map_data']
                    
                    if i not in opsinSwapList: # same as above if in opsinSwapList
                        
                        coincidenttraceData[str(i)+'_'+str(delay)+'_actual'] = workspacedf[str(delay)+'_'+'paired pulse map_data']
                        coincidenttraceData[str(i)+'_'+str(delay)+'_sum'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf[str(delay)+'_'+'pulse 1 map_data']
                        
                       
    
                    
                else:   
    
                    if i in opsinSwapList:
                        if delay == 50:
                            delay2FStraceData[str(i)+'_'+str(delay)+'_actual'] = workspacedf[str(delay)+'_'+'paired pulse map_swap_data']                        
                            workspacedf['zeros'] = np.zeros(len(workspacedf))
                            workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 1 map_data'][1000:2000]
                            delay2FStraceData[str(i)+'_'+str(delay)+'ms_sum'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf['zeros']
    
                            delay2SFtraceData['delay '+str(delay)+'ms_frontal paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_data']                        
                            workspacedf['zeros'] = np.zeros(len(workspacedf))
                            workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 2 map_data'][1000:2000]
                            delay2SFtraceData[str(i)+'_'+str(delay)+'ms_sum'] = workspacedf[str(delay)+'_'+'pulse 1 map_data'] + workspacedf['zeros']
    
                        if delay == 100:
                            delay3FStraceData[str(i)+'_'+str(delay)+'_actual'] = workspacedf[str(delay)+'_'+'paired pulse map_swap_data']                        
                            workspacedf['zeros'] = np.zeros(len(workspacedf))
                            workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 1 map_data'][1000:2000]
                            delay3FStraceData[str(i)+'_'+str(delay)+'ms_sum'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf['zeros']
    
                            delay3SFtraceData['delay '+str(delay)+'ms_frontal paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_data']                        
                            workspacedf['zeros'] = np.zeros(len(workspacedf))
                            workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 2 map_data'][1000:2000]
                            delay3SFtraceData[str(i)+'_'+str(delay)+'ms_sum'] = workspacedf[str(delay)+'_'+'pulse 1 map_data'] + workspacedf['zeros']
    
                        if delay == 250:
                            delay4FStraceData[str(i)+'_'+str(delay)+'_actual'] = workspacedf[str(delay)+'_'+'paired pulse map_swap_data']                        
                            workspacedf['zeros'] = np.zeros(len(workspacedf))
                            workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 1 map_data'][1000:2000]
                            delay4FStraceData[str(i)+'_'+str(delay)+'ms_sum'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf['zeros']
    
                            delay4SFtraceData[str(i)+'_'+str(delay)+'_actual'] = workspacedf[str(delay)+'_'+'paired pulse map_data']                        
                            workspacedf['zeros'] = np.zeros(len(workspacedf))
                            workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 2 map_data'][1000:2000]
                            delay4SFtraceData[str(i)+'_'+str(delay)+'ms_sum'] = workspacedf[str(delay)+'_'+'pulse 1 map_data'] + workspacedf['zeros']
    
    
                    if i not in opsinSwapList:
                        if delay == 50:
                            delay2FStraceData[str(i)+'_'+str(delay)+'ms_actual'] = workspacedf[str(delay)+'_'+'paired pulse map_data']                        
                            workspacedf['zeros'] = np.zeros(len(workspacedf))
                            workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 2 map_data'][1000:2000]
                            delay2FStraceData[str(i)+'_'+str(delay)+'ms_sum'] = workspacedf[str(delay)+'_'+'pulse 1 map_data'] + workspacedf['zeros']
    
                            delay2SFtraceData[str(i)+'_'+str(delay)+'ms_actual'] = workspacedf[str(delay)+'_'+'paired pulse map_swap_data']                        
                            workspacedf['zeros'] = np.zeros(len(workspacedf))
                            workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 1 map_data'][1000:2000]
                            delay2SFtraceData[str(i)+'_'+str(delay)+'ms_sum'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf['zeros']
                            
                        if delay == 100:
                            delay3FStraceData[str(i)+'_'+str(delay)+'ms_actual'] = workspacedf[str(delay)+'_'+'paired pulse map_data']                        
                            workspacedf['zeros'] = np.zeros(len(workspacedf))
                            workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 2 map_data'][1000:2000]
                            delay3FStraceData[str(i)+'_'+str(delay)+'ms_sum'] = workspacedf[str(delay)+'_'+'pulse 1 map_data'] + workspacedf['zeros']
    
                            delay3SFtraceData[str(i)+'_'+str(delay)+'ms_actual'] = workspacedf[str(delay)+'_'+'paired pulse map_swap_data']                        
                            workspacedf['zeros'] = np.zeros(len(workspacedf))
                            workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 1 map_data'][1000:2000]
                            delay3SFtraceData[str(i)+'_'+str(delay)+'ms_sum'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf['zeros']
    
                        if delay == 250:
                            delay4FStraceData[str(i)+'_'+str(delay)+'ms_actual'] = workspacedf[str(delay)+'_'+'paired pulse map_data']                        
                            workspacedf['zeros'] = np.zeros(len(workspacedf))
                            workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 2 map_data'][1000:2000]
                            delay4FStraceData[str(i)+'_'+str(delay)+'ms_sum'] = workspacedf[str(delay)+'_'+'pulse 1 map_data'] + workspacedf['zeros']
    
                            delay4SFtraceData[str(i)+'_'+str(delay)+'ms_actual'] = workspacedf[str(delay)+'_'+'paired pulse map_swap_data']                        
                            workspacedf['zeros'] = np.zeros(len(workspacedf))
                            workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 1 map_data'][1000:2000]
                            delay4SFtraceData[str(i)+'_'+str(delay)+'ms_sum'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf['zeros']
                           

                                                    

            
            except:
                print('missing delay points detected in '+str(i))
                if delay == 0:
                    coincidenttraceData[str(i)+'_'+str(delay)+'ms_actual'] = np.nan
                    coincidenttraceData[str(i)+'_'+str(delay)+'ms_sum'] = np.nan
                    
                    coincidenttraceData[str(i)+'_'+str(delay)+'ms_actual'] = np.nan
                    coincidenttraceData[str(i)+'_'+str(delay)+'ms_sum'] = np.nan                    
                    
                if delay == 50:
                    delay2FStraceData[str(i)+'_'+str(delay)+'ms_actual'] = np.nan
                    delay2FStraceData[str(i)+'_'+str(delay)+'ms_sum'] = np.nan
                    
                    delay2SFtraceData[str(i)+'_'+str(delay)+'ms_actual'] = np.nan
                    delay2SFtraceData[str(i)+'_'+str(delay)+'ms_sum'] = np.nan
                        
                    
                if delay == 100:
                    delay3FStraceData[str(i)+'_'+str(delay)+'ms_actual'] = np.nan
                    delay3FStraceData[str(i)+'_'+str(delay)+'ms_sum'] = np.nan
                    
                    delay3SFtraceData[str(i)+'_'+str(delay)+'ms_actual'] = np.nan
                    delay3SFtraceData[str(i)+'_'+str(delay)+'ms_sum'] = np.nan
                        
                    
                if delay == 250:
                    delay4FStraceData[str(i)+'_'+str(delay)+'ms_actual'] = np.nan
                    delay4FStraceData[str(i)+'_'+str(delay)+'ms_sum'] = np.nan
                    
                    delay4SFtraceData[str(i)+'_'+str(delay)+'ms_actual'] = np.nan
                    delay4SFtraceData[str(i)+'_'+str(delay)+'ms_sum'] = np.nan


                     
    if order == 'both':
        orderList = [coincidenttraceData.astype(float), 
                       delay2FStraceData.astype(float), delay2SFtraceData.astype(float),
                       delay3FStraceData.astype(float), delay3SFtraceData.astype(float),
                       delay4FStraceData.astype(float), delay4SFtraceData.astype(float)]
    if order == 'FS':
        orderList = [coincidenttraceData.astype(float), 
                       delay2FStraceData.astype(float),
                       delay3FStraceData.astype(float), 
                       delay4FStraceData.astype(float)]        
    if order == 'SF':
        orderList = [coincidenttraceData.astype(float), 
                       delay2SFtraceData.astype(float),
                       delay3SFtraceData.astype(float),
                       delay4SFtraceData.astype(float)]

        
    #baselining
    if delayBase == 'delay':    
        for i in orderList:
            for column in i:
                if '_0' in column:
                    i[column] = i[column] - np.mean(i[column][995:1000])              
                if '_50ms' in column:
                    i[column] = i[column] - np.mean(i[column][1495:1500])
                if '_100ms' in column:
                    i[column] = i[column] - np.mean(i[column][1995:2000])        
                if '_250ms' in column:
                    i[column] = i[column] - np.mean(i[column][3495:3500])        
        
        
        
        
        
    if redblue == False:    
        for iEnum, delayTrace in enumerate(orderList):
            
            #mouse averaging 
            workspaceMousedf = delayTrace.copy().transpose()
            workspaceMousedf = workspaceMousedf.astype(float)
            workspaceMousedf['strippedID'] = ""
            for i in workspaceMousedf.index:
                workspaceMousedf.at[i,'strippedID'] = i[:i.find('cell')-1] + '_' + i[-3:]
            grp_mouse = workspaceMousedf.groupby(['strippedID'])
            ggg = grp_mouse.mean()
            
            sumData = pd.DataFrame()
            actualData = pd.DataFrame()
            
            for mouse in ggg.index:
                if mouse[-3:] == 'sum':
                    x = ggg.loc[mouse,list(ggg)]
                    sumData[mouse] = x[800:4500]

                        
                if mouse[-3:] == 'ual':
                    x = ggg.loc[mouse,list(ggg)]
                    actualData[mouse] = x[800:4500]

                        
            sumData = sumData.transpose()
            actualData = actualData.transpose()
            
    
            # this function ignores opsin swap, and only plots default 

            #get CI stats
            CIstats = pd.DataFrame(index=['95% CI','sem','mean','upper bound','lower bound'])
            
            from matplotlib import pyplot as plt
            import numpy as np
            import scipy.stats
            
            plt.figure()
            
            
            
            
            if error == 'pop':
                for ggg in [actualData, sumData]:
                    
                    for col in list(ggg.columns): 
                        a = ggg[col].values
                        float_arr = np.vstack(a[:]).astype(np.float)
                        n = len(float_arr)
                        m = ggg[col].mean()
                        se = scipy.stats.sem(float_arr, nan_policy = 'omit')
                        h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
                        #h = np.nanstd(float_arr) for standard dev
                        CIstats.at['95% CI',col]= h
                        CIstats.at['sem',col] = se
                        CIstats.at['mean',col]= m
                        if error == '95CI':
                            CIstats.at['upper bound',col]= m + h     
                            CIstats.at['lower bound',col]= m - h  
                        if error == 'sem':
                            CIstats.at['upper bound',col]= m + se     
                            CIstats.at['lower bound',col]= m - se  
                        if error == 'std':    
                            print("'haven't done that yet")
                            
                    from matplotlib import pyplot as plt
                    
                    for row in list(ggg.index.values): 
                        data2plot = np.asarray(ggg.loc[row])
                
                    
                        if ggg.equals(actualData) is True:
                            color = 'fuchsia'
                        if ggg.equals(sumData) is True:
                            plotColor = 'grey'                
                        
                        
                        plt.plot(data2plot,plotColor)
                        
                    
                    if ggg.equals(actualData) is True:
                        meanColor = 'red'
                    if ggg.equals(sumData) is True:
                        meanColor = 'black'        
                        
                    plt.plot(np.asarray(CIstats.loc['mean']),meanColor)
                    if ggg.equals(actualData) is True:
                        if iEnum == 0:
                            actualMean = np.asarray(CIstats.loc['mean'])
 
    
    
                plt.text(225, 2.3, 'n = '+str(len(ggg.index)), fontsize=14)
                plt.ylim(-2.5,15)
                plt.xlim(750,4500)
                plt.title(order)
                plt.show()



           
            else:
                for ggg in [sumData, actualData]:
                    for col in list(ggg.columns): 
                        a = ggg[col].values
                        float_arr = np.vstack(a[:]).astype(np.float)
                        n = len(float_arr)
                        m = ggg[col].mean()
                        se = scipy.stats.sem(float_arr, nan_policy = 'omit')
                        h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
                        #h = np.nanstd(float_arr) for standard dev
                        CIstats.at['95% CI',col]= h
                        CIstats.at['sem',col] = se
                        CIstats.at['mean',col]= m
                        if error == '95CI':
                            CIstats.at['upper bound',col]= m + h     
                            CIstats.at['lower bound',col]= m - h  
                        if error == 'sem':
                            CIstats.at['upper bound',col]= m + se     
                            CIstats.at['lower bound',col]= m - se  
                        if error == 'std':    
                            print("'haven't done that yet")
                            
                    from matplotlib import pyplot as plt
                    
                    
                    x = CIstats.transpose()
                    
                    if ggg.equals(actualData) is True:
                        plotColor = 'fuchsia'
                    if ggg.equals(sumData) is True:
                        plotColor = 'k--'
                        
                    
                    if any('_0_' in x for x in delayTrace.keys()):
                       data2plot = x['mean'][150:1000]
                       yerrTop = x['upper bound'][150:1000]
                       yerrBottom = x['lower bound'][150:1000]
                       names = np.asarray(list(x.index)[150:1000])
                    if any('_50ms_' in x for x in delayTrace.keys()):
                       data2plot = x['mean'][150:1500]
                       yerrTop = x['upper bound'][150:1500]
                       yerrBottom = x['lower bound'][150:1500]
                       names = np.asarray(list(x.index)[150:1500])
                    if any('_100ms_' in x for x in delayTrace.keys()):
                       data2plot = x['mean'][150:2000]
                       yerrTop = x['upper bound'][150:2000]
                       yerrBottom = x['lower bound'][150:2000]
                       names = np.asarray(list(x.index)[150:2000])
                    if any('_250ms_' in x for x in delayTrace.keys()):
                       data2plot = x['mean'][150:3500]
                       yerrTop = x['upper bound'][150:3500]
                       yerrBottom = x['lower bound'][150:3500]
                       names = np.asarray(list(x.index)[150:3500])
        
                
                    
                    plt.plot(data2plot,plotColor)
                    yerrUpper = np.asarray(yerrTop)
                    yerrLower = np.asarray(yerrBottom)
                    flat_yerrUpper = yerrUpper.flatten()
                    flat_yerrLower = yerrLower.flatten()
                    if ggg.equals(actualData) is True:
                        chosenColor = 'fuchsia'
                    if ggg.equals(sumData) is True:
                        chosenColor = 'black'
                    plt.fill_between(names, flat_yerrUpper, flat_yerrLower,alpha=0.3,interpolate=True,color = chosenColor)
            
                    plt.text(225, 2.3, 'n = '+str(len(ggg.index)), fontsize=14)
                    plt.ylim(-2.5,15)
                    plt.xlim(750,4500)
                    plt.title(order)
                    plt.show()
                    
                    if show == 1:
                        
                        if any('_0_' in x for x in delayTrace.keys()):
                            x = '0ms'
                        if any('_50ms_' in x for x in delayTrace.keys()):
                            x = '50ms'
                        if any('_100ms_' in x for x in delayTrace.keys()):
                            x = '100ms'
                        if any('_250ms_' in x for x in delayTrace.keys()):
                            x = '250ms'
                        
                        imagename = cellType+' '+order+' '+x+ ' '+fiberTypes[0]+'_'+fiberTypes[1]
                        imagepath = Path(imageloc)
                        
                        plt.savefig(imagepath / (imagename + '.png'), bbox_inches = "tight")  # may not work
                        plt.savefig(imagepath / (imagename + '.eps'), format='eps', dpi=1200)
                
                    
        
    from matplotlib import pyplot as plt
    import numpy as np
    import scipy.stats        
            
    # getting just red and blue
    if redblue == True:
        for iColor in [justBlue, justRed]:
            workspaceMousedf = iColor.copy().transpose()
            workspaceMousedf = workspaceMousedf.astype(float)
            workspaceMousedf['strippedID'] = ""
            for i in workspaceMousedf.index:
                workspaceMousedf.at[i,'strippedID'] = i[:i.find('cell')-1] + '_' + i[-3:]
            grp_mouse = workspaceMousedf.groupby(['strippedID'])
            ggg = grp_mouse.mean()
        
            
             #get CI stats
            CIstats = pd.DataFrame(index=['95% CI','sem','mean','upper bound','lower bound'])
            
            
            
            plt.figure()

            for col in list(ggg.columns): 
                a = ggg[col].values
                float_arr = np.vstack(a[:]).astype(np.float)
                n = len(float_arr)
                m = ggg[col].mean()
                se = scipy.stats.sem(float_arr, nan_policy = 'omit')
                h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
                #h = np.nanstd(float_arr) for standard dev
                CIstats.at['95% CI',col]= h
                CIstats.at['sem',col] = se
                CIstats.at['mean',col]= m
                if error == '95CI':
                    CIstats.at['upper bound',col]= float(m + h)     
                    CIstats.at['lower bound',col]= float(m - h)  
                if error == 'sem':
                    CIstats.at['upper bound',col]= float(m + se)    
                    CIstats.at['lower bound',col]= float(m - se)  
                if error == 'std':    
                    print("'haven't done that yet")
                    
            
            
            x = CIstats.transpose()
            

            plotColor = 'fuchsia'


            data2plot = x['mean'][950:3000]
            yerrTop = x['upper bound'][950:3000]
            yerrBottom = x['lower bound'][950:3000]
            names = np.asarray(list(x.index)[950:3000])
    
            
            plt.plot(data2plot,plotColor)
            yerrUpper = np.asarray(yerrTop)
            yerrLower = np.asarray(yerrBottom)
            flat_yerrUpper = yerrUpper.flatten()
            flat_yerrLower = yerrLower.flatten()

            chosenColor = 'fuchsia'

            plt.fill_between(names, flat_yerrUpper, flat_yerrLower,alpha=0.3,interpolate=True,color = chosenColor)
    
            plt.text(225, 2.3, 'n = '+str(len(ggg.index)), fontsize=14)
            plt.ylim(-2.5,15)
            plt.xlim(750,4500)
            
            if iColor.equals(justBlue):             
                imagename = 'frontal'+' '+fiberTypes[0]+'_'+fiberTypes[1]+' '+cellType
                plt.title('frontal')
                
                #blue is visual for V1-A1 integration
            if iColor.equals(justRed):
                imagename = 'sensory'+' '+fiberTypes[0]+'_'+fiberTypes[1]+' '+cellType
                plt.title('sensory')
                
            
            plt.show()
            

            if iColor.equals(justBlue):             
                imagename = 'frontal'+' '+fiberTypes[0]+'_'+fiberTypes[1]+' '+cellType
                #blue is visual for V1-A1 integration
            if iColor.equals(justRed):
                imagename = 'sensory'+' '+fiberTypes[0]+'_'+fiberTypes[1]+' '+cellType
                
            imagepath = Path(imageloc)
            
            plt.savefig(imagepath / (imagename + '.png'), bbox_inches = "tight")  # may not work
            plt.savefig(imagepath / (imagename + '.eps'), format='eps', dpi=1200)
    
            
    return
            
#%%

def plottrace2(cellType, opsinSwapList, opsinConfig, error):

    import tkinter
    from tkinter.filedialog import askopenfilename
    import pickle
    import os
    
    delayList = [250, 100, 50, 0]
    
    from pathlib import Path

    
    import pandas as pd
    import numpy as np

    
    ACC = pd.DataFrame()
    A1 = pd.DataFrame()
    V1 = pd.DataFrame()
    
    savedLoc1 = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration A1_ACC")
    savedLoc2 = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration A1_ACC mechanism\AP5")
    savedLoc3 = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration A1_ACC mechanism\mibefradil")
    savedLoc4 = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration A1_ACC mechanism\TTX")
    
    savedLoc5 = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration V1_ACC")
    savedLoc6 =Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration A1_V1")
    
    
    for savedLoc in [savedLoc1, savedLoc2, savedLoc3, savedLoc4, savedLoc5, savedLoc6]:
        
        # make a list with all folder names including cellType:
        allnames = os.listdir(savedLoc)
        selectednames = [x for x in allnames if cellType in x]
    

    
        
        for i in selectednames:
            
            if opsinConfig == 'default':
                if i in opsinSwapList:
                    continue
            if opsinConfig == 'swap':
                if i not in opsinSwapList:
                    continue
                
            print('processing...'+str(i)) 
            # point at data file to view
            cellPath = savedLoc / i
            workspacedf = pd.DataFrame()
            

            for file in os.listdir(cellPath):      
                for delay in delayList:
                    if '_'+str(delay)+'ms' in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                workspacedf[str(delay)+'_'+str(k)] = loadedData[k]
               
                if 'A1_ACC' in str(savedLoc):                
                    if i in opsinSwapList:           
                        A1[i] = np.mean(workspacedf[[x for x in workspacedf.columns if '_pulse 1' in x]],axis=1)    
                        ACC[i] = np.mean(workspacedf[[x for x in workspacedf.columns if '_pulse 2' in x]],axis=1)
                                                                   
                    if i not in opsinSwapList:           
                        A1[i] = np.mean(workspacedf[[x for x in workspacedf.columns if '_pulse 2' in x]],axis=1)    
                        ACC[i] = np.mean(workspacedf[[x for x in workspacedf.columns if '_pulse 1' in x]],axis=1) 
                        
                if 'V1_ACC' in str(savedLoc):                
                    if i in opsinSwapList:           
                        V1[i] = np.mean(workspacedf[[x for x in workspacedf.columns if '_pulse 1' in x]],axis=1)    
                        ACC[i] = np.mean(workspacedf[[x for x in workspacedf.columns if '_pulse 2' in x]],axis=1)
                                                                   
                    if i not in opsinSwapList:           
                        V1[i] = np.mean(workspacedf[[x for x in workspacedf.columns if '_pulse 2' in x]],axis=1)    
                        ACC[i] = np.mean(workspacedf[[x for x in workspacedf.columns if '_pulse 1' in x]],axis=1)     
                                   
                if 'A1_V1' in str(savedLoc):                
                    if i in opsinSwapList:           
                        A1[i] = np.mean(workspacedf[[x for x in workspacedf.columns if '_pulse 1' in x]],axis=1)    
                        V1[i] = np.mean(workspacedf[[x for x in workspacedf.columns if '_pulse 2' in x]],axis=1)
                                                                   
                    if i not in opsinSwapList:           
                        A1[i] = np.mean(workspacedf[[x for x in workspacedf.columns if '_pulse 2' in x]],axis=1)    
                        V1[i] = np.mean(workspacedf[[x for x in workspacedf.columns if '_pulse 1' in x]],axis=1)
                        
                                        
    # getting just red and blue

    ACC_data = {}
    A1_data = {}
    V1_data = {}
            
    from matplotlib import pyplot as plt
    import scipy.stats    
    
    for iFiber in [ACC, A1, V1]:
        
        plt.figure()
        
        if error == 'pop':
            
            if iFiber.equals(ACC):
                plt.title('ACC '+ cellType)
            elif iFiber.equals(A1):
                plt.title('A1 '+ cellType)
            elif iFiber.equals(V1):
                plt.title('V1 '+ cellType)
            
            
            modelData = pd.read_excel(r'C:\Users\Lur Lab 3\Dropbox\Rindner et al\model figures\model figure data\Single input supplementary trace\single input traces.xlsx', sheet_name = 'model traces', usecols="A:B") 
            # modelThreshCross = np.argmin(modelData['model 30ms NMDA; Na 0.015; T-Ca 0.0031:0.0062:0.0031'][0:150] - 0.5)
            
            
            for iTrace in iFiber.columns:
                #using 920 adjusts for synaptic delay
                # threshCross = np.argmin(iFiber[iTrace][920:1050]-0.5)
                
                plt.plot(iFiber[iTrace][920:4000].reset_index().drop('index',axis=1),color='lightgrey')
                
            ACC_data = ACC.loc[920:4000,:]
            A1_data = A1.loc[920:4000,:]
            V1_data = V1.loc[920:4000,:]
            
            
            plt.plot(modelData['model 30ms NMDA; Na 0.015; T-Ca 0.0031:0.0062:0.0031'],label='30ms NMDA decay')            
            plt.plot(modelData['model 60ms NMDA; Na 0.015; T-Ca 0.0031:0.0062:0.0031'],label='60ms NMDA decay') 
            plt.legend()
            plt.xlim(0,1500)
        
            #plot normalized
            plt.figure()
            if iFiber.equals(ACC):
                plt.title('ACC peak normalized '+ cellType)
            elif iFiber.equals(A1):
                plt.title('A1 peak normalized '+ cellType)
            elif iFiber.equals(V1):
                plt.title('V1 peak normalized '+ cellType)

            for iTrace in iFiber.columns:
                #using 930 adjusts for synaptic delay
                plt.plot(iFiber[iTrace][920:4000].reset_index().drop('index',axis=1)/max(iFiber[iTrace][930:1400]),color='lightgrey')            
            plt.plot(modelData['model 30ms NMDA; Na 0.015; T-Ca 0.0031:0.0062:0.0031']/max(modelData['model 30ms NMDA; Na 0.015; T-Ca 0.0031:0.0062:0.0031']),label='30ms NMDA decay')            
            plt.plot(modelData['model 60ms NMDA; Na 0.015; T-Ca 0.0031:0.0062:0.0031']/max(modelData['model 60ms NMDA; Na 0.015; T-Ca 0.0031:0.0062:0.0031']),label='60ms NMDA decay') 
            plt.legend()
            plt.xlim(0,1500)
        
        else:
            modelData = pd.read_excel(r'C:\Users\Lur Lab 3\Dropbox\Rindner et al\model figures\model figure data\Single input supplementary trace\single input traces.xlsx', sheet_name = 'model traces', usecols="A:B")
            plt.plot(modelData['model 30ms NMDA; Na 0.015; T-Ca 0.0031:0.0062:0.0031'],label='30ms NMDA decay')            
            plt.plot(modelData['model 60ms NMDA; Na 0.015; T-Ca 0.0031:0.0062:0.0031'],label='60ms NMDA decay') 
            
            plt.legend()
            
            print('working...')
            workspaceMousedf = iFiber.copy().transpose()
            workspaceMousedf = workspaceMousedf.astype(float)
            workspaceMousedf['strippedID'] = ""
            for i in workspaceMousedf.index:
                workspaceMousedf.at[i,'strippedID'] = i[:i.find('cell')-1] + '_' + i[-3:]
            grp_mouse = workspaceMousedf.groupby(['strippedID'])
            ggg = grp_mouse.mean()
        
            
             #get CI stats
            CIstats = pd.DataFrame(index=['95% CI','sem','std','mean','upper bound','lower bound'])
            

            
    
    
    
            for col in list(ggg.columns): 
                a = ggg[col].values
                float_arr = np.vstack(a[:]).astype(np.float)
                n = len(float_arr)
                m = ggg[col].mean()   
                CIstats.at['mean',col]= m
                maxVal = max(a)
                minVal = min(a)
                           
                if error == '95CI':
                    h = se * scipy.stats.t.ppf((1 + 0.95) / 2., n-1)
                    CIstats.at['95% CI',col] = h
                    CIstats.at['upper bound',col]= float(m + h)     
                    CIstats.at['lower bound',col]= float(m - h)  
                if error == 'sem':
                    se = scipy.stats.sem(float_arr, nan_policy = 'omit')
                    CIstats.at['sem',col] = se
                    CIstats.at['upper bound',col]= float(m + se)    
                    CIstats.at['lower bound',col]= float(m - se)  
                if error == 'std':
                    h = np.nanstd(float_arr)
                    CIstats.at['std',col] = h
                    CIstats.at['upper bound',col]= float(m + h)     
                    CIstats.at['lower bound',col]= float(m - h) 
                if error == 'maxmin':
                    CIstats.at['upper bound',col]= maxVal     
                    CIstats.at['lower bound',col]= minVal
                
                
            from matplotlib import pyplot as plt
            
            
            x = CIstats.transpose()
            
    
            plotColor = 'fuchsia'
    
                
            
            
            data2plot = x['mean'][950:3000]
            yerrTop = x['upper bound'][950:3000]
            yerrBottom = x['lower bound'][950:3000]
            names = np.asarray(list(x.index)[950:3000])
            
    
        
            
            plt.plot(data2plot,plotColor)
            yerrUpper = np.asarray(yerrTop)
            yerrLower = np.asarray(yerrBottom)
            flat_yerrUpper = yerrUpper.flatten()
            flat_yerrLower = yerrLower.flatten()
    
            chosenColor = 'fuchsia'
    
            plt.fill_between(names, flat_yerrUpper, flat_yerrLower,alpha=0.3,interpolate=True,color = chosenColor)
    
            plt.text(225, 2.3, 'n = '+str(len(ggg.index)), fontsize=14)
            plt.ylim(-2.5,15)
            plt.xlim(750,4500)
            
            if iFiber.equals(ACC):             
                plt.title('ACC')
                ACC_data['yerrTop'] = yerrTop
                ACC_data['yerrBottom'] = yerrBottom
                ACC_data['mean'] = data2plot
                
            if iFiber.equals(A1):
                plt.title('A1')
                A1_data['yerrTop'] = yerrTop
                A1_data['yerrBottom'] = yerrBottom
                A1_data['mean'] = data2plot
            
            plt.show()
            
    
            if iFiber.equals(ACC):             
                ACC_mean = np.array(CIstats.loc['mean',:])
            if iFiber.equals(A1):
                A1_mean = np.array(CIstats.loc['mean',:])
                

            
    return ACC_data, A1_data, V1_data

            
        
#%%            
        
def plotISteps(plotMin,plotMax,plotStart,plotStop,imageloc,step,firstTrace,Vm):      

    import tkinter
    from tkinter.filedialog import askopenfilename
    import pickle
    from matplotlib import pyplot as plt

    from pathlib import Path
    if Vm == 'Vrest':
        savedLoc = Path(r"C:\Users\Jay\Desktop\Preprocessed data\current steps\Vrest")
    if Vm == '70':
        savedLoc = Path(r"C:\Users\Jay\Desktop\Preprocessed data\current steps\-70")
        
    # make a list with all folder names including cellType:
    import os
    allnames = os.listdir(savedLoc)
    selectednames = [x for x in allnames]


    for i in selectednames:
        print('processing...'+str(i)) 
        
        # point at data file to view
        cellPath = savedLoc / i
        
        import pandas as pd
        import numpy as np
        
        tkinter.Tk().withdraw()
        loadedData = pickle.load(open(cellPath, 'rb'))
        
        for k in loadedData.keys():
            if '_data' in k:
                data = loadedData[k]
                plt.figure()
                plt.plot(data[:,firstTrace::step])
                plt.ylim((plotMin,plotMax))
                plt.yticks(np.arange(plotMin, plotMax+1, 20))
                plt.xlim((plotStart,plotStop))
                plt.title(str(i))

                imagename = str(i)
                imagepath = Path(imageloc)
                
                plt.savefig(imagepath / (imagename + '.png'))  # may not work
                plt.savefig(imagepath / (imagename + '.eps'), format='eps', dpi=1200)
                plt.close()
         
 

#%%
def plot3DcellMetrics():

    sweep = 13          # for old ISI ratio
    ISIspike = 3           # this is which spike n is looked at (ISI of spike 1 and spike n) for burstiness
    closestISI = 12
    closestAdap = 6
    spikeNumAHP = 3
    time = 30
    firstSpike = 1
    sagDepth = 90
    spikeNumAHP = 6
    closestSpike = 7
    
    depolToHyperList = ['200416_pvai_182_cell1_Isteps_Vrest_IB','200416_pvai_182_cell1_Isteps_Vrest_IB','200424_wt_999_cell1_Isteps_Vrest_IB',
                        '200501_wt_1010_cell1_Isteps_70_RS','200506_wt_1009_cell1_Isteps_Vrest_RS','200512_wt_1018_cell3_Isteps_70_RS','200515_wt_1040_cell2_Isteps_Vrest_IB',
                        '200522_wt_1045_cell4_Isteps_70_IB','200524_wt_1045_cell1_Isteps_70_IB','200524_wt_1053_cell2_Isteps_70_RS']

    plot = 'separate' # either separate or overlap
    

    from mpl_toolkits import mplot3d
    import numpy as np
    import matplotlib.pyplot as plt
    
    import DR_celltype as getMetric
    savedLoc = r"Z:\Danny R\Slice Phys\Preprocessed data\current steps\-70\PPC_L5"
    VrestLoc = r"Z:\Danny R\Slice Phys\Preprocessed data\current steps\just Vrest"
    
    Rinput = getMetric.getRinput(savedLoc) # uses -100 pA step to calculate Ri in MOhms
    sag, sagST = getMetric.getSag(savedLoc, depolToHyperList, sagDepth)
    Vrest = getMetric.getVrest(VrestLoc, savedLoc)
    spike, spikeAHP, spikeWidth = getMetric.getSpikeShape(savedLoc, depolToHyperList, spikeNumAHP) 
    sAHP = getMetric.getAHPslow(savedLoc)
    AHPdif = getMetric.getMinimaDiff(savedLoc, closestSpike)
    APnums = getMetric.gethowmanyAPs(savedLoc, depolToHyperList, closestSpike)
    


    import os
    allnames = os.listdir(savedLoc)
    
    import pandas as pd
    
    classification = pd.DataFrame({'cell ID':[*allnames]}).set_index('cell ID')
    classification['Vrest'] = Vrest.values()
    classification['Rinput'] = Rinput.values()
    classification['sag'] = sag.values()
    classification['AP half width'] = spikeWidth.values()
    classification['sAHP'] = sAHP.values()

    classification['max AHP difference'] = AHPdif.values()
    classification['AP count'] = APnums.values()
    


    for i in list(classification.index):
        classification.at[i,'qualitative cell type'] = i[-2:]
        
    IBclass = classification[classification['qualitative cell type'] == 'IB']
    RSclass = classification[classification['qualitative cell type'] == 'RS']
    
    
    plt.figure()
    x, y, z = plt.hist(IBclass['AP count'], alpha = 0.5, label = 'IB', weights=np.ones(len(IBclass['AP count'])) / len(IBclass['AP count']),bins=20)
    plt.hist(RSclass['AP count'], bins = y, alpha = 0.5, label = 'RS', weights=np.ones(len(RSclass['AP count'])) / len(RSclass['AP count']))
    plt.axvline(np.mean(IBclass['AP count']))
    plt.axvline(np.mean(RSclass['AP count']))
    pVal, color = getMetric.getStat(IBclass['AP count'].dropna(),RSclass['AP count'].dropna())
    plt.legend()
    plt.ylabel('% of cells')
    plt.xlabel('AP count')
    plt.title('% of APs within 40ms of first peak \n MWU pval = '+pVal +'\n IB mean= %.2f' % np.mean(IBclass['AP count']) +'; RS mean= %.2f' % np.mean(RSclass['AP count']))
    plt.ylim(0,0.3)
        

    plt.figure()
    x, y, z = plt.hist(IBclass['Vrest'], alpha = 0.5, label = 'IB', weights=np.ones(len(IBclass['Vrest'])) / len(IBclass['Vrest']),bins=20)
    plt.hist(RSclass['Vrest'], bins = y, alpha = 0.5, label = 'RS', weights=np.ones(len(RSclass['Vrest'])) / len(RSclass['Vrest']))
    plt.axvline(np.mean(IBclass['Vrest']))
    plt.axvline(np.mean(RSclass['Vrest']))
    pVal, color = getMetric.getStat(IBclass['Vrest'].dropna(),RSclass['Vrest'].dropna())
    plt.legend()
    plt.ylabel('% of cells')
    plt.xlabel('Vrest (mV)')
    plt.title('Vrest \n MWU pval = '+pVal +'\n IB mean= %.2f' % np.mean(IBclass['Vrest']) +'; RS mean= %.2f' % np.mean(RSclass['Vrest']))
    plt.ylim(0,0.3)
    
    
    plt.figure()
    x, y, z = plt.hist(IBclass['max AHP difference'], alpha = 0.5, label = 'IB', weights=np.ones(len(IBclass['max AHP difference'])) / len(IBclass['max AHP difference']),bins=20)
    plt.hist(RSclass['max AHP difference'], bins = y, alpha = 0.5, label = 'RS', weights=np.ones(len(RSclass['max AHP difference'])) / len(RSclass['max AHP difference']))
    plt.axvline(np.mean(IBclass['max AHP difference']))
    plt.axvline(np.mean(RSclass['max AHP difference']))
    pVal, color = getMetric.getStat(IBclass['max AHP difference'].dropna(),RSclass['max AHP difference'].dropna())
    plt.legend()
    plt.ylabel('% of cells')
    plt.xlabel('max AHP difference (mV)')
    plt.title('max AHP difference \n MWU pval = '+pVal +'\n IB mean= %.2f' % np.mean(IBclass['max AHP difference']) +'; RS mean= %.2f' % np.mean(RSclass['max AHP difference']))
    plt.ylim(0,0.3)
    
    
    plt.figure()
    x, y, z = plt.hist(IBclass['sAHP'], alpha = 0.5, label = 'IB', weights=np.ones(len(IBclass['sAHP'])) / len(IBclass['sAHP']),bins=20)
    plt.hist(RSclass['sAHP'], bins = y, alpha = 0.5, label = 'RS', weights=np.ones(len(RSclass['sAHP'])) / len(RSclass['sAHP']))
    plt.axvline(np.mean(IBclass['sAHP']))
    plt.axvline(np.mean(RSclass['sAHP']))
    pVal, color = getMetric.getStat(IBclass['sAHP'].dropna(),RSclass['sAHP'].dropna())
    plt.legend()
    plt.ylabel('% of cells')
    plt.xlabel('sAHP (mV)')
    plt.title('sAHP  400ms after current step \n MWU pval = '+pVal +'\n IB mean= %.2f' % np.mean(IBclass['sAHP']) +'; RS mean= %.2f' % np.mean(RSclass['sAHP']))
    plt.ylim(0,0.3)
    
    
    plt.figure()
    x, y, z = plt.hist(IBclass['AP half width'], alpha = 0.5, label = 'IB', weights=np.ones(len(IBclass['AP half width'])) / len(IBclass['AP half width']),bins=20)
    plt.hist(RSclass['AP half width'], bins = y, alpha = 0.5, label = 'RS', weights=np.ones(len(RSclass['AP half width'])) / len(RSclass['AP half width']))
    plt.axvline(np.mean(IBclass['AP half width']))
    plt.axvline(np.mean(RSclass['AP half width']))
    pVal, color = getMetric.getStat(IBclass['AP half width'].dropna(),RSclass['AP half width'].dropna())
    plt.legend()
    plt.ylabel('% of cells')
    plt.xlabel('AP half width (ms)')
    plt.title('AP half width \n MWU pval = '+pVal +'\n IB mean= %.2f' % np.mean(IBclass['AP half width']) +'; RS mean= %.2f' % np.mean(RSclass['AP half width']))  
    plt.ylim(0,0.3)
    
    
    plt.figure()
    x, y, z = plt.hist(IBclass['Rinput'], alpha = 0.5, label = 'IB', weights=np.ones(len(IBclass['Rinput'])) / len(IBclass['Rinput']),range=(0,200),bins=20)
    plt.hist(RSclass['Rinput'], bins = y, alpha = 0.5, label = 'RS', weights=np.ones(len(RSclass['Rinput'])) / len(RSclass['Rinput']),range=(0,200))
    plt.axvline(np.mean(IBclass['Rinput']))
    plt.axvline(np.mean(RSclass['Rinput']))
    pVal, color = getMetric.getStat(IBclass['Rinput'].dropna(),RSclass['Rinput'].dropna())
    plt.legend()
    plt.ylabel('% of cells')
    plt.xlabel('Rinput in MOhm')
    plt.title('Rinput\n  MWU pval = '+pVal +'\n IB mean= %.2f' % np.mean(IBclass['Rinput']) +'; RS mean= %.2f' % np.mean(RSclass['Rinput']))
    plt.ylim(0,0.3)
    

    plt.figure()
    x, y, z = plt.hist(IBclass['sag'], alpha = 0.5, label = 'IB', weights=np.ones(len(IBclass['sag'])) / len(IBclass['sag']), bins=20)
    plt.hist(RSclass['sag'], bins = y, alpha = 0.5, label = 'RS', weights=np.ones(len(RSclass['sag'])) / len(RSclass['sag']))
    plt.axvline(np.mean(IBclass['sag']))
    plt.axvline(np.mean(RSclass['sag']))
    pVal, color = getMetric.getStat(IBclass['sag'].dropna(),RSclass['sag'].dropna())
    plt.legend()
    plt.ylabel('% of cells')
    plt.xlabel('%sag (mV)')
    plt.title('%sag ' + 'at -'+str(sagDepth)+' \n MWU pval'+pVal +'\n IB mean= %.2f' % np.mean(IBclass['sag']) +'; RS mean= %.2f' % np.mean(RSclass['sag']))
    plt.ylim(0,0.3)
    


    ax1 = plt.figure().gca(projection='3d')
    plt.gca().invert_yaxis()
 
    x = 'AP count'
    y = 'Rinput'
    z = 'max AHP difference'
    
    #without sag shading
    red = [0.94,0.35,0.24]
    blue = [0.28,0.62,0.78]
    IBscat = ax1.scatter(IBclass[x], IBclass[y], IBclass[z], c=red, label='IB',  depthshade=False, s=12)
    RSscat = ax1.scatter(RSclass[x], RSclass[y], RSclass[z], c=blue, label='RS', depthshade=False, s=12)
    

    
    plt.legend()
    ax1.set_xlabel(x)
    ax1.set_ylabel(y)
    ax1.set_zlabel(z)
    plt.show()
        

    
    return classification

   
#%%
def getLatency(opsinSwapList):

    import tkinter
    from tkinter.filedialog import askopenfilename
    import pickle
    from pathlib import Path
    import os
    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt
    
    
    #will spit out which cells are over thresh
    
    chrimson = {}
    chr2 = {}
    
    chr2['ACC'] = pd.DataFrame()
    chr2['A1'] = pd.DataFrame()
    chr2['V1'] = pd.DataFrame()
    
    chrimson['ACC'] = pd.DataFrame()
    chrimson['A1'] = pd.DataFrame()
    chrimson['V1'] = pd.DataFrame()
    
    for iFolder in ['integration A1_ACC', 'integration V1_ACC', 'integration A1_V1']:
        
        dataloc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data")
        savedLoc = dataloc / iFolder
        allnames = os.listdir(savedLoc)
        
        for iCell in allnames:
            print('processing...'+str(iCell)) 
            
            # point at data file to view
            cellPath = savedLoc / iCell
    
            for file in os.listdir(cellPath):
                
                if '_0ms_blue' in file and 'red' not in file:
                    
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    
                    for k in loadedData.keys():
                        if '_data' in k:
                            data = loadedData[k]
    
                    #place the data into the appropriate df
                    if iFolder == 'integration A1_ACC':
                        if iCell in opsinSwapList:
                            chr2['A1'][str(iCell)] = data
                        if iCell not in opsinSwapList:
                            chr2['ACC'][str(iCell)] = data
                            
                    if iFolder == 'integration V1_ACC':
                        if iCell in opsinSwapList:
                            chr2['V1'][str(iCell)] = data
                        if iCell not in opsinSwapList:
                            chr2['ACC'][str(iCell)] = data
                                                        
                    if iFolder == 'integration A1_V1':
                        if iCell in opsinSwapList:
                            chr2['A1'][str(iCell)] = data
                        if iCell not in opsinSwapList:
                            chr2['V1'][str(iCell)] = data
                                                        
                                         
                if '_0ms_red' in file:       
                        
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    
                    for k in loadedData.keys():
                        if '_data' in k:
                            data = loadedData[k]
    
                    #place the data into the appropriate df
                    if iFolder == 'integration A1_ACC':
                        if iCell in opsinSwapList:
                            chrimson['ACC'][str(iCell)] = data
                        if iCell not in opsinSwapList:
                            chrimson['A1'][str(iCell)] = data 
                            
                    if iFolder == 'integration V1_ACC':
                        if iCell in opsinSwapList:
                            chrimson['ACC'][str(iCell)] = data
                        if iCell not in opsinSwapList:
                            chrimson['V1'][str(iCell)] = data                             
                            
                    if iFolder == 'integration A1_V1':
                        if iCell in opsinSwapList:
                            chrimson['V1'][str(iCell)] = data
                        if iCell not in opsinSwapList:
                            chrimson['A1'][str(iCell)] = data          
                            
      
    chr2Rise = {}
    chr2Rise['A1'] = pd.DataFrame()
    chr2Rise['ACC'] = pd.DataFrame()
    chr2Rise['V1'] = pd.DataFrame()
    
    chrimsonRise = {}
    chrimsonRise['A1'] = pd.DataFrame()
    chrimsonRise['ACC'] = pd.DataFrame()
    chrimsonRise['V1'] = pd.DataFrame()

    for k, v in chr2.items():
        for i in v:
            set1 = np.asarray(chr2[k][i][995:2000])
            set2 = np.asarray(chr2[k][i][1000:2005])
            derv = (set2 - set1)/5
                     
            thresh = 0.04

            r = np.arange(len(derv))
            for index in r:
                derv[index]
                if derv[index] < thresh :
                    continue
                if derv[index] >= thresh:
                    chr2Rise[k].at['0',i] = (index + 2 - 5)/10
                    break


    for k, v in chrimson.items():
        for i in v:
            set1 = np.asarray(chrimson[k][i][995:2000])
            set2 = np.asarray(chrimson[k][i][1000:2005])
            derv = (set2 - set1)/5
                     
            thresh = 0.04

            r = np.arange(len(derv))
            for index in r:
                derv[index]
                if derv[index] < thresh :
                    continue
                if derv[index] >= thresh:
                    chrimsonRise[k].at['0',i] = (index + 2 - 5)/10
                    break
                    
    for fiber in ['A1','V1','ACC']:
        
        plt.figure()
        chr2max = np.max(list(np.asarray(chr2Rise[fiber])))
        chrimsonmax = np.max(list(np.asarray(chrimsonRise[fiber])))
        
        if chr2max > chrimsonmax:
            x, y, z = plt.hist(chr2Rise[fiber], alpha = 0.5, label = 'chr2')
            plt.hist(chrimsonRise[fiber], bins = y, alpha = 0.5, label = 'chrimson')
            plt.legend()
            plt.title(fiber)
            plt.xlabel('EPSP latency (ms)')
            plt.ylabel('EPSP amplitude (mV)')
            xmin, xmax, ymin, ymax = plt.axis()
            plt.vlines(0,-1,ymax,color = 'k', linestyles='dashed')
            plt.xlim(left = -1)
            plt.axhline(color='k')
            
        else:
            x, y, z = plt.hist(chrimsonRise[fiber], alpha = 0.5, label = 'chrimson')
            plt.hist(chr2Rise[fiber], bins = y, alpha = 0.5, label = 'chr2')
            plt.legend()
            plt.title(fiber)
            plt.xlabel('EPSP latency (ms)')
            plt.ylabel('EPSP amplitude (mV)')
            xmin, xmax, ymin, ymax = plt.axis()
            plt.vlines(0,-1,ymax,color = 'k', linestyles='dashed')
            plt.xlim(left = -1)
            plt.axhline(color='k')

        
    return chr2Rise, chrimsonRise

#%%
def compareLatency(chr2Latency, chrimsonLatency):

    # for comparing opsins
    from matplotlib import pyplot as plt
    plt.figure()
    giant = []
    overThreshLatency = []
    for k, v in chr2Latency.items():
        x = list(chr2Latency[k].iloc[0,:])
        giant.extend(x)
        for i in list(v):
            if float(chr2Latency[k][i]) > 4:
                overThreshLatency.append(i) if i not in overThreshLatency else overThreshLatency
                print(i + ' is over threshold and fiber is ' +k )
                
    for k, v in chrimsonLatency.items():
        x = list(chrimsonLatency[k].iloc[0,:])
        giant.extend(x)
        for i in list(v):
            if float(chrimsonLatency[k][i]) > 4:
                overThreshLatency.append(i) if i not in overThreshLatency else overThreshLatency
                print(i + ' is over threshold and fiber is ' +k )
        
    import statistics
    median = statistics.median(giant)
    
    plt.hist(giant)
    plt.xlabel('EPSP latency (ms)')
    plt.title('all inputs latency histogram '+ str(len(giant)/2) + 'cells, median is ' +str(median))
    xmin, xmax, ymin, ymax = plt.axis()
    plt.vlines(0,-1,ymax,color = 'k', linestyles='dashed')
    plt.vlines(4,-1,ymax,color = 'k', linestyles='dashed')
    plt.xlim(left = -1)
    plt.axhline(color='k')    

#%%
def compareTTXLatency(chr2Latency, chrimsonLatency):
        
    #for seeing what the max latency is that we got recovery ALL CELLS IN THIS LIST HAD RECOVERY
    #make list of all good TTX cells where got recovery (looks only at the folders where we place cells that were determined to have good recovery)
    from pathlib import Path
    import os
    
    allnames = []
    for iFolder in ['TTX A1_ACC', 'TTX V1_ACC', 'TTX A1_V1']:
        
        dataloc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\TTX experiments")
        savedLoc = dataloc / iFolder
        y = os.listdir(savedLoc)
        allnames.extend(y)
    
    
    #make list of latencies for these cells (regardless of input)
    TTXlatencies = {}
    
    for k, v in chr2Latency.items():
        for cell in list(v.columns):
            if cell in allnames:
                TTXlatencies[cell] = float(chr2Latency[k][cell])
            else:
                continue
    
    for k, v in chrimsonLatency.items():
        for cell in list(v.columns):
            if cell in allnames:
                TTXlatencies[cell] = float(chrimsonLatency[k][cell])
            else:
                continue    
    
    #print what the longest latency is where we get recovery
    print('The largest latency where we get TTX recovery is ' + str(max(TTXlatencies.values())) + ' ms')
    print('The shortest latency where we get TTX recovery is ' + str(min(TTXlatencies.values())) + ' ms')
    
    
    #compare lists of cells that had recovery with integration experiment ones that were over threshold
    overThreshFinal = [x for x in overThreshLatency if x not in allnames]

#%%
def getEPSPDecayConstants(opsinSwapList, confidence, showOpsinAvg, showHist, showBar):

    import tkinter
    from tkinter.filedialog import askopenfilename
    import pickle
    from pathlib import Path
    import os
    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt
    
    chrimson = {}
    chr2 = {}
    
    chr2['ACC'] = pd.DataFrame()
    chr2['A1'] = pd.DataFrame()
    chr2['V1'] = pd.DataFrame()
    
    chrimson['ACC'] = pd.DataFrame()
    chrimson['A1'] = pd.DataFrame()
    chrimson['V1'] = pd.DataFrame()
    
    outliers = []

    
    for iFolder in ['integration A1_ACC', 'integration V1_ACC', 'integration A1_V1']:
        
        dataloc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data")
        savedLoc = dataloc / iFolder
        allnames = os.listdir(savedLoc)
        
        for iCell in allnames:
            print('processing...'+str(iCell)) 
            
            if iCell in outliers:
                continue
            
            # point at data file to view
            cellPath = savedLoc / iCell
    
            for file in os.listdir(cellPath):
                
                if '_0ms_blue' in file and 'red' not in file:
                    
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    
                    for k in loadedData.keys():
                        if '_data' in k:
                            data = loadedData[k]
    
                    #place the data into the appropriate df
                    if iFolder == 'integration A1_ACC':
                        if iCell in opsinSwapList:
                            chr2['A1'][str(iCell)] = data
                        if iCell not in opsinSwapList:
                            chr2['ACC'][str(iCell)] = data
                            
                    if iFolder == 'integration V1_ACC':
                        if iCell in opsinSwapList:
                            chr2['V1'][str(iCell)] = data
                        if iCell not in opsinSwapList:
                            chr2['ACC'][str(iCell)] = data
                                                        
                    if iFolder == 'integration A1_V1':
                        if iCell in opsinSwapList:
                            chr2['A1'][str(iCell)] = data
                        if iCell not in opsinSwapList:
                            chr2['V1'][str(iCell)] = data
                                                        
                                         
                if '_0ms_red' in file:       
                        
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    
                    for k in loadedData.keys():
                        if '_data' in k:
                            data = loadedData[k]
    
                    #place the data into the appropriate df
                    if iFolder == 'integration A1_ACC':
                        if iCell in opsinSwapList:
                            chrimson['ACC'][str(iCell)] = data
                        if iCell not in opsinSwapList:
                            chrimson['A1'][str(iCell)] = data 
                            
                    if iFolder == 'integration V1_ACC':
                        if iCell in opsinSwapList:
                            chrimson['ACC'][str(iCell)] = data
                        if iCell not in opsinSwapList:
                            chrimson['V1'][str(iCell)] = data                             
                            
                    if iFolder == 'integration A1_V1':
                        if iCell in opsinSwapList:
                            chrimson['V1'][str(iCell)] = data
                        if iCell not in opsinSwapList:
                            chrimson['A1'][str(iCell)] = data                             
    
    chr2Tau = {}
    chrimsonTau = {}
    
    chr2Tau['ACC'] = {}
    chr2Tau['A1'] = {}
    chr2Tau['V1'] = {}
    
    chrimsonTau['ACC'] = {}
    chrimsonTau['A1'] = {}
    chrimsonTau['V1'] = {}
    
    import numpy as np
    import scipy.stats
    
    def exponential(x, a, k, b):
      return a*np.exp(x*k)+b  
  
    for fiber in chr2.keys():
        
        import numpy as np
        import scipy.stats
        print('processing tau...'+str(fiber))
        
        for cell in chr2[fiber].columns:
               
            shortData = chr2[fiber][cell][700:2200]
            peakLoc = np.argmax(shortData) + 700
    
            decay = shortData[peakLoc]*0.368
            idx = (np.abs(shortData[peakLoc-700:]-decay)).argmin() + peakLoc
               
            tau = (idx - peakLoc) / 10
            chr2Tau[fiber][cell] = tau
            
        

    for fiber in chrimson.keys():
        
        import numpy as np
        import scipy.stats
        print('processing tau...'+str(fiber))
        
        for cell in chrimson[fiber].columns:
            shortData = chrimson[fiber][cell][700:2200]
            peakLoc = np.argmax(shortData) + 700

            decay = shortData[peakLoc]*0.368
            idx = (np.abs(shortData[peakLoc-700:]-decay)).argmin() + peakLoc
            
            
            tau = (idx - peakLoc) / 10
            chrimsonTau[fiber][cell] = tau
                
         
    chr2_stats = {}
    chrimson_stats = {}
    
    for k, v in chr2.items():
        
        #get CI stats
        chr2_stats[str(k)] = pd.DataFrame(columns=['95% CI','mean','upper bound','lower bound'])
    
        import numpy as np
        import scipy.stats
    
        for row in list(chr2[k].index[700:2200]): 
            a = v.loc[row,:]
            float_arr = np.vstack(a[:]).astype(np.float)
            n = len(float_arr)
            m = v.loc[row,:].mean()
            se = scipy.stats.sem(float_arr, nan_policy = 'omit')
            h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
            #h = np.nanstd(float_arr) for standard dev
            chr2_stats[k].at[row,'95% CI']= h
            chr2_stats[k].at[row,'mean']= m
            chr2_stats[k].at[row,'upper bound']= m + h     
            chr2_stats[k].at[row,'lower bound']= m - h  
        
        print('processing chr2 CI...'+str(k))
        
        
    for k, v in chrimson.items():
        
        #get CI stats
        chrimson_stats[str(k)] = pd.DataFrame(columns=['95% CI','mean','upper bound','lower bound'])
    
        import numpy as np
        import scipy.stats
    
        for row in list(chrimson[k].index[700:2200]): 
            a = v.loc[row,:]
            float_arr = np.vstack(a[:]).astype(np.float)
            n = len(float_arr)
            m = v.loc[row,:].mean()
            se = scipy.stats.sem(float_arr, nan_policy = 'omit')
            h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
            #h = np.nanstd(float_arr) for standard dev
            chrimson_stats[k].at[row,'95% CI']= h
            chrimson_stats[k].at[row,'mean']= m
            chrimson_stats[k].at[row,'upper bound']= m + h     
            chrimson_stats[k].at[row,'lower bound']= m - h  
        
        print('processing chrimson CI...'+str(k))
                    
        
    #plotting avg
    if showOpsinAvg == 1:
        for fiber in chr2_stats.keys():
            plt.figure()
            chr2_values = np.asarray(chr2_stats[fiber]['mean'])
            plt.plot(chr2_values,'blue', label = 'ChR2  n='+str(chr2[fiber].shape[1]))
            chrimson_values = np.asarray(chrimson_stats[fiber]['mean'])
            plt.plot(chrimson_values,'red',label = 'Chrimson  n='+str(chrimson[fiber].shape[1]))    
            plt.title(str(fiber))
            plt.legend()
    
    #histogram
    if showHist == 1:
        for fiber in ['A1','V1','ACC']:
            
            plt.figure()
            chr2max = np.max(list(chr2Tau[fiber].values()))
            chrimsonmax = np.max(list(chrimsonTau[fiber].values()))
            
            if chr2max > chrimsonmax:
                x, y, z = plt.hist(chr2Tau[fiber].values(), alpha = 0.5, label = 'chr2')
                plt.hist(chrimsonTau[fiber].values(), bins = y, alpha = 0.5, label = 'chrimson')
                plt.legend()
                plt.title(str(fiber))
            else:
                x, y, z = plt.hist(chrimsonTau[fiber].values(), alpha = 0.5, label = 'chrimson')
                plt.hist(chr2Tau[fiber].values(), bins = y, alpha = 0.5, label = 'chr2')
                plt.legend()
                plt.title(str(fiber))
            

    if showBar == 1:
        
        cellTypeTau = {}
        
        for cellType in ['IB', 'RS']:            
            cellTypeTau[cellType] = {}
            cellTypeTau[cellType]['chr2'] = {}
            cellTypeTau[cellType]['chrimson'] = {}
            plt.figure()
            
            for fiber, cells in chr2Tau.items():
        
                selected = {k:v for k,v in cells.items() if cellType in k}
                
                x =  [fiber] * len(selected.values())
                y = list(selected.values())
                avg = np.mean(list(selected.values()))
                
                cellTypeTau[cellType]['chr2'][fiber] = y.copy()
                
                plt.scatter(x,y,marker='o',facecolors='none', edgecolors='blue')
                plt.scatter(fiber+' avg', avg, marker='o',facecolors='none', edgecolors='k')
                plt.title('chr2 ' + cellType)
                plt.ylim(0,70)
                
            plt.figure()
            for fiber, cells in chrimsonTau.items():
                
                selected = {k:v for k,v in cells.items() if cellType in k}
                
                x =  [fiber] * len(selected.values())
                y = list(selected.values())
                avg = np.mean(list(selected.values()))
                
                cellTypeTau[cellType]['chrimson'][fiber] = y.copy()
                
                plt.scatter(x,y,marker='o',facecolors='none', edgecolors='red')
                plt.scatter(fiber+' avg', avg, marker='o',facecolors='none', edgecolors='k')
                plt.title('chrimson ' + cellType)
                plt.ylim(0,70)        
            
        
    return chr2_stats, chrimson_stats, chr2Tau, chrimsonTau, cellTypeTau

#%% 

def celltypeDecay():
    
    import tkinter
    from tkinter.filedialog import askopenfilename
    import pickle
    from pathlib import Path
    import os
    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt
   
    
    burstingtraces_ACC = pd.DataFrame()
    burstingtraces_A1 = pd.DataFrame()
    regulartraces_ACC = pd.DataFrame()
    regulartraces_A1 = pd.DataFrame()
    

    for iFolder in ['integration A1_ACC',
                    'integration A1_ACC mechanism\AP5',
                    'integration A1_ACC mechanism\mibefradil',
                    'integration A1_ACC mechanism\TTX',
                    'integration A1_ACC mechanism\PTX']:
        
        dataloc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data")
        savedLoc = dataloc / iFolder
        allnames = os.listdir(savedLoc)
        
        for iCell in allnames:
            print('processing...'+str(iCell)) 
            
            if iCell in celltoRemove:
                continue
        
                
            # point at data file to view
            cellPath = savedLoc / iCell
    
            for file in os.listdir(cellPath):
                
                if '_0ms_blue' in file and 'red' not in file and 'blue_' not in file:
                    
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    
                    for k in loadedData.keys():
                        if '_data' in k:
                            data = loadedData[k]
    
                    #place the data into the appropriate df
                    if 'IB' in iCell:
                        if iCell in opsinSwapList:
                            burstingtraces_A1[iCell] = data
                        if iCell not in opsinSwapList:
                            burstingtraces_ACC[iCell] = data
                    if 'RS' in iCell:
                        if iCell in opsinSwapList:
                            regulartraces_A1[iCell] = data
                        if iCell not in opsinSwapList:
                            regulartraces_ACC[iCell] = data
                                                        
                                         
                if '_0ms_red' in file and 'red_' not in file:       
                        
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    
                    for k in loadedData.keys():
                        if '_data' in k:
                            data = loadedData[k]
    
                    #place the data into the appropriate df
                    if 'IB' in iCell:
                        if iCell in opsinSwapList:
                            burstingtraces_ACC[iCell] = data
                        if iCell not in opsinSwapList:
                            burstingtraces_A1[iCell] = data
                    if 'RS' in iCell:
                        if iCell in opsinSwapList:
                            regulartraces_ACC[iCell] = data
                        if iCell not in opsinSwapList:
                            regulartraces_A1[iCell] = data         
    
   
    test1=[i for i in regulartraces_ACC.columns]
    
    burstingRiseDF = pd.DataFrame(columns=['ACC','A1'])
    regularRiseDF = pd.DataFrame(columns=['ACC','A1'])  
    
    
   

    import DR_tau_functions as gt
    for fiber, data, results in [['ACC', burstingtraces_ACC, burstingRiseDF],
                 ['A1', burstingtraces_A1, burstingRiseDF],
                 ['ACC', regulartraces_ACC, regularRiseDF],
                 ['A1', regulartraces_A1, regularRiseDF]]:
        for cell in data.columns:
            trace = np.asarray(data[cell][900:4000])
            threshold = 0.05
            start = gt.getIPSCstart(trace, threshold)
            rise = gt.getIPSCrise(trace, start)
            results.at[cell, fiber] = rise
        
        
    burstingDecayDF = pd.DataFrame(columns=['ACC','A1'])
    regularDecayDF = pd.DataFrame(columns=['ACC','A1'])   
    
    for fiber, data, results in [['ACC', burstingtraces_ACC, burstingDecayDF],
                 ['A1', burstingtraces_A1, burstingDecayDF],
                 ['ACC', regulartraces_ACC, regularDecayDF],
                 ['A1', regulartraces_A1, regularDecayDF]]:
        for cell in data.columns:
            trace = np.asarray(data[cell][900:4000])
            decay = gt.getIPSCdecay(trace)
            results.at[cell, fiber] = decay    

        
    return burstingRiseDF, regularRiseDF, burstingDecayDF, regularDecayDF
        


#%%
def getEPSPRiseConstants(opsinSwapList, confidence, celltoRemove, showHist, showBar):

    import tkinter
    from tkinter.filedialog import askopenfilename
    import pickle
    from pathlib import Path
    import os
    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt
    
    chrimson = {}
    chr2 = {}
    
    chr2['ACC'] = pd.DataFrame()
    chr2['A1'] = pd.DataFrame()
    chr2['V1'] = pd.DataFrame()
    
    chrimson['ACC'] = pd.DataFrame()
    chrimson['A1'] = pd.DataFrame()
    chrimson['V1'] = pd.DataFrame()
    
    outliers = []
    
    for iFolder in ['integration A1_ACC', 'integration V1_ACC', 'integration A1_V1']:
        
        dataloc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data")
        savedLoc = dataloc / iFolder
        allnames = os.listdir(savedLoc)
        
        for iCell in allnames:
            print('processing...'+str(iCell)) 
            
            if iCell in outliers:
                continue
            
            # point at data file to view
            cellPath = savedLoc / iCell
    
            for file in os.listdir(cellPath):
                
                if '_0ms_blue' in file and 'red' not in file:
                    
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    
                    for k in loadedData.keys():
                        if '_data' in k:
                            data = loadedData[k]
    
                    #place the data into the appropriate df
                    if iFolder == 'integration A1_ACC':
                        if iCell in opsinSwapList:
                            chr2['A1'][str(iCell)] = data
                        if iCell not in opsinSwapList:
                            chr2['ACC'][str(iCell)] = data
                            
                    if iFolder == 'integration V1_ACC':
                        if iCell in opsinSwapList:
                            chr2['V1'][str(iCell)] = data
                        if iCell not in opsinSwapList:
                            chr2['ACC'][str(iCell)] = data
                                                        
                    if iFolder == 'integration A1_V1':
                        if iCell in opsinSwapList:
                            chr2['A1'][str(iCell)] = data
                        if iCell not in opsinSwapList:
                            chr2['V1'][str(iCell)] = data
                                                        
                                         
                if '_0ms_red' in file:       
                        
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    
                    for k in loadedData.keys():
                        if '_data' in k:
                            data = loadedData[k]
    
                    #place the data into the appropriate df
                    if iFolder == 'integration A1_ACC':
                        if iCell in opsinSwapList:
                            chrimson['ACC'][str(iCell)] = data
                        if iCell not in opsinSwapList:
                            chrimson['A1'][str(iCell)] = data 
                            
                    if iFolder == 'integration V1_ACC':
                        if iCell in opsinSwapList:
                            chrimson['ACC'][str(iCell)] = data
                        if iCell not in opsinSwapList:
                            chrimson['V1'][str(iCell)] = data                             
                            
                    if iFolder == 'integration A1_V1':
                        if iCell in opsinSwapList:
                            chrimson['V1'][str(iCell)] = data
                        if iCell not in opsinSwapList:
                            chrimson['A1'][str(iCell)] = data                             
    
    chr2Tau = {}
    chrimsonTau = {}
    
    chr2Tau['ACC'] = {}
    chr2Tau['A1'] = {}
    chr2Tau['V1'] = {}
    
    chrimsonTau['ACC'] = {}
    chrimsonTau['A1'] = {}
    chrimsonTau['V1'] = {}
    
    import numpy as np
    import scipy.stats
    

    for fiber in chr2.keys():
        
        import numpy as np
        import scipy.stats
        print('processing tau...'+str(fiber))
        
        
        for cell in chr2[fiber].columns:
            
            set1 = np.asarray(chr2[fiber][cell][995:2000])
            set2 = np.asarray(chr2[fiber][cell][1000:2005])
            derv = (set2 - set1)/5
                     
            thresh = 0.04

            r = np.arange(len(derv))
            for index in r:
                
                if derv[index] < thresh :
                    continue
                if derv[index] >= thresh:
                    startEPSP = (index + 2)
                    break
      
                
            shortData = chr2[fiber][cell][700:2200]
            peakLoc = np.argmax(shortData)

            rise = shortData[peakLoc]*0.632
            
            for x in list(shortData.index):
                if shortData[x] < rise:
                    continue
                if shortData[x] >= rise:
                    tauidx = x
                    break
            
            startidx = 1000 + startEPSP
            idx = tauidx - startidx
            
            tau = idx / 10
            chr2Tau[fiber][cell] = tau


    for fiber in chrimson.keys():
        
        import numpy as np
        import scipy.stats
        print('processing tau...'+str(fiber))
        
        for cell in chrimson[fiber].columns:
            
            set1 = np.asarray(chrimson[fiber][cell][995:2000])
            set2 = np.asarray(chrimson[fiber][cell][1000:2005])
            derv = (set2 - set1)/5
                     
            thresh = 0.04

            r = np.arange(len(derv))
            for index in r:
                
                if derv[index] < thresh :
                    continue
                if derv[index] >= thresh:
                    startEPSP = (index + 2)
                    break
    
            shortData = chrimson[fiber][cell][700:2200]
            peakLoc = np.argmax(shortData)

            rise = shortData[peakLoc]*0.632
            
            for x in list(shortData.index):
                if shortData[x] < rise:
                    continue
                if shortData[x] >= rise:
                    tauidx = x
                    break
            
            startidx = 1000 + startEPSP
            idx = tauidx - startidx
            
            tau = idx / 10
            chrimsonTau[fiber][cell] = tau
            

    #histogram
    if showHist == 1:
        for fiber in ['A1','V1','ACC']:
            
            plt.figure()
            chr2max = np.max(list(chr2Tau[fiber].values()))
            chrimsonmax = np.max(list(chrimsonTau[fiber].values()))
            plt.title('trace')
            
            if chr2max > chrimsonmax:
                x, y, z = plt.hist(chr2Tau[fiber].values(), alpha = 0.5, label = 'chr2')
                plt.hist(chrimsonTau[fiber].values(), bins = y, alpha = 0.5, label = 'chrimson')
                plt.legend()
                plt.title(str(fiber))
            else:
                x, y, z = plt.hist(chrimsonTau[fiber].values(), alpha = 0.5, label = 'chrimson')
                plt.hist(chr2Tau[fiber].values(), bins = y, alpha = 0.5, label = 'chr2')
                plt.legend()
                plt.title(str(fiber))
            

    if showBar == 1:
     
        cellTypeTau = {}
        
        for cellType in ['IB', 'RS']:            
            cellTypeTau[cellType] = {}
            cellTypeTau[cellType]['chr2'] = {}
            cellTypeTau[cellType]['chrimson'] = {}
            plt.figure()
            
            for fiber, cells in chr2Tau.items():
        
                selected = {k:v for k,v in cells.items() if cellType in k}
                
                x =  [fiber] * len(selected.values())
                y = list(selected.values())
                avg = np.mean(list(selected.values()))
                
                cellTypeTau[cellType]['chr2'][fiber] = y.copy()
                
                plt.scatter(x,y,marker='o',facecolors='none', edgecolors='blue')
                plt.scatter(fiber+' avg', avg, marker='o',facecolors='none', edgecolors='k')
                plt.title('chr2 ' + cellType)
                plt.ylim(0,10)
                
            plt.figure()
            for fiber, cells in chrimsonTau.items():
                
                selected = {k:v for k,v in cells.items() if cellType in k}
                
                x =  [fiber] * len(selected.values())
                y = list(selected.values())
                avg = np.mean(list(selected.values()))
                
                cellTypeTau[cellType]['chrimson'][fiber] = y.copy()
                
                plt.scatter(x,y,marker='o',facecolors='none', edgecolors='red')
                plt.scatter(fiber+' avg', avg, marker='o',facecolors='none', edgecolors='k')
                plt.title('chrimson ' + cellType)
                plt.ylim(0,10)        
        
       
            
    return  chr2Tau, chrimsonTau, cellTypeTau

#%%

def getIPSCConstants():
    
    import tkinter
    import pickle
    from pathlib import Path
    import os
    import pandas as pd
    import numpy as np

    ACCevokedIPSCtaudf = pd.DataFrame()
    AUDevokedIPSCtaudf = pd.DataFrame()

    ACCevokedIPSC = pd.DataFrame()
    AUDevokedIPSC = pd.DataFrame()
    
    outliers = []
    
    iFolder = 'IPSC'

    dataloc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data")
    savedLoc = dataloc / iFolder
    allnames = os.listdir(savedLoc)
    
    for iCell in allnames:
        print('processing...'+str(iCell)) 
        
        if iCell in outliers:
            continue
   
        #only built to look at RS cells
        if iCell[-2:] == 'IB':
            continue    
        
        # point at data file to view
        cellPath = savedLoc / iCell

        for file in os.listdir(cellPath):
            
            if '_50ms_blue' in file and 'red' not in file:            
                tkinter.Tk().withdraw()
                loadedData = pickle.load(open(cellPath / file, 'rb'))    
                for k in loadedData.keys():
                    if '_data' in k:
                        data = loadedData[k]
                ACCevokedIPSC[iCell] = data
                          
            if '_50ms_red' in file and 'blue' not in file:       
                tkinter.Tk().withdraw()
                loadedData = pickle.load(open(cellPath / file, 'rb'))        
                for k in loadedData.keys():
                    if '_data' in k:
                        data = loadedData[k]
                AUDevokedIPSC[iCell] = data 


    for iData in[ACCevokedIPSC,AUDevokedIPSC]:
        for cell in iData.columns:
            
            set1 = np.asarray(iData[cell][995:2000])
            set2 = np.asarray(iData[cell][1000:2005])
            derv = (set2 - set1)/5
                     
            thresh = 3
        
            r = np.arange(len(derv))
            for index in r:
                if derv[index] < thresh :
                    continue
                if derv[index] >= thresh:
                    startEPSP = (index + 2)
                    break
        

            shortData = iData[cell][700:2200]
            peakLoc = np.argmax(shortData) + 700
    
            rise = shortData[peakLoc]*0.632
            
            for x in list(shortData.index):
                if shortData[x] < rise:
                    continue
                if shortData[x] >= rise:
                    tauidx = x
                    break
            
            startidx = 1000 + startEPSP
            idx = tauidx - startidx
            
            tau = idx / 10
            
            if iData.equals(ACCevokedIPSC):
                ACCevokedIPSCtaudf.at[cell,'rise'] = tau
            if iData.equals(AUDevokedIPSC):
                AUDevokedIPSCtaudf.at[cell,'rise'] = tau
                
                
    for iData in[ACCevokedIPSC,AUDevokedIPSC]:
        
        for cell in iData.columns:
            
            shortData = iData[cell][700:2200]
            peakLoc = np.argmax(shortData) + 700
    
            decay = shortData[peakLoc]*0.368
            idx = (np.abs(shortData[peakLoc-700:]-decay)).argmin() + peakLoc

            
            tau = (idx - peakLoc) / 10
            
            if iData.equals(ACCevokedIPSC):
                ACCevokedIPSCtaudf.at[cell,'decay'] = tau
            if iData.equals(AUDevokedIPSC):
                AUDevokedIPSCtaudf.at[cell,'decay'] = tau
      
     
    return ACCevokedIPSCtaudf, AUDevokedIPSCtaudf


#%%
    
def getTTX(fiberTypes, cellType, failed, legend):
    
    import tkinter
    from tkinter.filedialog import askopenfilename
    import pickle
    from pathlib import Path
    
    
    if failed == True:
        if 'A1' in fiberTypes and 'V1' in fiberTypes:
            savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\TTX experiments\TTX A1_V1 removed\all nonrecovery")
        if 'A1' in fiberTypes and 'ACC' in fiberTypes:
            savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\TTX experiments\TTX A1_ACC removed\all nonrecovery")
        if 'V1' in fiberTypes and 'ACC' in fiberTypes:
            savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\TTX experiments\TTX V1_ACC removed\all nonrecovery")
    
    if failed == False:
        if 'A1' in fiberTypes and 'V1' in fiberTypes:
            savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\TTX experiments\TTX A1_V1")
        if 'A1' in fiberTypes and 'ACC' in fiberTypes:
            savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\TTX experiments\TTX A1_ACC")
        if 'V1' in fiberTypes and 'ACC' in fiberTypes:
            savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\TTX experiments\TTX V1_ACC")    


    # make a list with all folder names including cellType:
    import os
    allnames = os.listdir(savedLoc)
    selectednames = [x for x in allnames if cellType in x]
    
    
    import pandas as pd
    import numpy as np


    peakData = pd.DataFrame({'cell ID':[*selectednames]}).set_index('cell ID')
    
    
    for i in selectednames:
        print('processing...'+str(i)) 
        # point at data file to view
        cellPath = savedLoc / i
        workspacedf = pd.DataFrame()

        for file in os.listdir(cellPath):
            if 'pre' in file:
                tkinter.Tk().withdraw()
                loadedData = pickle.load(open(cellPath / file, 'rb'))
                for k in loadedData.keys():
                    if '_data' in k:
                        workspacedf['pre'] = loadedData[k] 
                    if 'StimTime' in k:
                        delay = int(float(loadedData[k][1])*10000)
                        
                        
            if 'TTX' in file:
                tkinter.Tk().withdraw()
                loadedData = pickle.load(open(cellPath / file, 'rb'))
                for k in loadedData.keys():
                    if '_data' in k:
                        workspacedf['TTX'] = loadedData[k]           
                        
            if '4AP' in file:
                tkinter.Tk().withdraw()
                loadedData = pickle.load(open(cellPath / file, 'rb'))
                for k in loadedData.keys():
                    if '_data' in k:
                        workspacedf['4AP'] = loadedData[k] 
                        
            if 'GLU' in file:
                tkinter.Tk().withdraw()
                loadedData = pickle.load(open(cellPath / file, 'rb'))
                for k in loadedData.keys():
                    if '_data' in k:
                        workspacedf['GLU'] = loadedData[k] 
        
        
    
        maxlocPreF1 = np.argmax(workspacedf['pre'][1000:1300],axis = 0)
        PreF1BL = abs(np.mean(workspacedf['pre'][990:999],axis = 0))
        maxValPreF1 = abs(np.mean(workspacedf['pre'][maxlocPreF1+997 : maxlocPreF1+1003], 0))
        maxValPreF1BL = maxValPreF1 - PreF1BL
        
        maxlocPreF2 = np.argmax(workspacedf['pre'][delay:delay+300],axis = 0)
        PreF2BL = abs(np.mean(workspacedf['pre'][delay-10:delay-1],axis = 0))
        maxValPreF2 = abs(np.mean(workspacedf['pre'][maxlocPreF2+997 : maxlocPreF2+1003], 0))
        maxValPreF2BL = maxValPreF2- PreF2BL
        
        maxlocTTXF1 = np.argmax(workspacedf['TTX'][1000:1300],axis = 0)
        TTXF1BL = abs(np.mean(workspacedf['TTX'][990:999],axis = 0))
        maxValTTXF1 = abs(np.mean(workspacedf['TTX'][maxlocTTXF1+997 : maxlocTTXF1+1003], 0))
        maxValTTXF1BL = maxValTTXF1 - TTXF1BL
        
        maxlocTTXF2 = np.argmax(workspacedf['TTX'][delay:delay+300],axis = 0)
        TTXF2BL = abs(np.mean(workspacedf['TTX'][delay-10:delay-1],axis = 0))
        maxValTTXF2 = abs(np.mean(workspacedf['TTX'][maxlocTTXF2+997 : maxlocTTXF2+1003], 0))
        maxValTTXF2BL = maxValTTXF2- TTXF2BL            
    
        maxloc4APF1 = np.argmax(workspacedf['4AP'][1000:1300],axis = 0)
        FAPF1BL = abs(np.mean(workspacedf['4AP'][990:999],axis = 0))
        maxVal4APF1 = abs(np.mean(workspacedf['4AP'][maxloc4APF1+997 : maxloc4APF1+1003], 0))
        maxVal4APF1BL = maxVal4APF1 - FAPF1BL
        
        maxloc4APF2 = np.argmax(workspacedf['4AP'][delay:delay+300],axis = 0)
        FAPF2BL = abs(np.mean(workspacedf['4AP'][delay-10:delay-1],axis = 0))
        maxVal4APF2 = abs(np.mean(workspacedf['4AP'][maxloc4APF2+997 : maxloc4APF2+1003], 0))
        maxVal4APF2BL = maxVal4APF2- FAPF2BL            

        maxlocGLUF1 = np.argmax(workspacedf['GLU'][1000:1300],axis = 0)
        GLUF1BL = abs(np.mean(workspacedf['GLU'][990:999],axis = 0))
        maxValGLUF1 = abs(np.mean(workspacedf['GLU'][maxlocGLUF1+997 : maxlocGLUF1+1003], 0))
        maxValGLUF1BL = maxValGLUF1 - GLUF1BL
        
        maxlocGLUF2 = np.argmax(workspacedf['GLU'][delay:delay+300],axis = 0)
        GLUF2BL = abs(np.mean(workspacedf['GLU'][delay-10:delay-1],axis = 0))
        maxValGLUF2 = abs(np.mean(workspacedf['GLU'][maxlocGLUF2+997 : maxlocGLUF2+1003], 0))
        maxValGLUF2BL = maxValGLUF2- GLUF2BL            
               

            
        if 'A1_ACC' in str(cellPath) and 'F1A1' in file:
            firstFiber = 'A1'
            secondFiber = 'ACC'
        elif 'A1_ACC' in str(cellPath) and 'F1ACC' in file:
            firstFiber = 'ACC'
            secondFiber = 'A1'
                        


        elif 'V1_ACC' in str(cellPath) and 'F1V1' in file:
            firstFiber = 'V1'
            secondFiber = 'ACC'
        elif 'V1_ACC' in str(cellPath) and 'F1ACC' in file:
            firstFiber = 'ACC'
            secondFiber = 'V1'     


        elif 'A1_V1' in str(cellPath) and 'F1A1' in file:
            firstFiber = 'A1'
            secondFiber = 'V1'
        elif 'A1_V1' in str(cellPath) and 'F1V1' in file:
            firstFiber = 'V1'
            secondFiber = 'A1'     


        peakData.at[str(i),firstFiber+'_pre'] = maxValPreF1BL
        peakData.at[str(i),secondFiber+'_pre'] = maxValPreF2BL
        peakData.at[str(i),firstFiber+'_TTX'] = maxValTTXF1BL
        peakData.at[str(i),secondFiber+'_TTX'] = maxValTTXF2BL            
        peakData.at[str(i),firstFiber+'_4AP'] = maxVal4APF1BL
        peakData.at[str(i),secondFiber+'_4AP'] = maxVal4APF2BL                
        peakData.at[str(i),firstFiber+'_GLU'] = maxValGLUF1BL
        peakData.at[str(i),secondFiber+'_GLU'] = maxValGLUF2BL
        
        
        names = peakData.index
        values = peakData.columns
    
    
    firstData = peakData.loc[:,[firstFiber+'_pre',firstFiber+'_TTX',firstFiber+'_4AP',firstFiber+'_GLU']]
    secondData = peakData.loc[:,[secondFiber+'_pre',secondFiber+'_TTX',secondFiber+'_4AP',secondFiber+'_GLU']]
    meanFirst = firstData.mean(0)
    meanSecond = secondData.mean(0)
    
    
    from matplotlib import pyplot as plt
    plt.figure(figsize=(5,5))
    plt.ylim(0,18)
    names = firstData.columns
    plt.bar(names,meanFirst,alpha = 0.5)
    plt.text(3.3, 13, 'n = '+str(len(firstData)), fontsize=14)
    plt.title(cellType + ' '+firstFiber+' '+secondFiber)
    for i in firstData.index:
        values = firstData.loc[i,names]
        plt.plot(names,values)
        plt.scatter(names,values,s = 80, facecolors='none')
    if legend == 1:
        plt.legend()    


    plt.figure(figsize=(5,5))
    plt.ylim(0,18)
    names = secondData.columns
    plt.text(3.3, 13, 'n = '+str(len(secondData)), fontsize=14)
    plt.bar(names,meanSecond,alpha = 0.5)
    plt.title(cellType + ' '+firstFiber+' '+secondFiber)
    for i in secondData.index:
        values = secondData.loc[i,names]
        plt.plot(names,values)
        plt.scatter(names,values,s = 80, facecolors='none')
    if legend == 1:
        plt.legend() 
    
    
    return peakData

#%%
        
def ppcPie(opsinSwapList):

    
    #run code to pick out all latencies - look through all folders (sub integration, mechanism, single fiber, TTX) - include FAILED LATENCY folders too
        #make histogram of ALL latencies (maybe two peaks)
        
        #print out cells (from sub integration, mechanism, single fiber,) that fail latency test (>4ms)
            #say whether failed cells in main folder or already in removed folder - this lets us go back and place cells in appropriate folder manually
            #somehow has to handle if same cell in multiple experiments
            
            
         #current policy is most stringent, that if cell fails either TTX or latency test, is removed    
            
            
        #print out cells (from sub integration, mechanism, single fiber) that fail TTX test (XX %recovery)
            #say if failed cells also found in main folder or also found in already in removed folder - this lets us go back and place cells in appropriate folder manually
        
        #from TTX folder, run code to get latencies of pharmacologically confirmed non-monosynaptic cells with no recovery from TTX
        
        #make color coded overlayed histogram with latencies of all cells and those that failed TTX test

        
        #count all cells
        #count cells in removed TTX and removed latency folders and cells failing TTX that aren't in those folders
        #add cells manually that didn't recieve both inputs and therefore didn't record (from notes)
        #make pie charts


    #pick out all latencies - look through all folders (sub integration, mechanism, single fiber, TTX) - include FAILED LATENCY folders too
    
    
#puts all latencies (except TTX experiments) in latdf folder
    import tkinter
    from tkinter.filedialog import askopenfilename
    import pickle
    from pathlib import Path
    import os
    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt
    
    
    latdf = {}
    
    latdf['ACC'] = pd.DataFrame()
    latdf['A1'] = pd.DataFrame()
    latdf['V1'] = pd.DataFrame()

    
    for iFolder in ['integration A1_ACC', 'integration V1_ACC', 'integration A1_V1',
                    'integration A1_ACC removed/Reason is latency',
                    'integration V1_ACC removed/Reason is latency',
                    'integration A1_V1 removed/Reason is latency',]:
        
        dataloc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data")
        savedLoc = dataloc / iFolder
        allnames = os.listdir(savedLoc)
        
        for iCell in allnames:
            print('processing...'+str(iCell)) 
            
            # point at data file to view
            cellPath = savedLoc / iCell
    
            for file in os.listdir(cellPath):
                
                if '_0ms_blue' in file and 'red' not in file:
                    
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    
                    for k in loadedData.keys():
                        if '_data' in k:
                            data = loadedData[k]
    
                    #place the data into the appropriate df
                    if 'integration A1_ACC' in iFolder:
                        if iCell not in opsinSwapList:
                            latdf['ACC'][str(iCell)] = data
                        if iCell in opsinSwapList:
                            latdf['A1'][str(iCell)] = data
                            
                    if 'integration V1_ACC' in iFolder:
                        if iCell not in opsinSwapList:
                            latdf['ACC'][str(iCell)] = data
                        if iCell not in opsinSwapList:
                            latdf['V1'][str(iCell)] = data
                           
                    if 'integration A1_V1' in iFolder:
                        if iCell not in opsinSwapList:
                            latdf['V1'][str(iCell)] = data
                        if iCell not in opsinSwapList:
                            latdf['A1'][str(iCell)] = data

                                  
                if '_0ms_red' in file:       
                        
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    
                    for k in loadedData.keys():
                        if '_data' in k:
                            data = loadedData[k]
    
                    #place the data into the appropriate df
                    if 'integration A1_ACC' in iFolder:
                        if iCell not in opsinSwapList:
                            latdf['A1'][str(iCell)] = data
                        if iCell in opsinSwapList:
                            latdf['ACC'][str(iCell)] = data
                            
                    if 'integration V1_ACC' in iFolder:
                        if iCell not in opsinSwapList:
                            latdf['V1'][str(iCell)] = data
                        if iCell not in opsinSwapList:
                            latdf['ACC'][str(iCell)] = data
                           
                    if 'integration A1_V1' in iFolder:
                        if iCell not in opsinSwapList:
                            latdf['A1'][str(iCell)] = data
                        if iCell not in opsinSwapList:
                            latdf['V1'][str(iCell)] = data

                                              
    for iFolder in ['double A1', 'double V1', 'double ACC']:
        
        dataloc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data")
        savedLoc = dataloc / iFolder
        allnames = os.listdir(savedLoc)
        
        for iCell in allnames:
            print('processing...'+str(iCell)) 
            
            # point at data file to view
            cellPath = savedLoc / iCell
    
            for file in os.listdir(cellPath):
                
                if iFolder == 'double A1':      
                    
                    if '_50ms_red' in file and 'redred' not in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                data = loadedData[k]
                                
                        latdf['A1'][str(iCell)] = data
                        
                    if '_50ms_blue' in file and 'blueblue' not in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                data = loadedData[k]
                                
                        latdf['A1'][str(iCell)] = data

                if iFolder == 'double ACC':              
                    
                    if '_50ms_red' in file and 'redred' not in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                data = loadedData[k]
                                
                        latdf['ACC'][str(iCell)] = data
                        
                    if '_50ms_blue' in file and 'blueblue' not in file:    
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                data = loadedData[k]
                                
                        latdf['ACC'][str(iCell)] = data

                if iFolder == 'double V1':
                    
                    if '_50ms_red' in file and 'redred' not in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                data = loadedData[k]
                                
                        latdf['V1'][str(iCell)] = data
                        
                    if '_50ms_blue' in file and 'blueblue' not in file:    
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                data = loadedData[k]
                                
                        latdf['V1'][str(iCell)] = data
                       
                        
 
    for iFolder in ['integration A1_ACC mechanism/AP5', 'integration A1_ACC mechanism/mibefradil', 'integration A1_ACC mechanism/TTX',
                    'integration A1_ACC mechanism/time control',
                    'integration A1_ACC mechanism removed/Reason is latency/AP5',
                    'integration A1_ACC mechanism removed/Reason is latency/TTX',
                    'integration A1_ACC mechanism removed/Reason is latency/mibefradil']:
        
        dataloc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data")
        savedLoc = dataloc / iFolder
        allnames = os.listdir(savedLoc)
        
        for iCell in allnames:
            print('processing...'+str(iCell)) 
            
            # point at data file to view
            cellPath = savedLoc / iCell
            
            
            #assumes all cells in this paradigm are default (ACC ChR2, A1 Chrimson) 
            if any('_0ms' in s for s in os.listdir(cellPath)) == True:
                
                for file in os.listdir(cellPath):
                    
                    if '_0ms_red' in file and 'redred' not in file and 'red_' not in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                data = loadedData[k]
                            
                        latdf['A1'][str(iCell)] = data
                                           
                    if '_0ms_blue' in file and 'blueblue' not in file and 'blue_' not in file: 
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                data = loadedData[k]
                            
                        latdf['ACC'][str(iCell)] = data 
                    
                    
            if any('_0ms' in s for s in os.listdir(cellPath)) == False:
                
                for file in os.listdir(cellPath):
                    
                    if '_50ms_red' in file and 'redred' not in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                data = loadedData[k]
                            
                        latdf['A1'][str(iCell)] = data
                                           
                    if '_50ms_blue' in file and 'blueblue' not in file:    
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                data = loadedData[k]
                        
                        latdf['ACC'][str(iCell)] = data
                


#and more!!
    for iFolder in ['suprathreshold A1_ACC']:
        
        dataloc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data")
        savedLoc = dataloc / iFolder
        allnames = os.listdir(savedLoc)
        
        for iCell in allnames:
            print('processing...'+str(iCell)) 
                        
            #assumes all cells in this paradigm are default (ACC ChR2, A1 Chrimson) 
            cellPath = savedLoc / iCell
    
            for file in os.listdir(cellPath):
                for delay in ['_250ms_',
                              '_100ms_',
                              '_50ms_',
                              '_0ms_']:
                    
                    if any(delay in s for s in os.listdir(cellPath)):
                        if delay+'blue' in file and 'red' not in file:
                            
                            tkinter.Tk().withdraw()
                            loadedData = pickle.load(open(cellPath / file, 'rb'))
                            
                            for k in loadedData.keys():
                                if '_data' in k:
                                    data = loadedData[k]
            
                            #place the data into the appropriate df
        
                            latdf['ACC'][str(iCell)] = data.mean(axis=1)
        
                                    
                        if delay+'red' in file:       
                                
                            tkinter.Tk().withdraw()
                            loadedData = pickle.load(open(cellPath / file, 'rb'))
                            
                            for k in loadedData.keys():
                                if '_data' in k:
                                    data = loadedData[k]
            
                            #place the data into the appropriate df
        
                            latdf['A1'][str(iCell)] = data.mean(axis=1)

                

    
#TTX experiments, data organized into folders manually for if pass/fail TTX test
#use this classification to find latencies for those exact cells
#create two new dictionaries with cells that pass TTX and cells that don't pass TTX
#overlay passing TTX and failing TTX on all cells histogram in green and red

    #cells that pass TTX
    passTTX = {}
    passTTX['A1'] = pd.DataFrame()
    passTTX['ACC'] = pd.DataFrame()
    passTTX['V1'] = pd.DataFrame()
    
    #cells that fail TTX, doesn't seperate by which fiber failed!
    failTTX = {}
    failTTX['A1'] = pd.DataFrame()
    failTTX['ACC'] = pd.DataFrame()
    failTTX['V1'] = pd.DataFrame()


    for iFolder in ['TTX experiments/TTX A1_ACC', 'TTX experiments/TTX V1_ACC', 'TTX experiments/TTX A1_V1',
                    'TTX experiments/TTX A1_ACC removed/A1 nonrecovery', 'TTX experiments/TTX A1_ACC removed/ACC nonrecovery',
                    'TTX experiments/TTX V1_ACC removed/V1 nonrecovery', 'TTX experiments/TTX V1_ACC removed/ACC nonrecovery',
                    'TTX experiments/TTX A1_V1 removed/A1 nonrecovery', 'TTX experiments/TTX A1_V1 removed/V1 nonrecovery']:
                    
    
        dataloc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data")
        savedLoc = dataloc / iFolder
        allnames = os.listdir(savedLoc)
        
        for iCell in allnames:
            print('processing...'+str(iCell)) 
            
            # point at data file to view
            cellPath = savedLoc / iCell
            
            if 'removed' not in iFolder:
                for file in os.listdir(cellPath):
                    if '_pre' in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                data = loadedData[k]
                            if 'StimTime' in k:
                                delay = int(10000*float(loadedData[k][1]))
                                start = delay - 1000
                                
                        if file.split('F1')[1][0:2] == 'AC':
                            passTTX['ACC'][str(iCell)] = data[0:2500]
                        if file.split('F1')[1][0:2] == 'A1':
                            passTTX['A1'][str(iCell)] = data[0:2500]                        
                        if file.split('F1')[1][0:2] == 'V1':
                            passTTX['V1'][str(iCell)] = data[0:2500]                        
                            
                            
                        if file.split('F2')[1][0:2] == 'AC':    
                            passTTX['ACC'][str(iCell)] = data[start:2500+start]
                        if file.split('F2')[1][0:2] == 'A1':    
                            passTTX['A1'][str(iCell)] = data[start:2500+start]                       
                        if file.split('F2')[1][0:2] == 'V1':
                            passTTX['V1'][str(iCell)] = data[start:2500+start]   
    
            if 'removed' in iFolder:
                for file in os.listdir(cellPath):
                    if '_pre' in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                data = loadedData[k]
                            if 'StimTime' in k:
                                delay = int(10000*float(loadedData[k][1]))
                                start = delay - 1000
                                
                        if file.split('F1')[1][0:2] == 'AC':
                            failTTX['ACC'][str(iCell)] = data[0:2500]
                        if file.split('F1')[1][0:2] == 'A1':
                            failTTX['A1'][str(iCell)] = data[0:2500]                        
                        if file.split('F1')[1][0:2] == 'V1':
                            failTTX['V1'][str(iCell)] = data[0:2500]                        
                            
                            
                        if file.split('F2')[1][0:2] == 'AC':    
                            failTTX['ACC'][str(iCell)] = data[start:2500+start]
                        if file.split('F2')[1][0:2] == 'A1':    
                            failTTX['A1'][str(iCell)] = data[start:2500+start]                       
                        if file.split('F2')[1][0:2] == 'V1':
                            failTTX['V1'][str(iCell)] = data[start:2500+start]



    #add all the failed and passing TTX cells to the total data set
    for iDict in [failTTX, passTTX]:
        for k, v in iDict.items():
            for i in v:
                latdf[k][i] = v[i]
    #latdf now has every single cell, including passing and failing both TTX and latency



#get rise of cells where both inputs pass TTX
    passRise = {}
    passRise['A1'] = pd.DataFrame()
    passRise['ACC'] = pd.DataFrame()
    passRise['V1'] = pd.DataFrame()

    for k, v in passTTX.items():
        for i in v:
            set1 = np.asarray(passTTX[k][i][995:2000])
            set2 = np.asarray(passTTX[k][i][1000:2005])
            derv = (set2 - set1)/5
                     
            thresh = 0.04

            r = np.arange(len(derv))
            for index in r:
                derv[index]
                if derv[index] < thresh :
                    continue
                if derv[index] >= thresh:
                    passRise[k].at['0',i] = (index + 2 - 5)/10
                    break
    

#NOW get list of which fiber failed during TTX experiments
    test = {}
    test['A1']=[]
    test['ACC']=[]
    test['V1']=[]
    
     
    for iFolder in ['TTX experiments/TTX A1_ACC removed/A1 nonrecovery', 'TTX experiments/TTX A1_ACC removed/ACC nonrecovery',
                    'TTX experiments/TTX V1_ACC removed/V1 nonrecovery', 'TTX experiments/TTX V1_ACC removed/ACC nonrecovery',
                    'TTX experiments/TTX A1_V1 removed/A1 nonrecovery', 'TTX experiments/TTX A1_V1 removed/V1 nonrecovery']:
                    
        dataloc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data")
        savedLoc = dataloc / iFolder
        allnames = os.listdir(savedLoc)
        
        for iCell in allnames:
            nonrecovery = iFolder.find('nonrecovery')
            removed = iFolder.find('removed')
            if iFolder[removed+8:nonrecovery-1] == 'A1':
                test['A1'].extend([iCell])
            if iFolder[removed+8:nonrecovery-1] == 'ACC':
                test['ACC'].extend([iCell])        
            if iFolder[removed+8:nonrecovery-1] == 'V1':
                test['V1'].extend([iCell])
         
            
            
#get latencies of the fiber that failed during TTX experiments    
    failRise = {}
    failRise['A1'] = pd.DataFrame()
    failRise['ACC'] = pd.DataFrame()
    failRise['V1'] = pd.DataFrame()
        
    for k, v in failTTX.items():
        for i in v:
            set1 = np.asarray(failTTX[k][i][995:2000])
            set2 = np.asarray(failTTX[k][i][1000:2005])
            derv = (set2 - set1)/5
                     
            thresh = 0.04
            
            r = np.arange(len(derv))
            for index in r:
                derv[index]
                if derv[index] < thresh :
                    continue
                if derv[index] >= thresh:
                    if i in test[k]:
                        failRise[k].at['0',i] = (index + 2 - 5)/10
                    
                    #add the other fiber that passed into passRise
                    if i not in test[k]:
                        passRise[k].at['0',i] = (index + 2 - 5)/10
                        
                    break





#find latency of all fibers for cells (including TTX pass/fail) from latdf    
    rise = {}
    rise['A1'] = pd.DataFrame()
    rise['ACC'] = pd.DataFrame()
    rise['V1'] = pd.DataFrame()

    for k, v in latdf.items():
        for i in v:
            set1 = np.asarray(latdf[k][i][995:2000])
            set2 = np.asarray(latdf[k][i][1000:2005])
            derv = (set2 - set1)/5
                     
            thresh = 0.04

            r = np.arange(len(derv))
            for index in r:
                derv[index]
                if derv[index] < thresh :
                    continue
                if derv[index] >= thresh:
                    rise[k].at['0',i] = (index + 2 - 5)/10
                    break


#plot all cells for each fibers
    for fiber in ['A1', 'ACC', 'V1']:
        plt.figure()
        x, bins, z = plt.hist(rise[fiber], bins = [0,1,2,3,4,5,6,7,8,9,10,11,12], alpha = 0.5)
        plt.title(fiber)
        plt.xlabel('EPSP latency (ms)')
        plt.ylabel('number of cells')
        plt.xlim(-0.5,9)
        plt.ylim(-5,69)
        xmin, xmax, ymin, ymax = plt.axis()
        plt.vlines(0,-1,ymax,color = 'k', linestyles='dashed')
        plt.xlim(left = -1)
        plt.axhline(color='k')
        
        passed = passRise[fiber]
        plt.hist(passed, bins = [0,1,2,3,4,5,6,7,8,9,10,11,12], alpha = 0.5)
        failed = failRise[fiber]
        plt.hist(failed, bins = [0,1,2,3,4,5,6,7,8,9,10,11,12], alpha = 0.5)        
        
#plot all cells for all fibers together
    allInputs = pd.concat([rise['A1'],rise['ACC'],rise['V1']],axis=1) #for all inputs
#    allInputs = pd.concat([rise['A1'],rise['ACC']],axis=1) #for when we make NRSA figure, only A1/ACC inputs
    plt.figure()
    x, bins, z = plt.hist(allInputs, bins = [0,1,2,3,4,5,6,7,8,9,10,11,12], alpha = 0.5)
    plt.title('All synaptic input')
    plt.xlabel('EPSP latency (ms)')
    plt.ylabel('number of cells')
    xmin, xmax, ymin, ymax = plt.axis()
    plt.vlines(0,-1,ymax,color = 'k', linestyles='dashed')
    plt.xlim(left = -1)
    plt.axhline(color='k')    
    
#overlay cells that passed TTX and cells that failed TTX
    allPass = pd.concat([passRise['A1'],passRise['ACC'],passRise['V1']],axis=1)
    plt.hist(allPass, bins = [0,1,2,3,4,5,6,7,8,9,10,11,12], alpha = 0.5)

    allFail = pd.concat([failRise['A1'],failRise['ACC'],failRise['V1']],axis=1)
    plt.hist(allFail, bins = [0,1,2,3,4,5,6,7,8,9,10,11,12], alpha = 0.5)
    
                  
             #if the latency failing cell isn't in one of the folders assuming it passes, then in right place!!

#            

#%%
            
def cellTypeMonoPie(opsinSwapList):      
    
#puts all latencies (except TTX experiments) in latdf folder
    import tkinter
    from tkinter.filedialog import askopenfilename
    import pickle
    from pathlib import Path
    import os
    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt
    
  
    alldf = {}
    
    alldf['A1_ACC'] = {}
    alldf['V1_ACC'] = {}
    alldf['A1_V1'] = {}
    

#add some traces    
    for iFolder in ['integration A1_ACC', 'integration V1_ACC', 'integration A1_V1',
                    'integration A1_ACC removed/Reason is latency',
                    'integration V1_ACC removed/Reason is latency',
                    'integration A1_V1 removed/Reason is latency',]:
        
        dataloc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data")
        savedLoc = dataloc / iFolder
        allnames = os.listdir(savedLoc)
        
        for iCell in allnames:
            print('processing...'+str(iCell)) 
            
            # point at data file to view
            cellPath = savedLoc / iCell
            
            
            if 'integration A1_ACC' in iFolder:
                alldf['A1_ACC'][iCell] = {}
                
                for file in os.listdir(cellPath):
                    
                    if '_0ms_blue' in file and 'red' not in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        
                        for k in loadedData.keys():
                            if '_data' in k:
                                data = loadedData[k]
              
                                if iCell not in opsinSwapList:
                                    alldf['A1_ACC'][iCell]['ACC']= data
                                if iCell in opsinSwapList:
                                    alldf['A1_ACC'][iCell]['A1']= data
          
                    if '_0ms_red' in file:       
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        
                        for k in loadedData.keys():
                            if '_data' in k:
                                data = loadedData[k]
                  
                                if iCell not in opsinSwapList:
                                    alldf['A1_ACC'][iCell]['A1']= data
                                if iCell in opsinSwapList:
                                    alldf['A1_ACC'][iCell]['ACC']= data                        
                        
                        
            if 'integration V1_ACC' in iFolder:
                alldf['V1_ACC'][iCell] = {}
                
                for file in os.listdir(cellPath):
                    
                    if '_0ms_blue' in file and 'red' not in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        
                        for k in loadedData.keys():
                            if '_data' in k:
                                data = loadedData[k]
              
                                if iCell not in opsinSwapList:
                                    alldf['V1_ACC'][iCell]['ACC']= data
                                if iCell in opsinSwapList:
                                    alldf['V1_ACC'][iCell]['V1']= data
          
                    if '_0ms_red' in file:       
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        
                        for k in loadedData.keys():
                            if '_data' in k:
                                data = loadedData[k]
              
                                if iCell not in opsinSwapList:
                                    alldf['V1_ACC'][iCell]['V1']= data
                                if iCell in opsinSwapList:
                                    alldf['V1_ACC'][iCell]['ACC']= data                         
                        
                        
            if 'integration A1_V1' in iFolder:
                alldf['A1_V1'][iCell] = {}
                
                for file in os.listdir(cellPath):
                    
                    if '_0ms_blue' in file and 'red' not in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        
                        for k in loadedData.keys():
                            if '_data' in k:
                                data = loadedData[k]
                  
                                if iCell not in opsinSwapList:
                                    alldf['A1_V1'][iCell]['V1']= data
                                if iCell in opsinSwapList:
                                    alldf['A1_V1'][iCell]['A1']= data
          
                    if '_0ms_red' in file:       
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        
                        for k in loadedData.keys():
                            if '_data' in k:
                                data = loadedData[k]
              
                                if iCell not in opsinSwapList:
                                    alldf['A1_V1'][iCell]['A1']= data
                                if iCell in opsinSwapList:
                                    alldf['A1_V1'][iCell]['V1']= data                         
                                                

    
#add more traces   
    for iFolder in ['integration A1_ACC mechanism/AP5', 'integration A1_ACC mechanism/mibefradil', 'integration A1_ACC mechanism/TTX','integration A1_ACC mechanism/PTX',
                    'integration A1_ACC mechanism/time control',
                    'integration A1_ACC mechanism removed/Reason is latency/AP5',
                    'integration A1_ACC mechanism removed/Reason is latency/TTX',
                    'integration A1_ACC mechanism removed/Reason is latency/mibefradil']:
        
        dataloc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data")
        savedLoc = dataloc / iFolder
        allnames = os.listdir(savedLoc)
        
        for iCell in allnames:
            print('processing...'+str(iCell)) 
            
            # point at data file to view
            cellPath = savedLoc / iCell
            
            alldf['A1_ACC'][iCell] = {}
            
            
            #assumes all cells in this paradigm are default (ACC ChR2, A1 Chrimson) 
            if any('_0ms' in s for s in os.listdir(cellPath)) == True:
                
                for file in os.listdir(cellPath):
                    
                    if '_0ms_red' in file and 'redred' not in file and 'red_' not in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                data = loadedData[k]
                            
                        alldf['A1_ACC'][iCell]['A1'] = data
                                           
                    if '_0ms_blue' in file and 'blueblue' not in file and 'blue_' not in file: 
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                data = loadedData[k]
                            
                        alldf['A1_ACC'][iCell]['ACC'] = data
                    
                    
            if any('_0ms' in s for s in os.listdir(cellPath)) == False:
                
                for file in os.listdir(cellPath):
                    
                    if '_50ms_red' in file and 'redred' not in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                data = loadedData[k]
                            
                        alldf['A1_ACC'][iCell]['A1'] = data
                                           
                    if '_50ms_blue' in file and 'blueblue' not in file:    
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                data = loadedData[k]
                        
                        alldf['A1_ACC'][iCell]['ACC'] = data
                

#add even more traces! 
    for iFolder in ['TTX experiments/TTX A1_ACC', 'TTX experiments/TTX V1_ACC', 'TTX experiments/TTX A1_V1',
                    'TTX experiments/TTX A1_ACC removed/A1 nonrecovery', 'TTX experiments/TTX A1_ACC removed/ACC nonrecovery',
                    'TTX experiments/TTX V1_ACC removed/V1 nonrecovery', 'TTX experiments/TTX V1_ACC removed/ACC nonrecovery',
                    'TTX experiments/TTX A1_V1 removed/A1 nonrecovery', 'TTX experiments/TTX A1_V1 removed/V1 nonrecovery']:
                    
    
        dataloc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data")
        savedLoc = dataloc / iFolder
        allnames = os.listdir(savedLoc)
        
        for iCell in allnames:
            print('processing...'+str(iCell)) 
            
            # point at data file to view
            cellPath = savedLoc / iCell
            
            
            if 'A1_ACC' in iFolder:
                alldf['A1_ACC'][iCell] = {}
            if 'V1_ACC' in iFolder:
                alldf['V1_ACC'][iCell] = {}            
            if 'A1_V1' in iFolder:
                alldf['A1_V1'][iCell] = {}            

            for file in os.listdir(cellPath):
                if '_pre' in file:
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    for k in loadedData.keys():
                        if '_data' in k:
                            data = loadedData[k]
                        if 'StimTime' in k:
                            delay = int(10000*float(loadedData[k][1]))
                            start = delay - 1000
                            
                    if 'A1_ACC' in iFolder:        
                        if file.split('F1')[1][0:2] == 'AC':
                            alldf['A1_ACC'][iCell]['ACC'] = data[0:2500]
                        if file.split('F1')[1][0:2] == 'A1':
                            alldf['A1_ACC'][iCell]['A1'] = data[0:2500] 
                            
                        if file.split('F2')[1][0:2] == 'AC':    
                            alldf['A1_ACC'][iCell]['ACC'] = data[start:2500+start]
                        if file.split('F2')[1][0:2] == 'A1':    
                            alldf['A1_ACC'][iCell]['A1'] = data[start:2500+start]          
                            
                    if 'V1_ACC' in iFolder:        
                        if file.split('F1')[1][0:2] == 'AC':
                            alldf['V1_ACC'][iCell]['ACC'] = data[0:2500]
                        if file.split('F1')[1][0:2] == 'V1':
                            alldf['V1_ACC'][iCell]['V1'] = data[0:2500] 
                            
                        if file.split('F2')[1][0:2] == 'AC':    
                            alldf['V1_ACC'][iCell]['ACC'] = data[start:2500+start]
                        if file.split('F2')[1][0:2] == 'V1':    
                            alldf['V1_ACC'][iCell]['V1'] = data[start:2500+start]                                 
                            
                    if 'A1_V1' in iFolder:        
                        if file.split('F1')[1][0:2] == 'A1':
                            alldf['A1_V1'][iCell]['A1'] = data[0:2500]
                        if file.split('F1')[1][0:2] == 'V1':
                            alldf['A1_V1'][iCell]['V1'] = data[0:2500] 
                            
                        if file.split('F2')[1][0:2] == 'A1':    
                            alldf['A1_V1'][iCell]['A1'] = data[start:2500+start]
                        if file.split('F2')[1][0:2] == 'V1':    
                            alldf['A1_V1'][iCell]['V1'] = data[start:2500+start]                                 

#and more!!
    for iFolder in ['suprathreshold A1_ACC']:
        
        dataloc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data")
        savedLoc = dataloc / iFolder
        allnames = os.listdir(savedLoc)
        
        for iCell in allnames:
            print('processing...'+str(iCell)) 
            
            alldf['A1_ACC'][iCell] = {}
            
            #assumes all cells in this paradigm are default (ACC ChR2, A1 Chrimson) 
            cellPath = savedLoc / iCell
    
            for file in os.listdir(cellPath):
                for delay in ['_250ms_',
                              '_100ms_',
                              '_50ms_',
                              '_0ms_']:
                    
                    if any(delay in s for s in os.listdir(cellPath)):
                        if delay+'blue' in file and 'red' not in file:
                            
                            tkinter.Tk().withdraw()
                            loadedData = pickle.load(open(cellPath / file, 'rb'))
                            
                            for k in loadedData.keys():
                                if '_data' in k:
                                    data = loadedData[k]
            
                            #place the data into the appropriate df
        
                            alldf['A1_ACC'][iCell]['ACC'] = data.mean(axis=1)
        
                                    
                        if delay+'red' in file:       
                                
                            tkinter.Tk().withdraw()
                            loadedData = pickle.load(open(cellPath / file, 'rb'))
                            
                            for k in loadedData.keys():
                                if '_data' in k:
                                    data = loadedData[k]
            
                            #place the data into the appropriate df
        
                            alldf['A1_ACC'][iCell]['A1'] = data.mean(axis=1)
                        
            
#get rise of all cells
    allRise = {}

    for k, v in alldf.items():
        allRise[k] = {}
        
        for l, b in v.items():
            allRise[k][l] = {}
            
            for j, c in b.items():
                
                
                set1 = np.asarray(alldf[k][l][j][995:2000])
                set2 = np.asarray(alldf[k][l][j][1000:2005])
                derv = (set2 - set1)/5
                         
                thresh = 0.04
    
                r = np.arange(len(derv))
                for index in r:
                    derv[index]
                    if derv[index] < thresh :
                        continue
                    if derv[index] >= thresh:
                        allRise[k][l][j] = (index + 2 - 5)/10
                        break

#count failures
    allCounts = {}
    failedNames = []
    
    latencyThreshold = 4
                    
    for k, v in allRise.items():
        fiber1 = k.split('_')[0]
        fiber2 = k.split('_')[1]
        
        allCounts[k] = {
                'IB' : {'dual pass':0,
                        'dual fail':0,
                        fiber1+' fails':0,
                        fiber2+' fails':0},
                        
                'RS' : {'dual pass':0,
                        'dual fail':0,
                        fiber1+' fails':0,
                        fiber2+' fails':0}}
        
        for l, b in v.items():
            
            test = [0, 0]
            fiber = [0, 0]
            for index, (j, c) in enumerate(b.items()):
                fiber[index] = j
                if c < latencyThreshold:
                    test[index] = False
                    
                if c >= latencyThreshold:
                    test[index] = True
                    
                if index == 1:
                    if sum(test) == 0:
                        allCounts[k][l[-2:]]['dual pass'] = allCounts[k][l[-2:]]['dual pass'] + 1
                        
                    if sum(test) == 1:
                        xx = fiber[[i for i, x in enumerate(test) if x][0]]
                        allCounts[k][l[-2:]][xx + ' fails'] = allCounts[k][l[-2:]][xx + ' fails'] + 1
                        
                    if sum(test) == 2:
                        allCounts[k][l[-2:]]['dual fail'] = allCounts[k][l[-2:]]['dual fail'] + 1

    for k, v in allCounts.items():
        
        fiber1 = k.split('_')[0]
        fiber2 = k.split('_')[1]
    
        for l, b in v.items():
            
            
            dualPass = b['dual pass']
            x = b[fiber1+' fails']
            y = b[fiber2+' fails']
            dualFail = b['dual fail']
            
            cells = [dualPass, x, y, dualFail]

            totalNum = sum(list(b.values()))

            # Plot pie
            labels = ['Dual monosynaptic', fiber2+' only', fiber1+' only','both fail']
            colors = ['black', 'lightgrey','white','darkgrey']
            plt.figure()
            plt.pie(cells, labels=labels, colors=colors,
                    autopct='%1.1f%%', startangle=140,
                    wedgeprops={"edgecolor":"0",'linewidth': 1, 
                                'antialiased': True})
            plt.axis('equal')
            plt.title(l+ ' ' +k+ ' n=' +str(totalNum))
            plt.show()   
        

            
        # Plot bar
        bothPass = np.array([v['IB']['dual pass'],v['RS']['dual pass']])
        f1Only = np.array([v['IB'][fiber2+' fails'],v['RS'][fiber2+' fails']])
        f2Only = np.array([v['IB'][fiber1+' fails'],v['RS'][fiber1+' fails']])
        bothFail = np.array([v['IB']['dual fail'],v['RS']['dual fail']]) 
        
            
        ind = [0,1]
        totalNumIB = sum(list(v['IB'].values()))
        totalNumRS = sum(list(v['RS'].values()))  
        
        proportion_dual = [None,None]
        proportion_f2only = [None,None]
        proportion_f1only = [None,None]
        proportion_none = [None,None]
        
        proportions = [proportion_dual,
                  proportion_f2only,
                  proportion_f1only,
                  proportion_none]
        
        values = [bothPass,
                  f2Only,
                  f1Only,
                  bothFail]   
        
        for i, c in enumerate(proportions):
            for x in ind:
                if x == 0:
                    c[x] = values[i][x]/totalNumIB *100
                if x == 1:
                    c[x] = values[i][x]/totalNumRS *100
                  
        plt.figure()

        labels = ['Dual monosynaptic', fiber2+' passes', fiber1+' passes','both fail']
        proportion_dual = np.asarray(proportion_dual)
        proportion_f2only = np.asarray(proportion_f2only)
        proportion_f1only = np.asarray(proportion_f1only)
        proportion_none = np.asarray(proportion_none)
        
        p1 = plt.bar(ind, proportion_dual, width=0.8, label = labels[0])
        p2 = plt.bar(ind, proportion_f2only, width=0.8, bottom = proportion_dual, label = labels[1])
        p3 = plt.bar(ind, proportion_f1only, width=0.8, bottom = proportion_dual+proportion_f2only, label = labels[2])
        p4 = plt.bar(ind, proportion_none, width=0.8, bottom = proportion_dual+proportion_f2only+proportion_f1only, label = labels[3])
        

        plt.ylabel('percent of cells')
        plt.title(k)
        plt.xticks(ind, ('IB', 'RS'))
        plt.yticks(np.arange(0, 101, 10))
        plt.legend((p1[0], p2[0], p3[0], p4[0]), labels)
    
                
        plt.show()


    return  allRise, allCounts


#%%

def cellPie():
    
    import tkinter
    from tkinter.filedialog import askopenfilename
    import pickle
    from pathlib import Path
    import os
    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt
    

    allnames = os.listdir(Path(r"Z:\Danny R\Slice Phys\Preprocessed data\current steps\-70\PPC_L5"))

    x = list(allnames)

    IBcount = sum('IB' in s for s in x)
    RScount = sum('RS' in s for s in x)

    # Data to plot for A1 - ACC
    labels = ['IB', 'RS']
    cells = [IBcount, RScount]
    colors = ['darkgrey','lightgrey']
    
    # Plot
    plt.figure()
    plt.pie(cells, labels=labels, colors=colors,
            autopct='%1.1f%%', startangle=140,
            wedgeprops={"edgecolor":"0",'linewidth': 1, 
                        'antialiased': True})

    plt.axis('equal')
    plt.title('total  n=' + str(IBcount+RScount))
    plt.show()        

    
#%%
    
def intMechanismInternal(confidence, cellType, opsinSwapList, oneMapCells, drug, imageloc, show, order, tau, averaging, plots):


    #load data
    #organize data in pairs, pre and post drug
    #get pulse ratios
    #plot with each other, straight line then dotted for post


    import tkinter
    from tkinter.filedialog import askopenfilename
    import pickle


    from pathlib import Path
    
    
    if drug == 'PTX internal':
        savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration A1_ACC mechanism\internal PTX")
    if drug == 'QX314 internal':
        savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration A1_ACC mechanism\internal QX314")


    # make a list with all folder names including cellType:
    import os
    allnames = os.listdir(savedLoc)
    selectednames = [x for x in allnames if cellType in x]
    
    
    import pandas as pd
    import numpy as np
    frontalsensoryData = pd.DataFrame()
    sensoryfrontalData = pd.DataFrame()
    coincidentData = pd.DataFrame()
    
    peakData = pd.DataFrame({'cell ID':[*selectednames]}).set_index('cell ID')
    
    peakData['0ms_frontal single']=""
    peakData['0ms_frontal paired']=""
    peakData['0ms_sensory single']=""
    peakData['0ms_sensory paired']=""
    peakData['50ms_frontal single']=""
    peakData['50ms_frontal paired']=""
    peakData['50ms_sensory single']=""
    peakData['50ms_sensory paired']=""


    for i in selectednames:
        print('processing...'+str(i)) 
        # point at data file to view
        cellPath = savedLoc / i
        workspacedf = pd.DataFrame()
        
        for file in os.listdir(cellPath):      
            for delay in [0,50]:                                    
                if '_'+str(delay)+'ms' in file:
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    for k in loadedData.keys():
                        if '_data' in k:
                            workspacedf[str(delay)+'_'+str(k)] = loadedData[k]

        for delay in [0,50]:        
            if delay == 0:
                try:
                    if i in opsinSwapList:
                        
                        coincidentData['actualCoincident'] = workspacedf[str(delay)+'_'+'paired pulse map_data']
                        coincidentData['arithmeticSum'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf[str(delay)+'_'+'pulse 1 map_data']
                        
                            
                            
                    if i not in opsinSwapList: # same as above if in opsinSwapList
                        
                        coincidentData['actualCoincident'] = workspacedf[str(delay)+'_'+'paired pulse map_data']
                        coincidentData['arithmeticSum'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf[str(delay)+'_'+'pulse 1 map_data']
                        
                       
                            
                    #without drug
                    maxLocActual = np.argmax(coincidentData['actualCoincident'][1000:1300],axis = 0) +1000
                    maxValActual = []
                    actualBL = np.mean(coincidentData['actualCoincident'][990:999],axis = 0)
                    maxValActual = np.mean(coincidentData['actualCoincident'][maxLocActual-3 : maxLocActual+3], 0) - actualBL       
                    
                    maxLocSum = np.argmax(coincidentData['arithmeticSum'][1000:1300],axis = 0) +1000
                    maxValSum = []
                    sumBL = np.mean(coincidentData['arithmeticSum'][990:999],axis = 0)
                    maxValSum = np.mean(coincidentData['arithmeticSum'][maxLocSum-3 : maxLocSum+3], 0) - sumBL
    
                    peakData.at[str(i),str(delay)+'ms_sensory single'] = maxValSum #now has to equal arithmetic addition of traces peak
                    peakData.at[str(i),str(delay)+'ms_sensory paired'] = maxValActual #now has to equal coincident
                    peakData.at[str(i),str(delay)+'ms_frontal single'] = maxValSum # same as above
                    peakData.at[str(i),str(delay)+'ms_frontal paired'] = maxValActual # same as above

            
                except:
                    peakData.at[str(i),str(delay)+'ms_sensory single'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_sensory paired'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_frontal single'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_frontal paired'] = np.nan
                                      
                    
            if delay == 50:
                try:
                    if i in opsinSwapList:
    
                    #without drug
                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_swap_data']                        
                        workspacedf['zeros'] = np.zeros(len(workspacedf))
                        workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 1 map_data'][1000:2000]
                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf['zeros']
    
                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_data']                        
                        workspacedf['zeros'] = np.zeros(len(workspacedf))
                        workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 2 map_data'][1000:2000]
                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 1 map_data'] + workspacedf['zeros']
                   
                    
    
                    if i not in opsinSwapList:
    
                        #without drug
                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_data']                        
                        workspacedf['zeros'] = np.zeros(len(workspacedf))
                        workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 2 map_data'][1000:2000]
                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 1 map_data'] + workspacedf['zeros']
    
                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_swap_data']                        
                        workspacedf['zeros'] = np.zeros(len(workspacedf))
                        workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 1 map_data'][1000:2000]
                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf['zeros']
                   
                            
                    #for before drug
                    maxLocSensoryActual = np.argmax(frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'][1000+(delay*10):1300+(delay*10)],axis = 0) + 1000 +(delay*10)
                    maxValSensoryActual = []
                    sensoryActualPeak = abs(np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'][maxLocSensoryActual-3: maxLocSensoryActual+3], 0))        
                    sensoryActualBL = abs(np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'][990+(delay*10):999+(delay*10)], 0))
                    peakValSensoryActual = sensoryActualPeak - sensoryActualBL    
                        
                    maxLocSensoryArithmetic = np.argmax(frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'][1000+(delay*10):1300+(delay*10)],axis = 0) + 1000 +(delay*10)
                    maxValSensoryArithmetic = []
                    sensoryArithmeticPeak = abs(np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'][maxLocSensoryArithmetic-3 : maxLocSensoryArithmetic+3], 0))        
                    sensoryArithmeticBL = abs(np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'][990+(delay*10):999+(delay*10)], 0))
                    peakValSensoryArithmetic = sensoryArithmeticPeak - sensoryArithmeticBL                         
    
                    maxLocFrontalActual = np.argmax(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'][1000+(delay*10):1300+(delay*10)],axis = 0) + 1000 +(delay*10)
                    maxValFrontalActual = []
                    frontalActualPeak = abs(np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'][maxLocFrontalActual-3 : maxLocFrontalActual+3], 0))        
                    frontalActualBL = abs(np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'][990+(delay*10):999+(delay*10)], 0))
                    peakValFrontalActual = frontalActualPeak - frontalActualBL    
                        
                    maxLocFrontalArithmetic = np.argmax(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'][1000+(delay*10):1300+(delay*10)],axis = 0) + 1000 +(delay*10)
                    maxValFrontalArithmetic = []
                    frontalArithmeticPeak = abs(np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'][maxLocFrontalArithmetic-3: maxLocFrontalArithmetic+3], 0))        
                    frontalArithmeticBL = abs(np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'][990+(delay*10):999+(delay*10)], 0))
                    peakValFrontalArithmetic = frontalArithmeticPeak - frontalArithmeticBL                         
                    
                    #get peak amplitudes
                    peakData.at[str(i),str(delay)+'ms_sensory single'] = peakValSensoryArithmetic
                    peakData.at[str(i),str(delay)+'ms_sensory paired'] = peakValSensoryActual
                    peakData.at[str(i),str(delay)+'ms_frontal single'] = peakValFrontalArithmetic
                    peakData.at[str(i),str(delay)+'ms_frontal paired'] = peakValFrontalActual
                    
                    
                    
                except:
                    peakData.at[str(i),str(delay)+'ms_sensory single'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_sensory paired'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_frontal single'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_frontal paired'] = np.nan

    #get ratios
        
    pairedpeakRatio = pd.DataFrame(index=peakData.index)
    
    pairedpeakRatio['0ms_frontal']=""
    pairedpeakRatio['0ms_sensory']=""
    pairedpeakRatio['50ms_frontal']=""
    pairedpeakRatio['50ms_sensory']=""

    
    for iIndex in selectednames:
        pairedpeakRatio.at[str(iIndex),'0ms_frontal']= peakData.at[str(iIndex),'0ms_frontal paired'] / peakData.at[str(iIndex),'0ms_frontal single']
        pairedpeakRatio.at[str(iIndex),'0ms_sensory']= peakData.at[str(iIndex),'0ms_sensory paired'] / peakData.at[str(iIndex),'0ms_sensory single']
        pairedpeakRatio.at[str(iIndex),'50ms_frontal']= peakData.at[str(iIndex),'50ms_frontal paired'] / peakData.at[str(iIndex),'50ms_frontal single']
        pairedpeakRatio.at[str(iIndex),'50ms_sensory']= peakData.at[str(iIndex),'50ms_sensory paired'] / peakData.at[str(iIndex),'50ms_sensory single']

    
    
    # mouse averaging
    if averaging == 'mouse':
        pairedpeakRatio.index = pairedpeakRatio.index.map(lambda x: str(x)[:-9])
        workspaceMousedf = pairedpeakRatio.copy()
        workspaceMousedf = workspaceMousedf.astype(float)
        strippedID = []
        for i in selectednames:
            strippedID.append(i[0:-9])
        workspaceMousedf['stripped Names']=strippedID
        grp_mouse = workspaceMousedf.groupby(['stripped Names'])
        pairedpeakMouseRatio = grp_mouse.mean()
        
    elif averaging == 'cell':
        pairedpeakMouseRatio = pairedpeakRatio.astype(float)
        

    if plots == 'yes':    
        #get CI stats
        CIstats = pd.DataFrame(index=['95% CI','mean','upper bound','lower bound'])
        CIstats['0ms_frontal']=""
        CIstats['0ms_sensory']=""
        CIstats['50ms_frontal']=""
        CIstats['50ms_sensory']=""


        import numpy as np
        import scipy.stats
    
        for col in list(CIstats.columns): 
            a = pairedpeakMouseRatio[col].values
            float_arr = np.vstack(a[:]).astype(np.float)
            # n = len(float_arr)
            n = np.count_nonzero(~np.isnan(float_arr))
            m = pairedpeakMouseRatio[col].mean()
            se = scipy.stats.sem(float_arr, nan_policy = 'omit')
            h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
            #h = np.nanstd(float_arr) for standard dev
            CIstats.at['95% CI',col]= h
            CIstats.at['mean',col]= m
            CIstats.at['upper bound',col]= m + h     
            CIstats.at['lower bound',col]= m - h  
            
            CIstats.at['one sample t-test p val',col] = scipy.stats.ttest_1samp(float_arr,1.0,nan_policy='omit')[1]
            if CIstats.at['one sample t-test p val',col] < 0.05:
                CIstats.at['one sample significant?',col] = 'red'
            else:
                CIstats.at['one sample significant?',col] = 'black' 
                
                           
        from matplotlib import pyplot as plt
        

        if order == 'FS':
            

            for cell in list(pairedpeakMouseRatio.index):
                names = ['coin.','50 ms']
                values = [pairedpeakMouseRatio.at[cell,'0ms_sensory'], pairedpeakMouseRatio.at[cell,'50ms_sensory']]
                
                #if connecting lines
                plt.plot(names, values, color = 'lightgrey')
                #if just markers
                # plt.scatter(names, values)
                
                linevalues = [1,1]
                plt.ylim((0.3,2.5))
                plt.plot(names,linevalues,'k--',alpha=0.7)
                plt.tight_layout()
                

            plt.text('coin.', 0.5, "%.3f" % CIstats.at['one sample t-test p val', '0ms_sensory'], color = CIstats.at['one sample significant?','0ms_sensory'])
            plt.text('50 ms', 0.5, "%.3f" % CIstats.at['one sample t-test p val', '50ms_sensory'], color = CIstats.at['one sample significant?','50ms_sensory'])
            meanvals = [CIstats.at['mean','0ms_sensory'], CIstats.at['mean','50ms_sensory']]
            plt.plot(names, meanvals, color = 'red')  
            
   
    return pairedpeakMouseRatio

    

    
#%%
    
def intMechanism(fiberTypes, confidence, cellType, opsinSwapList, oneMapCells, drug, imageloc, show, order, tau, averaging, plots):

    #load data
    #organize data in pairs, pre and post drug
    #get pulse ratios
    #plot with each other, straight line then dotted for post

    import tkinter
    from tkinter.filedialog import askopenfilename
    import pickle

    from pathlib import Path
    

    if drug == 'AP5':
        if 'A1' in fiberTypes and 'ACC' in fiberTypes:
            savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration A1_ACC mechanism\AP5")

    if drug == 'mib': 
        if 'A1' in fiberTypes and 'ACC' in fiberTypes:
            savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration A1_ACC mechanism\mibefradil")
                 
    if drug == 'TTX': 
        if 'A1' in fiberTypes and 'ACC' in fiberTypes:
            savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration A1_ACC mechanism\TTX")

   
    if drug == 'PTX': 
        if 'A1' in fiberTypes and 'ACC' in fiberTypes:
            savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration A1_ACC mechanism\PTX")      

    if drug == 'time': 
        if 'A1' in fiberTypes and 'ACC' in fiberTypes:
            savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration A1_ACC mechanism\time control")   


    # make a list with all folder names including cellType:
    import os
    allnames = os.listdir(savedLoc)
    selectednames = [x for x in allnames if cellType in x]
    
    
    import pandas as pd
    import numpy as np
    frontalsensoryData = pd.DataFrame()
    sensoryfrontalData = pd.DataFrame()
    coincidentData = pd.DataFrame()
    
    peakData = pd.DataFrame({'cell ID':[*selectednames]}).set_index('cell ID')
    
    peakData['0ms_frontal single']=""
    peakData['0ms_frontal paired']=""
    peakData['0ms_sensory single']=""
    peakData['0ms_sensory paired']=""
    peakData['50ms_frontal single']=""
    peakData['50ms_frontal paired']=""
    peakData['50ms_sensory single']=""
    peakData['50ms_sensory paired']=""
    peakData['0ms_drug frontal single']=""
    peakData['0ms_drug frontal paired']=""
    peakData['0ms_drug sensory single']=""
    peakData['0ms_drug sensory paired']=""
    peakData['50ms_drug frontal single']=""
    peakData['50ms_drug frontal paired']=""
    peakData['50ms_drug sensory single']=""
    peakData['50ms_drug sensory paired']=""
    
    taudf_ctr = pd.DataFrame()
    taudf_drug = pd.DataFrame()
    
    for i in selectednames:
        print('processing...'+str(i)) 
        # point at data file to view
        cellPath = savedLoc / i
        workspacedf = pd.DataFrame()
        for delay in [0,50]: #this loop added to deal with PTX experiment 220212
            workspacedf[str(delay)+'_paired pulse map_data'] = [np.nan] * 10000
            workspacedf[str(delay)+'_pulse 1 map_data'] = [np.nan] * 10000
            workspacedf[str(delay)+'_paired pulse map_swap_data'] = [np.nan] * 10000
            workspacedf[str(delay)+'_pulse 2 map_data'] = [np.nan] * 10000
            workspacedf[str(delay)+'_paired pulse map_data_'+drug] = [np.nan] * 10000
            workspacedf[str(delay)+'_pulse 1 map_data_'+drug] = [np.nan] * 10000
            workspacedf[str(delay)+'_paired pulse map_swap_data_'+drug] = [np.nan] * 10000
            workspacedf[str(delay)+'_pulse 2 map_data_'+drug] = [np.nan] * 10000
            
        for file in os.listdir(cellPath):      
            for delay in [0,50]:                                    
                if '_'+str(delay)+'ms' in file:
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    for k in loadedData.keys():
                        if '_data' in k and drug not in file:
                            workspacedf[str(delay)+'_'+str(k)] = loadedData[k]
                        elif '_data' in k and drug in file:
                            workspacedf[str(delay)+'_'+str(k)+'_'+drug] = loadedData[k]

        
        for delay in [0,50]:        
            if delay == 0:
                try:
                    if i in opsinSwapList:
                        
                        coincidentData['actualCoincident'] = workspacedf[str(delay)+'_'+'paired pulse map_data']
                        coincidentData['arithmeticSum'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf[str(delay)+'_'+'pulse 1 map_data']
                        
                        if order == 'FS': 
                            taudf_ctr[i+'_'+str(delay)] = workspacedf[str(delay)+'_'+'pulse 2 map_data']
                        elif order == 'SF':
                            taudf_ctr[i+'_'+str(delay)] = workspacedf[str(delay)+'_'+'pulse 1 map_data']
                            
                        try:
                            coincidentData['actualCoincident_drug'] = workspacedf[str(delay)+'_'+'paired pulse map_data_'+drug]
                            coincidentData['arithmeticSum_drug'] = workspacedf[str(delay)+'_'+'pulse 2 map_data_'+drug] + workspacedf[str(delay)+'_'+'pulse 1 map_data_'+drug]
                            
                            if order == 'FS':
                                taudf_drug[i+'_'+str(delay)+'drug'] = workspacedf[str(delay)+'_'+'pulse 2 map_data_'+drug]
                            elif order == 'SF':
                                taudf_drug[i+'_'+str(delay)+'drug'] = workspacedf[str(delay)+'_'+'pulse 1 map_data_'+drug]
                            
                        except:
                            coincidentData['actualCoincident_drug'] = np.nan
                            coincidentData['arithmeticSum_drug'] = np.nan
                            
                    if i not in opsinSwapList: # same as above if in opsinSwapList
                        
                        coincidentData['actualCoincident'] = workspacedf[str(delay)+'_'+'paired pulse map_data']
                        coincidentData['arithmeticSum'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf[str(delay)+'_'+'pulse 1 map_data']
                        
                        if order == 'FS': 
                            taudf_ctr[i+'_'+str(delay)] = workspacedf[str(delay)+'_'+'pulse 1 map_data']
                        elif order == 'SF':
                            taudf_ctr[i+'_'+str(delay)] = workspacedf[str(delay)+'_'+'pulse 2 map_data']
                        
                        try:
                            coincidentData['actualCoincident_drug'] = workspacedf[str(delay)+'_'+'paired pulse map_data_'+drug]
                            coincidentData['arithmeticSum_drug'] = workspacedf[str(delay)+'_'+'pulse 2 map_data_'+drug] + workspacedf[str(delay)+'_'+'pulse 1 map_data_'+drug]                        
                            
                            if order == 'FS':
                                taudf_drug[i+'_'+str(delay)+'drug'] = workspacedf[str(delay)+'_'+'pulse 1 map_data_'+drug]
                            elif order == 'SF':
                                taudf_drug[i+'_'+str(delay)+'drug'] = workspacedf[str(delay)+'_'+'pulse 2 map_data_'+drug]
                            
                        except:
                            coincidentData['actualCoincident_drug'] = np.nan
                            coincidentData['arithmeticSum_drug'] = np.nan
                            
                    #without drug
                    maxLocActual = np.argmax(coincidentData['actualCoincident'][1000:1300],axis = 0) +1000
                    maxValActual = []
                    actualBL = np.mean(coincidentData['actualCoincident'][990:999],axis = 0)
                    maxValActual = np.mean(coincidentData['actualCoincident'][maxLocActual-3 : maxLocActual+3], 0) - actualBL       
                    
                    maxLocSum = np.argmax(coincidentData['arithmeticSum'][1000:1300],axis = 0) +1000
                    maxValSum = []
                    sumBL = np.mean(coincidentData['arithmeticSum'][990:999],axis = 0)
                    maxValSum = np.mean(coincidentData['arithmeticSum'][maxLocSum-3 : maxLocSum+3], 0) - sumBL
    
                    peakData.at[str(i),str(delay)+'ms_sensory single'] = maxValSum #now has to equal arithmetic addition of traces peak
                    peakData.at[str(i),str(delay)+'ms_sensory paired'] = maxValActual #now has to equal coincident
                    peakData.at[str(i),str(delay)+'ms_frontal single'] = maxValSum # same as above
                    peakData.at[str(i),str(delay)+'ms_frontal paired'] = maxValActual # same as above


                    #with drug
                    maxLocActual = np.argmax(coincidentData['actualCoincident_drug'][1000:1300],axis = 0) +1000
                    maxValActual = []
                    actualBL = np.mean(coincidentData['actualCoincident_drug'][990:999],axis = 0)
                    maxValActual = np.mean(coincidentData['actualCoincident_drug'][maxLocActual-3 : maxLocActual+3], 0) - actualBL       
                    
                    maxLocSum = np.argmax(coincidentData['arithmeticSum_drug'][1000:1300],axis = 0) +1000
                    maxValSum = []
                    sumBL = np.mean(coincidentData['arithmeticSum_drug'][990:999],axis = 0)
                    maxValSum = np.mean(coincidentData['arithmeticSum_drug'][maxLocSum-3 : maxLocSum+3], 0) - sumBL
                 
                    
                    
                    peakData.at[str(i),str(delay)+'ms_drug sensory single'] = maxValSum #now has to equal arithmetic addition of traces peak
                    peakData.at[str(i),str(delay)+'ms_drug sensory paired'] = maxValActual #now has to equal coincident
                    peakData.at[str(i),str(delay)+'ms_drug frontal single'] = maxValSum # same as above
                    peakData.at[str(i),str(delay)+'ms_drug frontal paired'] = maxValActual # same as above
                                    
                    
                except:
                    peakData.at[str(i),str(delay)+'ms_sensory single'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_sensory paired'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_frontal single'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_frontal paired'] = np.nan
                                      
                    peakData.at[str(i),str(delay)+'ms_drug sensory single'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_drug sensory paired'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_drug frontal single'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_drug frontal paired'] = np.nan
           
                    
            if delay == 50:
                try:
                    if i in opsinSwapList:
    
                    #without drug
                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_swap_data']                        
                        workspacedf['zeros'] = np.zeros(len(workspacedf))
                        workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 1 map_data'][1000:2000]
                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf['zeros']
    
                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_data']                        
                        workspacedf['zeros'] = np.zeros(len(workspacedf))
                        workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 2 map_data'][1000:2000]
                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 1 map_data'] + workspacedf['zeros']
                   
                    #with drug  
                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual_drug'] = workspacedf[str(delay)+'_'+'paired pulse map_swap_data_'+drug]                        
                        workspacedf['zeros'] = np.zeros(len(workspacedf))
                        workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 1 map_data_'+drug][1000:2000]
                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic_drug'] = workspacedf[str(delay)+'_'+'pulse 2 map_data_'+drug] + workspacedf['zeros']
    
                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual_drug'] = workspacedf[str(delay)+'_'+'paired pulse map_data_'+drug]                        
                        workspacedf['zeros'] = np.zeros(len(workspacedf))
                        workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 2 map_data_'+drug][1000:2000]
                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic_drug'] = workspacedf[str(delay)+'_'+'pulse 1 map_data_'+drug] + workspacedf['zeros']
    
    
                    if i not in opsinSwapList:
    
                        #without drug
                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_data']                        
                        workspacedf['zeros'] = np.zeros(len(workspacedf))
                        workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 2 map_data'][1000:2000]
                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 1 map_data'] + workspacedf['zeros']
    
                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'] = workspacedf[str(delay)+'_'+'paired pulse map_swap_data']                        
                        workspacedf['zeros'] = np.zeros(len(workspacedf))
                        workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 1 map_data'][1000:2000]
                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf['zeros']
                        
                        #with drug
                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual_drug'] = workspacedf[str(delay)+'_'+'paired pulse map_data_'+drug]                        
                        workspacedf['zeros'] = np.zeros(len(workspacedf))
                        workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 2 map_data_'+drug][1000:2000]
                        frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic_drug'] = workspacedf[str(delay)+'_'+'pulse 1 map_data_'+drug] + workspacedf['zeros']
    
                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual_drug'] = workspacedf[str(delay)+'_'+'paired pulse map_swap_data_'+drug]                        
                        workspacedf['zeros'] = np.zeros(len(workspacedf))
                        workspacedf['zeros'][1000+(delay*10):2000+(delay*10)] = workspacedf[str(delay)+'_'+'pulse 1 map_data_'+drug][1000:2000]
                        sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic_drug'] = workspacedf[str(delay)+'_'+'pulse 2 map_data_'+drug] + workspacedf['zeros']
    
    
                            
                    #for before drug
                    maxLocSensoryActual = np.argmax(frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'][1000+(delay*10):1300+(delay*10)],axis = 0) + 1000 +(delay*10)
                    maxValSensoryActual = []
                    sensoryActualPeak = abs(np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'][maxLocSensoryActual-3: maxLocSensoryActual+3], 0))        
                    sensoryActualBL = abs(np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual'][990+(delay*10):999+(delay*10)], 0))
                    peakValSensoryActual = sensoryActualPeak - sensoryActualBL    
                        
                    maxLocSensoryArithmetic = np.argmax(frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'][1000+(delay*10):1300+(delay*10)],axis = 0) + 1000 +(delay*10)
                    maxValSensoryArithmetic = []
                    sensoryArithmeticPeak = abs(np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'][maxLocSensoryArithmetic-3 : maxLocSensoryArithmetic+3], 0))        
                    sensoryArithmeticBL = abs(np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic'][990+(delay*10):999+(delay*10)], 0))
                    peakValSensoryArithmetic = sensoryArithmeticPeak - sensoryArithmeticBL                         
    
                    maxLocFrontalActual = np.argmax(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'][1000+(delay*10):1300+(delay*10)],axis = 0) + 1000 +(delay*10)
                    maxValFrontalActual = []
                    frontalActualPeak = abs(np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'][maxLocFrontalActual-3 : maxLocFrontalActual+3], 0))        
                    frontalActualBL = abs(np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual'][990+(delay*10):999+(delay*10)], 0))
                    peakValFrontalActual = frontalActualPeak - frontalActualBL    
                        
                    maxLocFrontalArithmetic = np.argmax(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'][1000+(delay*10):1300+(delay*10)],axis = 0) + 1000 +(delay*10)
                    maxValFrontalArithmetic = []
                    frontalArithmeticPeak = abs(np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'][maxLocFrontalArithmetic-3: maxLocFrontalArithmetic+3], 0))        
                    frontalArithmeticBL = abs(np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic'][990+(delay*10):999+(delay*10)], 0))
                    peakValFrontalArithmetic = frontalArithmeticPeak - frontalArithmeticBL                         
                    
                    #get peak amplitudes
                    peakData.at[str(i),str(delay)+'ms_sensory single'] = peakValSensoryArithmetic
                    peakData.at[str(i),str(delay)+'ms_sensory paired'] = peakValSensoryActual
                    peakData.at[str(i),str(delay)+'ms_frontal single'] = peakValFrontalArithmetic
                    peakData.at[str(i),str(delay)+'ms_frontal paired'] = peakValFrontalActual
                    
                    
                    
                    #for after drug 
                    maxLocSensoryActual = np.argmax(frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual_drug'][1000+(delay*10):1300+(delay*10)],axis = 0) + 1000 +(delay*10)
                    maxValSensoryActual = []
                    sensoryActualPeak = abs(np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual_drug'][maxLocSensoryActual-3 : maxLocSensoryActual+3], 0))        
                    sensoryActualBL = abs(np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired actual_drug'][990+(delay*10):999+(delay*10)], 0))
                    peakValSensoryActual = sensoryActualPeak - sensoryActualBL    
                        
                    maxLocSensoryArithmetic = np.argmax(frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic_drug'][1000+(delay*10):1300+(delay*10)],axis = 0) + 1000 +(delay*10)
                    maxValSensoryArithmetic = []
                    sensoryArithmeticPeak = abs(np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic_drug'][maxLocSensoryArithmetic-3 : maxLocSensoryArithmetic+3], 0))        
                    sensoryArithmeticBL = abs(np.mean(frontalsensoryData['delay '+str(delay)+'ms_sensory paired arithmetic_drug'][990+(delay*10):999+(delay*10)], 0))
                    peakValSensoryArithmetic = sensoryArithmeticPeak - sensoryArithmeticBL                         
    
                    maxLocFrontalActual = np.argmax(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual_drug'][1000+(delay*10):1300+(delay*10)],axis = 0) + 1000 +(delay*10)
                    maxValFrontalActual = []
                    frontalActualPeak = abs(np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual_drug'][maxLocFrontalActual-3 : maxLocFrontalActual+3], 0))        
                    frontalActualBL = abs(np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired actual_drug'][990+(delay*10):999+(delay*10)], 0))
                    peakValFrontalActual = frontalActualPeak - frontalActualBL    
                        
                    maxLocFrontalArithmetic = np.argmax(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic_drug'][1000+(delay*10):1300+(delay*10)],axis = 0) + 1000 +(delay*10)
                    maxValFrontalArithmetic = []
                    frontalArithmeticPeak = abs(np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic_drug'][maxLocFrontalArithmetic-3 : maxLocFrontalArithmetic+3], 0))        
                    frontalArithmeticBL = abs(np.mean(sensoryfrontalData['delay '+str(delay)+'ms_frontal paired arithmetic_drug'][990+(delay*10):999+(delay*10)], 0))
                    peakValFrontalArithmetic = frontalArithmeticPeak - frontalArithmeticBL                      
                    
                
                    #get peak amplitudes
                    peakData.at[str(i),str(delay)+'ms_drug sensory single'] = peakValSensoryArithmetic
                    peakData.at[str(i),str(delay)+'ms_drug sensory paired'] = peakValSensoryActual
                    peakData.at[str(i),str(delay)+'ms_drug frontal single'] = peakValFrontalArithmetic
                    peakData.at[str(i),str(delay)+'ms_drug frontal paired'] = peakValFrontalActual
                    
                    
                except:
                    peakData.at[str(i),str(delay)+'ms_sensory single'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_sensory paired'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_frontal single'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_frontal paired'] = np.nan
                                      
                    peakData.at[str(i),str(delay)+'ms_drug sensory single'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_drug sensory paired'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_drug frontal single'] = np.nan
                    peakData.at[str(i),str(delay)+'ms_drug frontal paired'] = np.nan
                     
    #get ratios
        
    pairedpeakRatio = pd.DataFrame(index=peakData.index)
    
    pairedpeakRatio['0ms_frontal']=""
    pairedpeakRatio['0ms_sensory']=""
    pairedpeakRatio['50ms_frontal']=""
    pairedpeakRatio['50ms_sensory']=""
    pairedpeakRatio['0ms_drug frontal']=""
    pairedpeakRatio['0ms_drug sensory']=""
    pairedpeakRatio['50ms_drug frontal']=""
    pairedpeakRatio['50ms_drug sensory']=""
    
    for iIndex in selectednames:
        pairedpeakRatio.at[str(iIndex),'0ms_frontal']= peakData.at[str(iIndex),'0ms_frontal paired'] / peakData.at[str(iIndex),'0ms_frontal single']
        pairedpeakRatio.at[str(iIndex),'0ms_sensory']= peakData.at[str(iIndex),'0ms_sensory paired'] / peakData.at[str(iIndex),'0ms_sensory single']
        pairedpeakRatio.at[str(iIndex),'50ms_frontal']= peakData.at[str(iIndex),'50ms_frontal paired'] / peakData.at[str(iIndex),'50ms_frontal single']
        pairedpeakRatio.at[str(iIndex),'50ms_sensory']= peakData.at[str(iIndex),'50ms_sensory paired'] / peakData.at[str(iIndex),'50ms_sensory single']
        pairedpeakRatio.at[str(iIndex),'0ms_drug frontal']= peakData.at[str(iIndex),'0ms_drug frontal paired'] / peakData.at[str(iIndex),'0ms_drug frontal single']
        pairedpeakRatio.at[str(iIndex),'0ms_drug sensory']= peakData.at[str(iIndex),'0ms_drug sensory paired'] / peakData.at[str(iIndex),'0ms_drug sensory single']
        pairedpeakRatio.at[str(iIndex),'50ms_drug frontal']= peakData.at[str(iIndex),'50ms_drug frontal paired'] / peakData.at[str(iIndex),'50ms_drug frontal single']
        pairedpeakRatio.at[str(iIndex),'50ms_drug sensory']= peakData.at[str(iIndex),'50ms_drug sensory paired'] / peakData.at[str(iIndex),'50ms_drug sensory single']
    
    
    
    # mouse averaging
    if averaging == 'mouse':
        pairedpeakRatio.index = pairedpeakRatio.index.map(lambda x: str(x)[:-9])
        workspaceMousedf = pairedpeakRatio.copy()
        workspaceMousedf = workspaceMousedf.astype(float)
        strippedID = []
        for i in selectednames:
            strippedID.append(i[0:-9])
        workspaceMousedf['stripped Names']=strippedID
        grp_mouse = workspaceMousedf.groupby(['stripped Names'])
        pairedpeakMouseRatio = grp_mouse.mean()
        
    elif averaging == 'cell':
        pairedpeakMouseRatio = pairedpeakRatio.astype(float)
        


    if plots == 'yes':    
        #get CI stats
        CIstats = pd.DataFrame(index=['95% CI','mean','upper bound','lower bound'])
        
        
        CIstats['0ms_frontal']=""
        CIstats['0ms_sensory']=""
        CIstats['50ms_frontal']=""
        CIstats['50ms_sensory']=""
        CIstats['0ms_drug frontal']=""
        CIstats['0ms_drug sensory']=""
        CIstats['50ms_drug frontal']=""
        CIstats['50ms_drug sensory']=""

        import numpy as np
        import scipy.stats
    
        for col in list(CIstats.columns): 
            a = pairedpeakMouseRatio[col].values
            float_arr = np.vstack(a[:]).astype(np.float)
            # n = len(float_arr)
            n = np.count_nonzero(~np.isnan(float_arr))
            m = pairedpeakMouseRatio[col].mean()
            se = scipy.stats.sem(float_arr, nan_policy = 'omit')
            h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
            #h = np.nanstd(float_arr) for standard dev
            CIstats.at['95% CI',col]= h
            CIstats.at['mean',col]= m
            CIstats.at['upper bound',col]= m + h     
            CIstats.at['lower bound',col]= m - h  
            
            CIstats.at['one sample t-test p val',col] = scipy.stats.ttest_1samp(float_arr,1.0,nan_policy='omit')[1]
            if CIstats.at['one sample t-test p val',col] < 0.05:
                CIstats.at['one sample significant?',col] = 'red'
            else:
                CIstats.at['one sample significant?',col] = 'black' 
                
            if '0ms_drug frontal' in col:    
               CIstats.at['paired t-test p val',col] = scipy.stats.ttest_rel(pairedpeakMouseRatio[col], pairedpeakMouseRatio['0ms_frontal'], nan_policy='omit')[1]
               if CIstats.at['paired t-test p val',col] < 0.05:
                   CIstats.at['paired t test significant?',col] = 'red'
               else:
                   CIstats.at['paired t test significant?',col] = 'black'
                   
            if '0ms_drug sensory' in col:    
               CIstats.at['paired t-test p val',col] = scipy.stats.ttest_rel(pairedpeakMouseRatio[col], pairedpeakMouseRatio['0ms_sensory'], nan_policy='omit')[1]
               if CIstats.at['paired t-test p val',col] < 0.05:
                   CIstats.at['paired t test significant?',col] = 'red'
               else:
                   CIstats.at['paired t test significant?',col] = 'black'
                   
            if '50ms_drug frontal' in col:    
               CIstats.at['paired t-test p val',col] = scipy.stats.ttest_rel(pairedpeakMouseRatio[col], pairedpeakMouseRatio['50ms_frontal'], nan_policy='omit')[1]
               if CIstats.at['paired t-test p val',col] < 0.05:
                   CIstats.at['paired t test significant?',col] = 'red'
               else:
                   CIstats.at['paired t test significant?',col] = 'black'
                   
            if '50ms_drug sensory' in col:    
               CIstats.at['paired t-test p val',col] = scipy.stats.ttest_rel(pairedpeakMouseRatio[col], pairedpeakMouseRatio['50ms_sensory'], nan_policy='omit')[1]  
               if CIstats.at['paired t-test p val',col] < 0.05:
                   CIstats.at['paired t test significant?',col] = 'red'
               else:
                   CIstats.at['paired t test significant?',col] = 'black'
                   
           
        from matplotlib import pyplot as plt

        #calculate tau  
        tauArray_ctr = np.asarray(taudf_ctr.mean(1))
        tauArray_drug = np.asarray(taudf_drug.mean(1))
                
        #show drug figures for tau
      
        plt.figure()
        plt.plot(tauArray_ctr,label = 'ctr')
        plt.plot(tauArray_drug,label = drug)
        plt.legend()      
        
        
        #show drug figures for mechanism
        test = pairedpeakMouseRatio.transpose()
        test['time'] = ''
        test['input'] = ''
        test['condition'] = ''
        
        for i in list(test.index):
            if i[0] == '0':
                test.at[i,'time'] = '0ms'
            else:
                test.at[i,'time'] = '50ms'
                
            if 'frontal' in i:
                test.at[i,'input'] = 'frontal'
            else:
                test.at[i,'input'] = 'sensory'
                
            if 'drug' in i:
                test.at[i,'condition'] = drug
            else:
                test.at[i,'condition'] = 'ctr'
        
        for delay in ['0ms', '50ms']:
            
            from matplotlib import pyplot as plt
            
            plt.figure()
            
            test2 = test[test['time'] == delay]
            
            
            if order == 'FS':
                
                test3 = test2[test2['input'] == 'sensory']
    
                for i in list(pairedpeakMouseRatio.index):    
                    names = list(test3['condition'])
                    values = list(test3[i])
                    
                    plt.plot(names, values, color = 'lightgrey')
                    plt.title(delay)
                    linevalues = [1,1]
                    plt.ylim((0.3,2.5))
                    plt.plot(names,linevalues,'k--',alpha=0.7)
                    plt.tight_layout()
                    
                
                test3.at[delay+'_sensory','avg'] = pairedpeakMouseRatio[delay+'_sensory'].mean()
                test3.at[delay+'_drug sensory','avg'] = pairedpeakMouseRatio[delay+'_drug sensory'].mean()
                plt.text(0.4, 2.3, "%.3f" % CIstats.at['paired t-test p val', delay+'_drug sensory'], color = CIstats.at['paired t test significant?',delay+'_drug sensory']) 
                plt.text(0.65, 0.5, "%.3f" % CIstats.at['one sample t-test p val', delay+'_drug sensory'], color = CIstats.at['one sample significant?',delay+'_drug sensory'])
                plt.text('ctr', 0.5, "%.3f" % CIstats.at['one sample t-test p val', delay+'_sensory'], color = CIstats.at['one sample significant?',delay+'_sensory'])
                values = list(test3['avg'])
                plt.plot(names, values, color = 'red')  
                
            elif order == 'SF':
                
                test3 = test2[test2['input'] == 'frontal']
                
                for i in list(pairedpeakMouseRatio.index):    
                    names = list(test3['condition'])
                    values = list(test3[i])
                    
                    plt.plot(names, values, color = 'lightgrey')
                    plt.title(delay)
                    linevalues = [1,1]
                    plt.ylim((0.3,2.5))
                    plt.plot(names,linevalues,'k--',alpha=0.7)
                    plt.tight_layout()
                
                test3.at[delay+'_frontal','avg'] = pairedpeakMouseRatio[delay+'_frontal'].mean()
                test3.at[delay+'_drug frontal','avg'] = pairedpeakMouseRatio[delay+'_drug frontal'].mean()
                plt.text(0.4, 2.3, "%.3f" % CIstats.at['paired t-test p val', delay+'_drug frontal'], color = CIstats.at['paired t test significant?',delay+'_drug frontal'])
                plt.text(0.65, 0.5, "%.3f" % CIstats.at['one sample t-test p val', delay+'_drug frontal'], color = CIstats.at['one sample significant?',delay+'_drug frontal'])
                plt.text('ctr', 0.5, "%.3f" % CIstats.at['one sample t-test p val', delay+'_frontal'], color = CIstats.at['one sample significant?',delay+'_frontal'])
                values = list(test3['avg'])
                plt.plot(names, values, color = 'red')  
                
    
            if show == 1:
                imagename = drug + ' '+cellType+' '+delay 
                imagepath = Path(imageloc)
                
                plt.savefig(imagepath / (imagename + '.png'), bbox_inches = "tight")  # may not work
                plt.savefig(imagepath / (imagename + '.eps'), format='eps', dpi=1200)
        
                
    return pairedpeakMouseRatio    
#%%
def getallCI(fiberTypes, delay1, delay2, delay3, delay4, opsinSwapList, confidence, oneMapCells, quality, show, imageloc, complete, average, plots):
    
    import pandas as pd
    import tkinter
    from matplotlib import pyplot as plt
    from tkinter.filedialog import askopenfilename
    import numpy as np
    import DR_analysis_functions as af
        
    allMPRdf = pd.DataFrame(columns = ['IB_50', 'IB_0', 'RS_50', 'RS_0'])
    
    for cellType in ['IB', 'RS']:
    
        opswinSwapRatios, nonSwapRatios = af.plotmouseCI(fiberTypes, cellType, delay1, delay2, delay3, delay4, opsinSwapList, confidence, oneMapCells, quality, show, imageloc, complete, average, plots)
        tempdf=pd.DataFrame(columns = [cellType+'_50',cellType+'_0'])
        tempdf[cellType+'_50']=nonSwapRatios['50ms_sensory']
        tempdf[cellType+'_0']=nonSwapRatios['0ms_sensory']
    
        if cellType == 'IB':
            tempdf.at['200709_wt_1116_cell2_IB','IB_0'] = np.nan
        
        
        allMPRdf = allMPRdf.append(tempdf)
        
        
        for drug in ['AP5', 'mib', 'TTX', 'PTX']:
            # if cellType == 'RS' and drug == 'mib':
            #     continue
            pairedpeakMouseRatio = af.intMechanism(fiberTypes, confidence, cellType, opsinSwapList, oneMapCells, drug, imageloc, show, order, tau, averaging, plots)
            tempdf=pd.DataFrame(columns = [cellType+'_50',cellType+'_0'])
            tempdf[cellType+'_50']=pairedpeakMouseRatio['50ms_sensory']
            tempdf[cellType+'_0']=pairedpeakMouseRatio['0ms_sensory']
            
            if cellType == 'IB' and drug == 'mib':
                tempdf[cellType+'_50'] = np.nan
            if  cellType == 'RS' and drug == 'mib':
                tempdf[cellType+'_50'] = np.nan
                tempdf[cellType+'_0'] = np.nan
            
            
            allMPRdf = allMPRdf.append(tempdf)
    
    import numpy as np
    
    #get CI stats
    CIstats = pd.DataFrame(index=['CI','mean','upper bound','lower bound','median'])
    
    CIstats['IB_50']=""
    CIstats['IB_0']=""
    CIstats['RS_50']=""
    CIstats['RS_0']=""
    
    import scipy.stats as stats
    import numpy as np
    
    for col in list(CIstats.columns): 
        a = allMPRdf[col].values
        float_arr = np.vstack(a[:]).astype(np.float)
        n = len(float_arr)
        m = allMPRdf[col].mean()
        med = allMPRdf[col].median()
        se = stats.sem(float_arr, nan_policy = 'omit')
        h = se * stats.t.ppf((1 + confidence) / 2., n-1)
        # h = np.nanstd(float_arr) #for standard dev
        CIstats.at['CI',col]= h
        CIstats.at['mean',col]= m
        CIstats.at['median',col]= med
        CIstats.at['upper bound',col]= m + h     
        CIstats.at['lower bound',col]= m - h
    
    bounds= {}
    
    bounds['IBupper50'] = float(CIstats.at['upper bound','IB_50'] * 100)
    bounds['IBlower50'] = float(CIstats.at['lower bound','IB_50'] * 100)
    bounds['IBupper0'] = float(CIstats.at['upper bound','IB_0'] * 100)
    bounds['IBlower0'] = float(CIstats.at['lower bound','IB_0'] * 100)
    bounds['IBavg50'] = float(CIstats.at['mean','IB_50'] * 100)
    bounds['IBavg0'] = float(CIstats.at['mean','IB_0'] * 100)
    bounds['RSupper50'] = float(CIstats.at['upper bound','RS_50'] * 100)
    bounds['RSlower50'] = float(CIstats.at['lower bound','RS_50'] * 100)
    bounds['RSupper0'] = float(CIstats.at['upper bound','RS_0'] * 100)
    bounds['RSlower0'] = float(CIstats.at['lower bound','RS_0'] * 100)
    bounds['RSavg50'] = float(CIstats.at['mean','RS_50'] * 100)
    bounds['RSavg0'] = float(CIstats.at['mean','RS_0'] * 100)
    
    
    bounds['IBmed50'] = float(CIstats.at['median','IB_50'] * 100)
    bounds['IBmed0'] = float(CIstats.at['median','IB_0'] * 100)
    
    bounds['RSmed50'] = float(CIstats.at['median','RS_50'] * 100)
    bounds['RSmed0'] = float(CIstats.at['median','RS_0'] * 100)
        
      
    return bounds
    

#%% 
def GABAonEPSP(opsinSwapList, imageloc, confidence, show):
    
    import tkinter
    from tkinter.filedialog import askopenfilename
    import pickle
    import pandas as pd
    import numpy as np
    
    
    from pathlib import Path
    savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\GABA")      

    peak = {}
    
    for cellType in ['IB', 'RS']:
           
        # make a list with all folder names including cellType:
        import os
        allnames = os.listdir(savedLoc)
        selectednames = [x for x in allnames if cellType in x]
        
        peak[cellType] = pd.DataFrame({'cell ID':[*selectednames]}).set_index('cell ID')
        peak[cellType]['ctrData_A1'] = None
        peak[cellType]['ptxData_A1'] = None
        peak[cellType]['ctrData_ACC'] = None
        peak[cellType]['ptxData_ACC'] = None
            
        
        ctrData_A1 = pd.DataFrame()
        ptxData_A1 = pd.DataFrame()
        ctrData_ACC = pd.DataFrame()
        ptxData_ACC = pd.DataFrame()    
    
        for i in selectednames:
            print('processing...'+str(i)) 
            # point at data file to view
            cellPath = savedLoc / i
            workspacedf = pd.DataFrame()
            
            
            for file in os.listdir(cellPath):  
                if 'blue_60' in file:
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    for k in loadedData.keys():
                        if i not in opsinSwapList:
                            if '_data' in k and 'PTX' not in file:
                                ctrData_ACC[i] = loadedData[k]
                            elif '_data' in k and 'PTX' in file:
                                ptxData_ACC[i] = loadedData[k]   
                        if i in opsinSwapList:                            
                            if '_data' in k and 'PTX' not in file:
                                ctrData_A1[i] = loadedData[k]
                            elif '_data' in k and 'PTX' in file:
                                ptxData_A1[i] = loadedData[k]    
                                
                if 'red_60' in file:
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    for k in loadedData.keys():
                        if i not in opsinSwapList:
                            if '_data' in k and 'PTX' not in file:
                                ctrData_A1[i] = loadedData[k]
                            elif '_data' in k and 'PTX' in file:
                                ptxData_A1[i] = loadedData[k]   
                        if i in opsinSwapList:
                            if '_data' in k and 'PTX' not in file:
                                ctrData_ACC[i] = loadedData[k]
                            elif '_data' in k and 'PTX' in file:
                                ptxData_ACC[i] = loadedData[k]                                                   
                        
        from matplotlib import pyplot as plt
        
        plt.figure()
        
        for iData in list(ctrData_ACC.columns):
            plt.plot(ctrData_ACC[iData][700:5000] - np.mean(ctrData_ACC[iData][900:999]), color='whitesmoke')
            plt.plot(ptxData_ACC[iData][700:5000] - np.mean(ptxData_ACC[iData][900:999]), color='mistyrose')
            #plt.ylim(-70,-45)
            plt.ylim(-15,15)
            plt.title('ACC ' + cellType)
        plt.plot(ctrData_ACC.mean(1)[700:5000] - np.mean(ctrData_ACC.mean(1)[900:999]), color='black')
        plt.plot(ptxData_ACC.mean(1)[700:5000] - np.mean(ptxData_ACC.mean(1)[900:999]), color='red')
                
            
        
        plt.figure() 
    
        for iData in list(ctrData_A1.columns):
            plt.plot(ctrData_A1[iData][700:5000] - np.mean(ctrData_A1[iData][900:999]), color='whitesmoke')
            plt.plot(ptxData_A1[iData][700:5000] - np.mean(ptxData_A1[iData][900:999]), color='mistyrose')
            #plt.ylim(-70,-45)
            plt.ylim(-15,15)
            plt.title('A1 ' + cellType)                    
        plt.plot(ctrData_A1.mean(1)[700:5000] - np.mean(ctrData_A1.mean(1)[900:999]), color='black')
        plt.plot(ptxData_A1.mean(1)[700:5000] - np.mean(ptxData_A1.mean(1)[900:999]), color='red')  
               
        

    #for quantifying inhibition in each cell type
    #way 1 - measure peak in PTX and value at same time point in control        

        for iCell in list(ctrData_A1.columns):          
            maxIndex1 = np.argmax(ptxData_A1[iCell][1000:1500])
            maxVal1 = ptxData_A1[iCell][maxIndex1+1000]
            baseline1 = np.mean(ptxData_A1[iCell][990:999])
            peak[cellType].at[iCell,'ptxData_A1'] = maxVal1-baseline1
            maxVal2 = ctrData_A1[iCell][maxIndex1+1000]
            baseline2 = np.mean(ctrData_A1[iCell][990:999])
            peak[cellType].at[iCell,'ctrData_A1'] = maxVal2-baseline2        

        for iCell in list(ctrData_ACC.columns):
            maxIndex1 = np.argmax(ptxData_ACC[iCell][1000:1500])
            maxVal1 = ptxData_ACC[iCell][maxIndex1+1000]
            baseline1 = np.mean(ptxData_ACC[iCell][990:999])
            peak[cellType].at[iCell,'ptxData_ACC'] = maxVal1-baseline1
            maxVal2 = ctrData_ACC[iCell][maxIndex1+1000]
            baseline2 = np.mean(ctrData_ACC[iCell][990:999])
            peak[cellType].at[iCell,'ctrData_ACC'] = maxVal2-baseline2  
            
    
    
    difPeak = peak.copy()
    for k, v in difPeak.items():
        difPeak[k]['A1 difference'] = v['ptxData_A1'] - v['ctrData_A1']
        difPeak[k]['ACC difference'] = v['ptxData_ACC'] - v['ctrData_ACC']
    
    
    import scipy.stats as stats

    data = difPeak
    title = 'coincident peak'

    pvalA1 = stats.ttest_ind(data['IB']['A1 difference'], data['RS']['A1 difference'], nan_policy='omit')[1]
    pvalACC = stats.ttest_ind(data['IB']['ACC difference'], data['RS']['ACC difference'], nan_policy='omit')[1]
    if pvalA1 < 0.05:
        sigA1 = 'red'
    else:
        sigA1 = 'black' 
        
    if pvalACC < 0.05:
        sigACC = 'red'
    else:
        sigACC = 'black'  
    
    for iFiber in ['A1','ACC']: 
        plt.figure(figsize=[2,4.5])
        plt.title(title +' '+iFiber)
        plt.ylim(-4,21)
        
        for iType in ['IB','RS']:
            y = data[iType][iFiber+' difference']
            avg = np.mean(y)
            x = [iType] * len(y)
            plt.scatter(x,y,label=iType,facecolors='none',edgecolors='b')
            plt.scatter([iType],avg,color='red',marker='_')

        if iFiber == 'A1':
            plt.text(0.4, 14, "%.3f" % pvalA1, color = sigA1) 
        if iFiber == 'ACC':
            plt.text(0.4, 14, "%.3f" % pvalACC, color = sigACC) 
        
        plt.tight_layout()       


    for iType in ['IB', 'RS']: 
        
        CIstats = pd.DataFrame(index=['95% CI','mean','upper bound','lower bound'])
        
        for col in list(data[iType].columns): 
            a = data[iType][col].values
            float_arr = np.vstack(a[:]).astype(np.float)
            # n = len(float_arr)
            n = np.count_nonzero(~np.isnan(float_arr))
            m = data[iType][col].mean()
            se = stats.sem(float_arr, nan_policy = 'omit')
            h = se * stats.t.ppf((1 + confidence) / 2., n-1)
            #h = np.nanstd(float_arr) for standard dev
            CIstats.at['95% CI',col]= h
            CIstats.at['mean',col]= m
            CIstats.at['upper bound',col]= m + h     
            CIstats.at['lower bound',col]= m - h  
            
        pvalA1 = stats.ttest_rel(data[iType]['ctrData_A1'], data[iType]['ptxData_A1'], nan_policy='omit')[1]
        pvalACC = stats.ttest_rel(data[iType]['ctrData_ACC'], data[iType]['ptxData_ACC'], nan_policy='omit')[1]
        if pvalA1 < 0.05:
            sigA1 = 'red'
        else:
            sigA1 = 'black' 
            
        if pvalACC < 0.05:
            sigACC = 'red'
        else:
            sigACC = 'black'                
        
        
        
        for iFiber in ['A1','ACC']: 
            plt.figure(figsize=[2,4.5])
            for iCell in list(data[iType].index):    
                names = ['ctr','ptx']
                values = [data[iType].at[iCell,'ctrData_'+iFiber],data[iType].at[iCell,'ptxData_'+iFiber]]
                plt.plot(names, values, color = 'lightgrey')
                
            plt.title('peak_'+iType+'_'+iFiber)
            linevalues = [0,0]
            plt.ylim((-10,20))
            plt.plot(names,linevalues,'k--',alpha=0.7)
            plt.tight_layout()       
            if iFiber == 'A1':
                plt.text(0.4, 17, "%.3f" % pvalA1, color = sigA1) 
            if iFiber == 'ACC':
                plt.text(0.4, 17, "%.3f" % pvalACC, color = sigACC) 
    
    for iFiber in ['A1','ACC']:
        pval = stats.ttest_ind(data['IB']['ctrData_'+iFiber], data['RS']['ctrData_'+iFiber], nan_policy='omit')[1]
        print('peak_'+iFiber+'_between cell types t-test p val is: '+str(pval))    
        

    return difPeak




#%%
def GABAtoMEIcorrelation(opsinSwapList, averaging, difPeak):

    #load data
    #organize data in pairs, pre and post drug
    #get pulse ratios
    #plot with each other, straight line then dotted for post

    import tkinter
    import pickle

    from pathlib import Path


    savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\GABA correlation with MEI")

    for cellType in ['RS','IB']:
        # make a list with all folder names including cellType:
        import os
        allnames = os.listdir(savedLoc)
        selectednames = [x for x in allnames if cellType in x]
        
        
        import pandas as pd
        import numpy as np
    
        coincidentData = pd.DataFrame()
        
        peakData = pd.DataFrame({'cell ID':[*selectednames]}).set_index('cell ID')
        
        peakData['0ms_frontal single']=""
        peakData['0ms_frontal paired']=""
        peakData['0ms_sensory single']=""
        peakData['0ms_sensory paired']=""
    
    
    
        for i in selectednames:
            print('processing...'+str(i)) 
            # point at data file to view
            cellPath = savedLoc / i
            workspacedf = pd.DataFrame()
            
            for file in os.listdir(cellPath):      
                for delay in [0]:                                    
                    if '_'+str(delay)+'ms' in file:
                        tkinter.Tk().withdraw()
                        loadedData = pickle.load(open(cellPath / file, 'rb'))
                        for k in loadedData.keys():
                            if '_data' in k:
                                workspacedf[str(delay)+'_'+str(k)] = loadedData[k]
    
    
            
            try:
                if i in opsinSwapList:
                    
                    coincidentData['actualCoincident'] = workspacedf[str(delay)+'_'+'paired pulse map_data']
                    coincidentData['arithmeticSum'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf[str(delay)+'_'+'pulse 1 map_data']
                    
                        
                        
                if i not in opsinSwapList: # same as above if in opsinSwapList
                    
                    coincidentData['actualCoincident'] = workspacedf[str(delay)+'_'+'paired pulse map_data']
                    coincidentData['arithmeticSum'] = workspacedf[str(delay)+'_'+'pulse 2 map_data'] + workspacedf[str(delay)+'_'+'pulse 1 map_data']
                    
                   
                        
                #without drug
                maxLocActual = np.argmax(coincidentData['actualCoincident'][1000:1300],axis = 0) +1000
                maxValActual = []
                actualBL = np.mean(coincidentData['actualCoincident'][990:999],axis = 0)
                maxValActual = np.mean(coincidentData['actualCoincident'][maxLocActual-3 : maxLocActual+3], 0) - actualBL       
                
                maxLocSum = np.argmax(coincidentData['arithmeticSum'][1000:1300],axis = 0) +1000
                maxValSum = []
                sumBL = np.mean(coincidentData['arithmeticSum'][990:999],axis = 0)
                maxValSum = np.mean(coincidentData['arithmeticSum'][maxLocSum-3 : maxLocSum+3], 0) - sumBL
    
                peakData.at[str(i),str(delay)+'ms_sensory single'] = maxValSum #now has to equal arithmetic addition of traces peak
                peakData.at[str(i),str(delay)+'ms_sensory paired'] = maxValActual #now has to equal coincident
                peakData.at[str(i),str(delay)+'ms_frontal single'] = maxValSum # same as above
                peakData.at[str(i),str(delay)+'ms_frontal paired'] = maxValActual # same as above
 
                
            except:
                peakData.at[str(i),str(delay)+'ms_sensory single'] = np.nan
                peakData.at[str(i),str(delay)+'ms_sensory paired'] = np.nan
                peakData.at[str(i),str(delay)+'ms_frontal single'] = np.nan
                peakData.at[str(i),str(delay)+'ms_frontal paired'] = np.nan

    
        #get ratios
            
        pairedpeakRatio = pd.DataFrame(index=peakData.index)
        
        pairedpeakRatio['0ms_frontal'] = peakData['0ms_frontal paired'] / peakData['0ms_frontal single']
        pairedpeakRatio['0ms_sensory'] = peakData['0ms_sensory paired'] / peakData['0ms_sensory single']
        pairedpeakRatio['ACC GABA amplitude'] = difPeak[cellType]['ACC difference']
        pairedpeakRatio['AUD GABA amplitude'] = difPeak[cellType]['A1 difference']
        pairedpeakRatio['fiber averaged GABA amplitude'] = (pairedpeakRatio['ACC GABA amplitude'] + pairedpeakRatio['AUD GABA amplitude']) / 2
        
        # mouse averaging
        if averaging == 'mouse':
            pairedpeakRatio.index = pairedpeakRatio.index.map(lambda x: str(x)[:-9])
            workspaceMousedf = pairedpeakRatio.copy()
            workspaceMousedf = workspaceMousedf.astype(float)
            strippedID = []
            for i in selectednames:
                strippedID.append(i[0:-9])
            workspaceMousedf['stripped Names']=strippedID
            grp_mouse = workspaceMousedf.groupby(['stripped Names'])
            pairedpeakMouseRatio = grp_mouse.mean()
            
        elif averaging == 'cell':
            pairedpeakMouseRatio = pairedpeakRatio.astype(float)
                
        
        if cellType == 'RS':
            allData_RS = pairedpeakMouseRatio.copy()
        elif cellType == 'IB':
            allData_IB = pairedpeakMouseRatio.copy()    
        

    
    #plotting correlation
    from matplotlib import pyplot as plt
    from scipy import stats
    x = allData_RS['fiber averaged GABA amplitude'].append(allData_IB['fiber averaged GABA amplitude'])     
    y = allData_RS['0ms_sensory'].append(allData_IB['0ms_sensory'])
    mask = ~np.isnan(y)
    xmask = x.where(mask.values)
    xmask = xmask.dropna()
    y = y.dropna()
    plt.figure()
    plt.scatter(allData_IB['fiber averaged GABA amplitude'],allData_IB['0ms_sensory'],color='blue',label='IB')
    plt.scatter(allData_RS['fiber averaged GABA amplitude'],allData_RS['0ms_sensory'],color='orange',label='RS')
    slope, intercept, r, p, se = stats.linregress(xmask,y)
    plt.plot(xmask, intercept + slope*xmask, 'r')
    plt.title('per '+averaging+' Pearson r ='+"{0:.3f}".format(r))
    plt.xlabel('inhibition (quantified from PTX)')
    plt.ylabel('0ms MEI')
    plt.legend()



#%%

def raster(cellType, delay1, delay2, delay3, delay4, replacePolicy, addition, thresholdLower, thresholdUpper, averaging, point):
    
    import tkinter
    from tkinter.filedialog import askopenfilename
    import pickle
    import pandas as pd
    import numpy as np
    
    delayList = [delay1,delay2,delay3,delay4]
    
    from pathlib import Path
    savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\suprathreshold A1_ACC")

    # make a list with all folder names including cellType:
    import os
    allnames = os.listdir(savedLoc)
    selectednames = [x for x in allnames if cellType in x]


    allData = {}    
    allPeaks = {}
    
    import pandas as pd
    spikes = pd.DataFrame(index = selectednames)
    spikes['0_single'] = 0
    spikes['0_paired'] = 0
    spikes['50_single'] = 0
    spikes['50_paired'] = 0
    spikes['100_single'] = 0
    spikes['100_paired'] = 0
    spikes['250_single'] = 0
    spikes['250_paired'] = 0


        
    sNums = pd.DataFrame(index = selectednames)
    sNums['0_single'] = 0
    sNums['0_paired'] = 0
    sNums['50_single'] = 0
    sNums['50_paired'] = 0
    sNums['100_single'] = 0
    sNums['100_paired'] = 0
    sNums['250_single'] = 0
    sNums['250_paired'] = 0
    
    
    for i in selectednames:
        allPeaks[i] = {}
        allData[i] = {}

    
    
    peakDict = {}
    peakDict['0_pulse 2 map_data'] = [0]
    peakDict['0_pulse 1 map_data'] = [0]
    peakDict['0_paired pulse map_data'] = [0]
    peakDict['50_pulse 1 map_data'] = [0]
    peakDict['50_pulse 2 map_data'] = [0]
    peakDict['50_paired pulse map_data'] = [0]
    peakDict['50_paired pulse map_swap_data'] = [0]
    peakDict['100_pulse 1 map_data'] = [0]
    peakDict['100_pulse 2 map_data'] = [0]
    peakDict['100_paired pulse map_data'] = [0]
    peakDict['100_paired pulse map_swap_data'] = [0]    
    peakDict['250_pulse 1 map_data'] = [0]
    peakDict['250_pulse 2 map_data'] = [0]
    peakDict['250_paired pulse map_data'] = [0]
    peakDict['250_paired pulse map_swap_data'] = [0]
    


    sweepNums = {}
    sweepNums['0_pulse 2 map_data'] = 0
    sweepNums['0_pulse 1 map_data'] = 0
    sweepNums['0_paired pulse map_data'] = 0
    sweepNums['50_pulse 1 map_data'] = 0
    sweepNums['50_pulse 2 map_data'] = 0
    sweepNums['50_paired pulse map_data'] = 0
    sweepNums['50_paired pulse map_swap_data'] = 0
    sweepNums['100_pulse 1 map_data'] = 0
    sweepNums['100_pulse 2 map_data'] = 0
    sweepNums['100_paired pulse map_data'] = 0
    sweepNums['100_paired pulse map_swap_data'] = 0    
    sweepNums['250_pulse 1 map_data'] = 0
    sweepNums['250_pulse 2 map_data'] = 0
    sweepNums['250_paired pulse map_data'] = 0
    sweepNums['250_paired pulse map_swap_data'] = 0


    gaba = pd.DataFrame(index = selectednames)
    gaba['inhibition frontal'] = 0
    gaba['inhibition sensory'] = 0



    for i in selectednames:
        print('processing...'+str(i)) 
        # point at data file to view
        cellPath = savedLoc / i
        workspaceDict = {}
        
        
        for file in os.listdir(cellPath):      
            for delay in delayList:
                if '_'+str(delay)+'ms' in file:
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    for k in loadedData.keys():
                        if '_data' in k:
                            workspaceDict[str(delay)+'_'+str(k)] = loadedData[k]
        

        #dealing with unequal number of sweeps
        
        dict0 = {}
        dict50 = {}
        dict100 = {}
        dict250 = {}
        
        
        workspaceDict2 = workspaceDict.copy()
        
        for k, v in workspaceDict.items():
            # for coincident
            if '50_' not in k and '100_' not in k:
                dict0[k] = len(v[0])
                
            # for 50 ms delay
            if '50_' in k and '250_' not in k:
                dict50[k] = len(v[0])
                
            # for 100 ms delay
            if '100_' in k:
                dict100[k] = len(v[0])
                
            # for 250 ms delay
            if '250_' in k:
                dict250[k] = len(v[0])
  

        
        for idict in [dict0, dict50, dict100, dict250]:
            list1 = list(idict.values())
            try:
                minimum = min(list1)
                for k, v in idict.items():
                    if v != minimum:
                        workspaceDict2[k] = workspaceDict[k][:,:-1]
            except:
                continue

                   
    
        allData[i] = workspaceDict2
        for k, v in allData[i].items():  
            
            from scipy import signal
            allPeaks[i][k] = np.array(0)
                
            for isweep in range(len(v[0])):
                peaks = signal.find_peaks(v[:,isweep], distance=40, prominence=10, height=-10)
                allPeaks[i][k] = np.append(allPeaks[i][k],peaks[0])
                
        #counting spikes  

    # for i in selectednames:    
        
        gabadf = pd.DataFrame()
        
        for k, v in allPeaks[i].items():
            
            
            if '50' not in k and '00' not in k:                
                if '_paired' in k:
                    spikes.at[i,'0_paired'] = sum(1 for ispike in v if 1200>ispike>1000)
                    sNums.at[i,'0_paired'] = len(allData[i][k][0])
                if '_pulse' in k:
                    spikes.at[i,'0_single'] = spikes.at[i,'0_single'] + sum(1 for ispike in v if 1200>ispike>1000)
                    sNums.at[i,'0_single'] = sNums.at[i,'0_single'] + len(allData[i][k][0])
                    
                    for trace in range(0,len(workspaceDict[k][0])):
                        peaks = signal.find_peaks(workspaceDict[k][:,trace], distance=40, prominence=10, height=-10)
                        if any(3800>x>900 for x in peaks[0]) == False:
                            gabadf[k+'_'+str(trace)] = workspaceDict[k][:,trace]
                            
            if '50' in k and '250' not in k:                
                if '_paired' in k:
                    spikes.at[i,'50_paired'] = spikes.at[i,'50_paired'] + sum(1 for ispike in v if 1200>ispike>1000 or 1700>ispike>1500)
                    sNums.at[i,'50_paired'] = sNums.at[i,'50_paired'] + 2*len(allData[i][k][0])
                if '_pulse' in k:
                    spikes.at[i,'50_single'] = spikes.at[i,'50_single'] + sum(1 for ispike in v if 1200>ispike>1000)    
                    sNums.at[i,'50_single'] = sNums.at[i,'50_single'] + len(allData[i][k][0])
                    
                    for trace in range(0,len(workspaceDict[k][0])):
                        peaks = signal.find_peaks(workspaceDict[k][:,trace], distance=40, prominence=10, height=-10)
                        if any(3800>x>900 for x in peaks[0]) == False:
                            gabadf[k+'_'+str(trace)] = workspaceDict[k][:,trace]
                            
            if '100' in k:                
                if '_paired' in k:
                    spikes.at[i,'100_paired'] = spikes.at[i,'100_paired'] + sum(1 for ispike in v if 1200>ispike>1000 or 2200>ispike>2000)
                    sNums.at[i,'100_paired'] = sNums.at[i,'100_paired'] + 2*len(allData[i][k][0])
                if '_pulse' in k:
                    spikes.at[i,'100_single'] = spikes.at[i,'100_single'] + sum(1 for ispike in v if 1200>ispike>1000) 
                    sNums.at[i,'100_single'] = sNums.at[i,'100_single'] + len(allData[i][k][0])
                   
                    for trace in range(0,len(workspaceDict[k][0])):
                        peaks = signal.find_peaks(workspaceDict[k][:,trace], distance=40, prominence=10, height=-10)
                        if any(3800>x>900 for x in peaks[0]) == False:
                            gabadf[k+'_'+str(trace)] = workspaceDict[k][:,trace]
                            
            if '250' in k:                
                if '_paired' in k:
                    spikes.at[i,'250_paired'] = spikes.at[i,'250_paired'] + sum(1 for ispike in v if 1200>ispike>1000 or 3700>ispike>3500)
                    sNums.at[i,'250_paired'] = sNums.at[i,'250_paired'] + 2*len(allData[i][k][0])
                if '_pulse' in k:
                    spikes.at[i,'250_single'] = spikes.at[i,'250_single'] + sum(1 for ispike in v if 1200>ispike>1000)    
                    sNums.at[i,'250_single'] = sNums.at[i,'250_single'] + len(allData[i][k][0])
                   
                    for trace in range(0,len(workspaceDict[k][0])):
                        peaks = signal.find_peaks(workspaceDict[k][:,trace], distance=40, prominence=10, height=-10)
                        if any(3800>x>900 for x in peaks[0]) == False:
                            gabadf[k+'_'+str(trace)] = workspaceDict[k][:,trace]
                            
    
        gabaPulse1 = gabadf[[x for x in gabadf.columns if 'pulse 1' in x]]
        gabaPulse2 = gabadf[[x for x in gabadf.columns if 'pulse 2' in x]]
            
    #   cellmean = gabadf.mean(axis=1)
        pulse1mean = gabaPulse1.mean(axis=1)
        pulse2mean = gabaPulse2.mean(axis=1)
        
        pulse1baseline = np.mean(pulse1mean[900:999])
        pulse2baseline = np.mean(pulse2mean[900:999])
        
        if point == '0':
            pulse1inhibition = max(pulse1mean[1000:1300])
            pulse2inhibition = max(pulse2mean[1000:1300])
        elif point == '50':
            pulse1inhibition = np.mean(pulse1mean[1500:1550])
            pulse2inhibition = np.mean(pulse2mean[1500:1550])
        elif point == '100':
            pulse1inhibition = np.mean(pulse1mean[2000:2050])
            pulse2inhibition = np.mean(pulse2mean[2000:2050])
        elif point == 'global':
            gabamin_pulse1 = np.argmin(pulse1mean)
            gabamin_pulse2 = np.argmin(pulse2mean)
            pulse1inhibition = np.mean(pulse1mean[gabamin_pulse1-25:gabamin_pulse1+25])
            pulse2inhibition = np.mean(pulse2mean[gabamin_pulse2-25:gabamin_pulse2+25])
            
        #how far from baseline, neg means above, pos means below, currently includes both inhibition from frontal and sensory in one value
        gaba.loc[i,'inhibition frontal'] = pulse1baseline - pulse1inhibition
        gaba.loc[i,'inhibition sensory'] = pulse2baseline - pulse2inhibition
        gaba.loc[i,'inhibition cell average'] = (gaba.loc[i,'inhibition frontal']+gaba.loc[i,'inhibition sensory'])/2


    if addition == 'on':
        sNums['0_single'] = sNums['0_single'] / 2
        
    freq = spikes.div(sNums) 
    
    for column in ['0_single','50_single','100_single','250_single']:
        freq.loc[freq[column] <= thresholdLower, column] = np.nan
        freq.loc[freq[column] >= thresholdUpper, column] = np.nan
    
    
    ratios = pd.DataFrame(index = selectednames)
    ratios['0ms interaction'] = freq['0_paired']/freq['0_single']
    ratios['50ms interaction'] = freq['50_paired']/freq['50_single']
    ratios['100ms interaction'] = freq['100_paired']/freq['100_single']
    ratios['250ms interaction'] = freq['250_paired']/freq['250_single']


    if averaging == 'mouse':
        ratios.index = ratios.index.map(lambda x: str(x)[:-9])
        workspaceMousedf = ratios.copy()
        workspaceMousedf = workspaceMousedf.astype(float)
        
        strippedID = []
        for i in selectednames:
            strippedID.append(i[0:-9])
        workspaceMousedf['stripped Names']=strippedID
        grp_mouse = workspaceMousedf.groupby(['stripped Names'])
        peakMouseRatio = grp_mouse.mean()         
        
        gaba['stripped Names']=strippedID
        grp_gaba = gaba.groupby(['stripped Names'])
        grouped_gaba = grp_gaba.mean()
        
    elif averaging == 'cell':
        peakMouseRatio = ratios.copy()
        grouped_gaba = gaba.copy()
        
    #get CI stats
    CIstats = pd.DataFrame(index=['95% CI','mean','upper bound','lower bound'])
    
    CIstats['0ms interaction']= ''
    CIstats['50ms interaction']= ''
    CIstats['100ms interaction'] = ''
    CIstats['250ms interaction']= ''

    
    import scipy.stats as stats

    for col in list(CIstats.columns): 
        a = peakMouseRatio[col].values
        float_arr = np.vstack(a[:]).astype(np.float)
        # n = len(float_arr)
        n = np.count_nonzero(~np.isnan(float_arr))
        m = peakMouseRatio[col].mean()
        se = stats.sem(float_arr, nan_policy = 'omit')
        h = se * stats.t.ppf((1 + 0.95) / 2., n-1)
        #h = np.nanstd(float_arr) for standard dev
        CIstats.at['95% CI',col]= h
        CIstats.at['mean',col]= m
        CIstats.at['upper bound',col]= m + h     
        CIstats.at['lower bound',col]= m - h
        CIstats.at['one sample t-test p val',col] = stats.ttest_1samp(a,1.0,nan_policy='omit')[1]
        if CIstats.at['one sample t-test p val',col] < 0.05:
            CIstats.at['significant?',col] = 'red'
        else:
            CIstats.at['significant?',col] = 'black'
            
    from matplotlib import pyplot as plt
    
    #plotting correlation
    x = grouped_gaba['inhibition frontal']     
    y = peakMouseRatio['0ms interaction']
    mask = ~np.isnan(peakMouseRatio['0ms interaction'])
    xmask = x.where(mask.values)
    xmask = xmask.dropna()
    y = y.dropna()
    plt.figure()
    plt.scatter(xmask,y)
    slope, intercept, r, p, se = stats.linregress(xmask,y)
    plt.plot(xmask, intercept + slope*xmask, 'r')
    plt.title('per '+averaging+' Pearson r ='+"{0:.3f}".format(r))
    plt.xlabel('mV below baseline')
    plt.ylabel('0ms MEI')
    
    
    #plotting
    plt.figure(figsize=(3.5,5))
    names = np.asarray([0,50,100,250])
    values = np.asarray([CIstats.at['mean','0ms interaction'],CIstats.at['mean','50ms interaction'],CIstats.at['mean','100ms interaction'],CIstats.at['mean','250ms interaction']])
    linevalues = [1,1,1,1]
    plt.ylim((0.3,3.5))
    yerrUpper = np.asarray([CIstats.at['upper bound','0ms interaction'],CIstats.at['upper bound','50ms interaction'],CIstats.at['upper bound','100ms interaction'],CIstats.at['upper bound','250ms interaction']])
    yerrLower = np.asarray([CIstats.at['lower bound','0ms interaction'],CIstats.at['lower bound','50ms interaction'],CIstats.at['lower bound','100ms interaction'],CIstats.at['lower bound','250ms interaction']])
    flat_yerrUpper = yerrUpper.flatten()
    flat_yerrLower = yerrLower.flatten()
    plt.fill_between(names, flat_yerrUpper, flat_yerrLower,alpha=0.5,interpolate=True,color='navajowhite')
    plt.plot(names,values,'darkorange', marker='.')

    plt.plot(names,linevalues,'k--',alpha=0.7)
    plt.text(205, 2.3, 'n = '+str(len(peakMouseRatio['0ms interaction'])), fontsize=14)


    plt.text(0, 2.8, "%.3f" % CIstats.at['one sample t-test p val','0ms interaction'], color = CIstats.at['significant?','0ms interaction'])
    plt.text(45, 2.8, "%.3f" % CIstats.at['one sample t-test p val','50ms interaction'], color = CIstats.at['significant?','50ms interaction'])
    plt.text(90, 2.8, "%.3f" % CIstats.at['one sample t-test p val','100ms interaction'], color = CIstats.at['significant?','100ms interaction'])
    plt.text(230, 2.8, "%.3f" % CIstats.at['one sample t-test p val','250ms interaction'], color = CIstats.at['significant?','250ms interaction'])

    for cell in list(peakMouseRatio.index):
        names = np.asarray([0,50,100,250])
        values = np.asarray([peakMouseRatio.at[cell,'0ms interaction'],peakMouseRatio.at[cell,'50ms interaction'],peakMouseRatio.at[cell,'100ms interaction'],peakMouseRatio.at[cell,'250ms interaction']])
        linevalues = [1,1,1,1]
        plt.ylim((0.3,3.5))
        plt.plot(names,values,alpha=0.5, marker='.',label=cell)
    

    plt.legend()
    plt.show()
    
    

    return peakMouseRatio


#%% 
def supraGABA(cellType, delay1, delay2, delay3, delay4, baseline):
    
    import tkinter
    from tkinter.filedialog import askopenfilename
    import pickle

    delayList = [delay1,delay2,delay3,delay4]
    
    from pathlib import Path
    savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\suprathreshold A1_ACC")

    # make a list with all folder names including cellType:
    import os
    allnames = os.listdir(savedLoc)
    selectednames = [x for x in allnames if cellType in x]


    import pandas as pd
    import numpy as np

    allData = {}
    allTraces = {'A1':{},
                 'ACC':{}}

    for i in selectednames:
        allData[i] = {}
        allTraces['A1'][i] = {}
        allTraces['ACC'][i] = {}
    
    for i in selectednames:
        print('processing...'+str(i)) 
        # point at data file to view
        cellPath = savedLoc / i
        workspaceDict = {}
        
        
        for file in os.listdir(cellPath):      
            for delay in delayList:
                if '_'+str(delay)+'ms' in file:
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    for k in loadedData.keys():
                        if '_data' in k:
                            workspaceDict[str(delay)+'_'+str(k)] = loadedData[k]

        #dealing with unequal number of sweeps   
        dict0 = {}
        dict50 = {}
        dict100 = {}
        dict250 = {}

        workspaceDict2 = workspaceDict.copy()
        
        for k, v in workspaceDict.items():
            # for coincident
            if '50_' not in k and '100_' not in k:
                dict0[k] = len(v[0])
                
            # for 50 ms delay
            if '50_' in k and '250_' not in k:
                dict50[k] = len(v[0])
                
            # for 100 ms delay
            if '100_' in k:
                dict100[k] = len(v[0])
                
            # for 250 ms delay
            if '250_' in k:
                dict250[k] = len(v[0])

        
        for idict in [dict0, dict50, dict100, dict250]:
            list1 = list(idict.values())
            try:
                minimum = min(list1)
                for k, v in idict.items():
                    if v != minimum:
                        workspaceDict2[k] = workspaceDict[k][:,:-1]
            except:
                continue

        allData[i] = workspaceDict2
        
        
        upper = -45
        lower = -60
        

        for k, v in allData[i].items():  
            cellTraces = v.copy().T
            
            from scipy import signal
                
            if 'pulse 1 map' or 'pulse 2 map' in k:
                
                toInclude = []   
                
                #remove traces that have spikes
                for ind, y in enumerate(cellTraces):
                    peaks = signal.find_peaks(y[:], height = -20, threshold = 0)
                                    
                    if np.mean(y[900:999]) < lower or np.mean(y[900:999]) > upper:
                        continue
            
                    elif len(peaks[0]) > 0:
                        continue
                    
                    toInclude.extend([ind])
                    
                    #remove the traces that aren't passing
                    #add it to appripriate fiber dict
               
                nonSpiking = cellTraces[toInclude]
                if 'pulse 1 map' in k:                    
                    allTraces['ACC'][i] = nonSpiking.T
                if 'pulse 2 map' in k:                    
                    allTraces['A1'][i] = nonSpiking.T                

    allTracesAvg = allTraces.copy()
    
    for k, v in allTracesAvg.items():
        for j, c in v.items():
            average = np.mean(c,axis=1)
            if baseline == 0:
                allTracesAvg[k][j] = average
            if baseline == 1:
                allTracesAvg[k][j] = average - np.mean(average[900:999])
                
    from matplotlib import pyplot as plt
    
    for k, v in allTracesAvg.items():
        plt.figure()
        plt.title(cellType + ' ' +k)
        for j, c in v.items():    
            plt.plot(c, label = j)
            

        plt.xlim(700,4500)
        if baseline == 0:
            plt.ylim(-61,-46)
        if baseline == 1:
            plt.ylim(-11,16)
        
        
        plt.figure()
        plt.title(cellType + ' ' +k)
        values = list(allTracesAvg[k].values())
        cellTypeAvg = np.nanmean(values, axis=0)
        plt.plot(cellTypeAvg)
        
        plt.xlim(700,4500)
        if baseline == 0:
            plt.ylim(-61,-46)
        if baseline == 1:
            plt.ylim(-11,16)

    return



#%%

def plotTraces(cellType, fiberTypes):
    
    import tkinter
    from tkinter.filedialog import askopenfilename
    import pickle
    
    plotMin = -3
    plotMax = plotMin + 20
    plotStart = 750
    plotStop = 5500
    
    from matplotlib import pyplot as plt
    from pathlib import Path
    from pathlib import Path

    
    if 'A1' in fiberTypes and 'V1' in fiberTypes:
            savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration A1_V1")
    if 'A1' in fiberTypes and 'ACC' in fiberTypes:
            savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration A1_ACC")
    if 'V1' in fiberTypes and 'ACC' in fiberTypes:
            savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\integration V1_ACC")
    
    # make a list with all folder names including cellType:
    import os
    allnames = os.listdir(savedLoc)
    selectednames = [x for x in allnames if cellType in x]
    
    import numpy as np
    
    for iCell in selectednames:
        print('processing '+str(iCell))
        cellPath = savedLoc / iCell
        for file in os.listdir(cellPath):      
            
            if '_0ms' in file:
                tkinter.Tk().withdraw()
                loadedData = pickle.load(open(cellPath / file, 'rb'))
                
                plt.figure()
                
                if iCell in opsinSwapList:
                    if '_red' in file and 'blue' not in file:
                        label = '0ms_frontal'
                    elif '_blue' in file and 'red' not in file:
                        label = '0ms_sensory'
                    elif '_bluered' in file:
                        label = '0ms_coincident'
                        
                elif iCell not in opsinSwapList:
                    if '_red' in file and 'blue' not in file:
                        label = '0ms_sensory'
                    elif '_blue' in file and 'red' not in file:
                        label = '0ms_frontal'
                    elif '_bluered' in file:
                        label = '0ms_coincident'
                            
                
                for k in loadedData.keys():
                    if '_data' in k:
                        
                        plt.plot(loadedData[k])
                        plt.ylim((plotMin,plotMax))
                        # plt.yticks(np.arange(plotMin, plotMax+1, 20))
                        plt.xlim((plotStart,plotStop))
                        plt.title(label)
                        imagename = str(iCell)+'_'+str(label)
                        
                        plt.close()
                        
                    
            elif '_100ms' in file:
                tkinter.Tk().withdraw()
                loadedData = pickle.load(open(cellPath / file, 'rb'))
                
                plt.figure()
                
                if iCell in opsinSwapList:
                    if '_red' in file and 'blue' not in file:
                        label = '100ms_frontal'
                    elif '_blue' in file and 'red' not in file:
                        label = '100ms_sensory'
                    elif '_redblue' in file:
                        label = '100ms_frontal-sensory'
                    elif '_bluered' in file:
                        label = '100ms_sensory-frontal'
                        
                elif iCell not in opsinSwapList:
                    if '_red' and 'blue' not in file:
                        label = '100ms_sensory'
                    elif '_blue' and 'red' not in file:
                        label = '100ms_frontal'
                    elif '_redblue' in file:
                        label = '100ms_sensory-frontal' 
                    elif '_bluered' in file:
                        label = '100ms_frontal-sensory'                    
                        
                for k in loadedData.keys():
                    if '_data' in k:
                        
                        plt.plot(loadedData[k])
                        plt.ylim((plotMin,plotMax))
                        # plt.yticks(np.arange(plotMin, plotMax+1, 20))
                        plt.xlim((plotStart,plotStop))
                        plt.title(label)
                        
                        imagename = str(iCell)+'_'+str(label)
                        
                        plt.close()                    
                    


        
#%% EPSC/IPSC normalized

def EPSCnorm(method, internal):

    import tkinter
    from tkinter.filedialog import askopenfilename
    import pickle
    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt
    from scipy import signal
    import pandas
    
    import DR_tau_functions as gt
    
    from pathlib import Path
    if internal == 'standard':
        savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\EPSC_IPSC")
    if internal == 'PTX':
        savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\EPSC_IPSC internal PTX")

    # makes a list with all folder names including cellType:
    import os
    allnames = os.listdir(savedLoc)


    allData_ACC = pd.DataFrame(index = [i[:20] for i in allnames])
    allData_AUD = pd.DataFrame(index = [i[:20] for i in allnames])
    
    allIPSC = {}
    allEPSC = {}
    firstEPSP = pd.DataFrame()
    secondEPSP = pd.DataFrame()
    
    #partitions data into EPSP, IPSC and EPSCs, and plot both for every cell
    for iCell in allnames:
        print('processing...'+str(iCell)) 
        # point at data file to view
        cellPath = savedLoc / iCell
        plt.figure()
        plt.title(iCell)
        plt.ylabel('pA')
        plt.xlabel('100 points = 10ms')
        
        for file in os.listdir(cellPath):
            if 'baseLED' in file:
                tkinter.Tk().withdraw()
                loadedData = pickle.load(open(cellPath / file, 'rb'))
                stim1onset = int(float(loadedData['StimTime'][0]) * loadedData['SampleRateAcq'])
                stim2onset = int(float(loadedData['StimTime'][1]) * loadedData['SampleRateAcq'])
                
                if 'F1NA' not in file:
                    firstEPSP[file[:20]] = (loadedData['TTX_data'][stim1onset-100:stim1onset+3000] - 
                                            np.mean(loadedData['TTX_data'][stim1onset-100:stim1onset+3000][0:100]))
                if 'F2NA' not in file:                            
                    secondEPSP[file[:20]] = (loadedData['TTX_data'][stim2onset-100:stim2onset+3000] -
                                            np.mean(loadedData['TTX_data'][stim2onset-100:stim2onset+3000][0:100]))
                
                continue
            tkinter.Tk().withdraw()
            loadedData = pickle.load(open(cellPath / file, 'rb'))
            for k in loadedData.keys():
                if '_data' in k:
                    plt.plot(loadedData[k])
                    if '_70' in file:      
                        allEPSC[file] = {}
                        allEPSC[file]['traceData'] = loadedData[k]
                        allEPSC[file]['stim1onset'] = int(float(loadedData['StimTime'][0]) * loadedData['SampleRateAcq'])
                        allEPSC[file]['stim2onset'] = int(float(loadedData['StimTime'][1]) * loadedData['SampleRateAcq'])
                    elif '_0' in file:
                        allIPSC[file] = {}
                        allIPSC[file]['traceData'] = loadedData[k]
                        allIPSC[file]['stim1onset'] = int(float(loadedData['StimTime'][0]) * loadedData['SampleRateAcq'])
                        allIPSC[file]['stim2onset'] = int(float(loadedData['StimTime'][1]) * loadedData['SampleRateAcq'])
            
    
    
    
    firstEPSP['mean'] = np.mean(firstEPSP, 1)
    secondEPSP['mean'] = np.mean(secondEPSP, 1)
    
    EPSPdf = pd.DataFrame(index = [i[:20] for i in allIPSC.keys()]) 
    
    EPSPtraces_ACC = pd.DataFrame()
    EPSPtraces_AUD = pd.DataFrame()
       
    #analyze EPSPs first
    for iCell in firstEPSP.columns:
        trace = firstEPSP[iCell] - np.mean(firstEPSP[iCell][0:100])
        startEPSP = gt.getIPSCstart(trace, 0.02)
        tau = gt.getIPSCrise(trace,startEPSP)
        EPSPdf.at[iCell[:20],'first tau rise'] = tau
        EPSPdf.at[iCell[:20],'first tau decay'] = gt.getIPSCdecay(trace)
        
        allData_ACC.at[iCell[:20], 'EPSP rise'] = tau
        allData_ACC.at[iCell[:20], 'EPSP decay'] = gt.getIPSCdecay(trace)
        allData_ACC.at[iCell[:20], 'EPSP start'] = startEPSP
        allData_ACC.at[iCell[:20], 'EPSP peak'] = np.argmax(trace[:300])
        EPSPtraces_ACC[iCell[:20]] = trace
        
    for iCell in secondEPSP.columns:
        trace = secondEPSP[iCell] - np.mean(secondEPSP[iCell][0:100])
        startEPSP = gt.getIPSCstart(trace, 0.02)
        tau = gt.getIPSCrise(trace,startEPSP)
        EPSPdf.at[iCell[:20],'second tau rise'] = tau
        EPSPdf.at[iCell[:20],'second tau decay'] = gt.getIPSCdecay(trace)
        
        allData_AUD.at[iCell[:20], 'EPSP rise'] = tau
        allData_AUD.at[iCell[:20], 'EPSP decay'] = gt.getIPSCdecay(trace)
        allData_AUD.at[iCell[:20], 'EPSP start'] = startEPSP
        allData_AUD.at[iCell[:20], 'EPSP peak'] = np.argmax(trace[:300])       
        EPSPtraces_AUD[iCell[:20]] = trace
        
        
    risedf = pd.DataFrame(columns=['first fiber EPSC tau','second fiber EPSC tau','first fiber IPSC tau','second fiber IPSC tau'])
    decaydf = pd.DataFrame(columns=['first fiber EPSC tau','second fiber EPSC tau','first fiber IPSC tau','second fiber IPSC tau'])
    
    ACCtraces = pd.DataFrame()
    AUDtraces = pd.DataFrame() 
    
    latencydf_first = pd.DataFrame(index = [i[:20] for i in allIPSC.keys()])
    latencydf_second = pd.DataFrame(index = [i[:20] for i in allIPSC.keys()])
    
    
    if internal == 'PTX':
        for iCell in allIPSC.keys():
            BLfirstIPSC = allIPSC[iCell]['traceData'][allIPSC[iCell]['stim1onset']-100:allIPSC[iCell]['stim1onset']+4000]-np.mean(
                                        allIPSC[iCell]['traceData'][allIPSC[iCell]['stim1onset']-100:allIPSC[iCell]['stim1onset']+4000][0:100])
            BLsecondIPSC = allIPSC[iCell]['traceData'][allIPSC[iCell]['stim2onset']-100:allIPSC[iCell]['stim2onset']+4000]-np.mean(
                                        allIPSC[iCell]['traceData'][allIPSC[iCell]['stim2onset']-100:allIPSC[iCell]['stim2onset']+4000][0:100])
            if 'NA' not in iCell:    
                ACCtraces[iCell+'_IPSC'] = BLfirstIPSC
                AUDtraces[iCell+'_IPSC'] = BLsecondIPSC
            if 'NA' in iCell:
                omittedFiber = iCell[iCell.index('NA')-2:iCell.index('NA')]            
                if omittedFiber == 'F1':                   
                    AUDtraces[iCell+'_IPSC'] = BLsecondIPSC
                if omittedFiber == 'F2':
                    ACCtraces[iCell+'_IPSC'] = BLfirstIPSC    
                    
        for iCell in allEPSC.keys():
            BLfirstEPSC = allEPSC[iCell]['traceData'][allEPSC[iCell]['stim1onset']-100:allEPSC[iCell]['stim1onset']+4000]-np.mean(
                                        allEPSC[iCell]['traceData'][allEPSC[iCell]['stim1onset']-100:allEPSC[iCell]['stim1onset']+4000][0:100])
            BLsecondEPSC = allEPSC[iCell]['traceData'][allEPSC[iCell]['stim2onset']-100:allEPSC[iCell]['stim2onset']+4000]-np.mean(
                                        allEPSC[iCell]['traceData'][allEPSC[iCell]['stim2onset']-100:allEPSC[iCell]['stim2onset']+4000][0:100])    
            if 'NA' not in iCell:    
                ACCtraces[iCell+'_EPSC'] = BLfirstEPSC
                AUDtraces[iCell+'_EPSC'] = BLsecondEPSC
            if 'NA' in iCell:
                omittedFiber = iCell[iCell.index('NA')-2:iCell.index('NA')]            
                if omittedFiber == 'F1':                   
                    AUDtraces[iCell+'_EPSC'] = BLsecondEPSC
                if omittedFiber == 'F2':
                    ACCtraces[iCell+'_EPSC'] = BLfirstEPSC    
                    
    if internal == 'standard':
    
        for iCell in allIPSC.keys():
            
           
            if method == 'raw':
                BLfirstIPSC = allIPSC[iCell]['traceData'][allIPSC[iCell]['stim1onset']-100:allIPSC[iCell]['stim1onset']+4000]-np.mean(
                                        allIPSC[iCell]['traceData'][allIPSC[iCell]['stim1onset']-100:allIPSC[iCell]['stim1onset']+4000][0:100])
                BLsecondIPSC = allIPSC[iCell]['traceData'][allIPSC[iCell]['stim2onset']-100:allIPSC[iCell]['stim2onset']+4000]-np.mean(
                                        allIPSC[iCell]['traceData'][allIPSC[iCell]['stim2onset']-100:allIPSC[iCell]['stim2onset']+4000][0:100])
                threshold = 1.5
                firstIPSCstart = gt.getIPSCstart(BLfirstIPSC, threshold)
                secondIPSCstart = gt.getIPSCstart(BLsecondIPSC, threshold)
                
                latencydf_first.at[iCell[:20],'IPSC'] = firstIPSCstart
                latencydf_second.at[iCell[:20],'IPSC'] = secondIPSCstart
                
                
                
            if method == 'norm_samestart':
                BLfirstIPSC_prenorm = allIPSC[iCell]['traceData'][allIPSC[iCell]['stim1onset']-100:allIPSC[iCell]['stim1onset']+4000]-np.mean(
                                        allIPSC[iCell]['traceData'][allIPSC[iCell]['stim1onset']-100:allIPSC[iCell]['stim1onset']+4000][0:100])
                BLsecondIPSC_prenorm = allIPSC[iCell]['traceData'][allIPSC[iCell]['stim2onset']-100:allIPSC[iCell]['stim2onset']+4000]-np.mean(
                                        allIPSC[iCell]['traceData'][allIPSC[iCell]['stim2onset']-100:allIPSC[iCell]['stim2onset']+4000][0:100])
                threshold = 1.5
                firstIPSCstart = gt.getIPSCstart(BLfirstIPSC_prenorm, threshold)
                secondIPSCstart = gt.getIPSCstart(BLsecondIPSC_prenorm, threshold)
                
                BLfirstIPSC = BLfirstIPSC_prenorm/max(BLfirstIPSC_prenorm)
                BLsecondIPSC = BLsecondIPSC_prenorm/max(BLsecondIPSC_prenorm)
                
                latencydf_first.at[iCell[:20],'IPSC'] = firstIPSCstart
                latencydf_second.at[iCell[:20],'IPSC'] = secondIPSCstart
                
            if method == 'norm_uniquestart':
                
                BLfirstIPSC_prenorm = allIPSC[iCell]['traceData'][allIPSC[iCell]['stim1onset']-100:allIPSC[iCell]['stim1onset']+4000]-np.mean(
                                        allIPSC[iCell]['traceData'][allIPSC[iCell]['stim1onset']-100:allIPSC[iCell]['stim1onset']+4000][0:100])
                BLsecondIPSC_prenorm = allIPSC[iCell]['traceData'][allIPSC[iCell]['stim2onset']-100:allIPSC[iCell]['stim2onset']+4000]-np.mean(
                                        allIPSC[iCell]['traceData'][allIPSC[iCell]['stim2onset']-100:allIPSC[iCell]['stim2onset']+4000][0:100])
                
                BLfirstIPSC = BLfirstIPSC_prenorm/max(BLfirstIPSC_prenorm)
                BLsecondIPSC = BLsecondIPSC_prenorm/max(BLsecondIPSC_prenorm)
                
                threshold = 0.015
                firstIPSCstart = gt.getIPSCstart(BLfirstIPSC, threshold)
                secondIPSCstart = gt.getIPSCstart(BLsecondIPSC, threshold)
                
                latencydf_first.at[iCell[:20],'IPSC'] = firstIPSCstart
                latencydf_second.at[iCell[:20],'IPSC'] = secondIPSCstart
                
                #just to test how threshold affects start
                threshold = 1.5
                print(iCell+' first IPSC '+str(firstIPSCstart)+' '+str(gt.getIPSCstart(BLfirstIPSC_prenorm, threshold)))
                print(iCell+' second IPSC '+str(secondIPSCstart)+' '+str(gt.getIPSCstart(BLsecondIPSC_prenorm, threshold)))   
                
            
            if 'NA' not in iCell:    
                ACCtraces[iCell+'_IPSC'] = BLfirstIPSC
                AUDtraces[iCell+'_IPSC'] = BLsecondIPSC
                
                allData_ACC.at[iCell[:20],'IPSC peak'] = np.argmax(BLfirstIPSC[:300])
                allData_AUD.at[iCell[:20],'IPSC peak'] = np.argmax(BLsecondIPSC[:300])
                allData_ACC.at[iCell[:20],'IPSC start'] = firstIPSCstart
                allData_AUD.at[iCell[:20],'IPSC start'] = secondIPSCstart
                
                
                #get rise and decay tau for fiber 1
                #rise
                
                tau = gt.getIPSCrise(BLfirstIPSC, firstIPSCstart)
                risedf.at[iCell[:iCell.index('_F1')],'first fiber IPSC tau'] = tau    
                    
                
                #decay
                tau = gt.getIPSCdecay(BLfirstIPSC)
                decaydf.at[iCell[:iCell.index('_F1')],'first fiber IPSC tau'] = tau
                
                #get rise and decay tau for fiber 2
                #rise
                tau = gt.getIPSCrise(BLsecondIPSC, secondIPSCstart)
                risedf.at[iCell[:iCell.index('_F1')],'second fiber IPSC tau'] = tau   
                
                
                #decay
                tau = gt.getIPSCdecay(BLsecondIPSC)
                decaydf.at[iCell[:iCell.index('_F1')],'second fiber IPSC tau'] = tau
                
                
                
            #handling case when one or another fiber isn't being used
            if 'NA' in iCell:
                omittedFiber = iCell[iCell.index('NA')-2:iCell.index('NA')]
                
                if omittedFiber == 'F1':
                    
                    allData_AUD.at[iCell[:20],'IPSC peak'] = np.argmax(BLsecondIPSC[:300])
                    allData_AUD.at[iCell[:20],'IPSC start'] = secondIPSCstart
                    
                    AUDtraces[iCell+'_IPSC'] = BLsecondIPSC
                    
                    #get rise and decay tau for fiber 2
                    #rise
                    tau = gt.getIPSCrise(BLsecondIPSC, secondIPSCstart)
                    risedf.at[iCell[:iCell.index('_F1')],'second fiber IPSC tau'] = tau   
                                    
                    #decay
                    tau = gt.getIPSCdecay(BLsecondIPSC)
                    decaydf.at[iCell[:iCell.index('_F1')],'second fiber IPSC tau'] = tau
                    
                        
                if omittedFiber == 'F2':       
                    
                    allData_ACC.at[iCell[:20],'IPSC peak'] = np.argmax(BLfirstIPSC[:300])            
                    allData_ACC.at[iCell[:20],'IPSC start'] = firstIPSCstart
                    
                    ACCtraces[iCell+'_IPSC'] = BLfirstIPSC
                    
                    #get rise and decay tau for fiber 1
                    #rise
                    tau = gt.getIPSCrise(BLfirstIPSC, firstIPSCstart)
                    risedf.at[iCell[:iCell.index('_F1')],'first fiber IPSC tau'] = tau    
                        
                    
                    #decay
                    tau = gt.getIPSCdecay(BLfirstIPSC)
                    decaydf.at[iCell[:iCell.index('_F1')],'first fiber IPSC tau'] = tau
            
        
    
        for iCell in allEPSC.keys():
            #separate the two pulses
            
            if method == 'raw':
                BLfirstEPSC = allEPSC[iCell]['traceData'][allEPSC[iCell]['stim1onset']-100:allEPSC[iCell]['stim1onset']+4000]-np.mean(
                                        allEPSC[iCell]['traceData'][allEPSC[iCell]['stim1onset']-100:allEPSC[iCell]['stim1onset']+4000][0:100])
                BLsecondEPSC = allEPSC[iCell]['traceData'][allEPSC[iCell]['stim2onset']-100:allEPSC[iCell]['stim2onset']+4000]-np.mean(
                                        allEPSC[iCell]['traceData'][allEPSC[iCell]['stim2onset']-100:allEPSC[iCell]['stim2onset']+4000][0:100])
                threshold = 1.5
                firstEPSCstart = gt.getEPSCstart(BLfirstEPSC, threshold)
                secondEPSCstart = gt.getEPSCstart(BLsecondEPSC, threshold)
                
                latencydf_first.at[iCell[:20],'EPSC'] = firstEPSCstart
                latencydf_second.at[iCell[:20],'EPSC'] = secondEPSCstart
                
            if method == 'norm_samestart':
                BLfirstEPSC_prenorm = allEPSC[iCell]['traceData'][allEPSC[iCell]['stim1onset']-100:allEPSC[iCell]['stim1onset']+4000]-np.mean(
                                        allEPSC[iCell]['traceData'][allEPSC[iCell]['stim1onset']-100:allEPSC[iCell]['stim1onset']+4000][0:100])
                BLsecondEPSC_prenorm = allEPSC[iCell]['traceData'][allEPSC[iCell]['stim2onset']-100:allEPSC[iCell]['stim2onset']+4000]-np.mean(
                                        allEPSC[iCell]['traceData'][allEPSC[iCell]['stim2onset']-100:allEPSC[iCell]['stim2onset']+4000][0:100])
                threshold = 1.5
                firstEPSCstart = gt.getEPSCstart(BLfirstEPSC_prenorm, threshold)
                secondEPSCstart = gt.getEPSCstart(BLsecondEPSC_prenorm, threshold)
                    
                
                BLfirstEPSC = -BLfirstEPSC_prenorm/min(BLfirstEPSC_prenorm)
                BLsecondEPSC = -BLsecondEPSC_prenorm/min(BLsecondEPSC_prenorm)
                
                latencydf_first.at[iCell[:20],'EPSC'] = firstEPSCstart
                latencydf_second.at[iCell[:20],'EPSC'] = secondEPSCstart
                
            if method == 'norm_uniquestart':
                BLfirstEPSC_prenorm = allEPSC[iCell]['traceData'][allEPSC[iCell]['stim1onset']-100:allEPSC[iCell]['stim1onset']+4000]-np.mean(
                                        allEPSC[iCell]['traceData'][allEPSC[iCell]['stim1onset']-100:allEPSC[iCell]['stim1onset']+4000][0:100])
                BLsecondEPSC_prenorm = allEPSC[iCell]['traceData'][allEPSC[iCell]['stim2onset']-100:allEPSC[iCell]['stim2onset']+4000]-np.mean(
                                        allEPSC[iCell]['traceData'][allEPSC[iCell]['stim2onset']-100:allEPSC[iCell]['stim2onset']+4000][0:100])
                
                
                
                BLfirstEPSC = -BLfirstEPSC_prenorm/min(BLfirstEPSC_prenorm)
                BLsecondEPSC = -BLsecondEPSC_prenorm/min(BLsecondEPSC_prenorm)
                
                threshold = 0.015
                firstEPSCstart = gt.getEPSCstart(BLfirstEPSC, threshold)
                secondEPSCstart = gt.getEPSCstart(BLsecondEPSC, threshold)
                
                latencydf_first.at[iCell[:20],'EPSC'] = firstEPSCstart
                latencydf_second.at[iCell[:20],'EPSC'] = secondEPSCstart
                
                #just to test how threshold affects start
                threshold = 1.5
                print(iCell+'first EPSC '+str(firstEPSCstart)+' '+str(gt.getEPSCstart(BLfirstEPSC_prenorm, threshold)))
                print(iCell+'second EPSC '+str(secondEPSCstart)+' '+str(gt.getEPSCstart(BLsecondEPSC_prenorm, threshold)))
                
                
            
            if 'NA' not in iCell:    
                
                ACCtraces[iCell+'_EPSC'] = BLfirstEPSC
                AUDtraces[iCell+'_EPSC'] = BLsecondEPSC
            
                #get rise and decay tau for fiber 1
                #rise
                tau = gt.getEPSCrise(BLfirstEPSC, firstEPSCstart)
                risedf.at[iCell[:iCell.index('_F1')],'first fiber EPSC tau'] = tau    
                    
                
                #decay
                tau = gt.getEPSCdecay(BLfirstEPSC)
                decaydf.at[iCell[:iCell.index('_F1')],'first fiber EPSC tau'] = tau
                
                #get rise and decay tau for fiber 2
                #rise
                tau = gt.getEPSCrise(BLsecondEPSC, secondEPSCstart)
                risedf.at[iCell[:iCell.index('_F1')],'second fiber EPSC tau'] = tau    
                    
                
                #decay
                tau = gt.getEPSCdecay(BLsecondEPSC)
                decaydf.at[iCell[:iCell.index('_F1')],'second fiber EPSC tau'] = tau
                
                
            #handling case when one or another fiber isn't being used
            if 'NA' in iCell:
                omittedFiber = iCell[iCell.index('NA')-2:iCell.index('NA')]
                
                
                if omittedFiber == 'F1':
                    
                    AUDtraces[iCell+'_EPSC'] = BLsecondEPSC
                    
                    #get rise and decay tau for fiber 2
                    #rise
                    tau = gt.getEPSCrise(BLsecondEPSC, secondEPSCstart)
                    risedf.at[iCell[:iCell.index('_F1')],'second fiber EPSC tau'] = tau    
                        
                    
                    #decay
                    tau = gt.getEPSCdecay(BLsecondEPSC)
                    decaydf.at[iCell[:iCell.index('_F1')],'second fiber EPSC tau'] = tau
                            
                if omittedFiber == 'F2':
                    
                    ACCtraces[iCell+'_EPSC'] = BLfirstEPSC
                    
                    #rise
                    tau = gt.getEPSCrise(BLfirstEPSC, firstEPSCstart)
                    risedf.at[iCell[:iCell.index('_F1')],'first fiber EPSC tau'] = tau    
                        
                    
                    #decay
                    tau = gt.getEPSCdecay(BLfirstEPSC)
                    decaydf.at[iCell[:iCell.index('_F1')],'first fiber EPSC tau'] = tau
                
     
        for direction in [risedf, decaydf]:
            for fiber in ['first fiber', 'second fiber']:
                fig = plt.figure()
                # fig.set_size_inches(3,5)
    
                if direction.equals(risedf):
                    plt.ylim(0,4)
                    if 'second' in fiber:          
                        plt.title('AUD rise tau, method='+str(method))
                    if 'first' in fiber:          
                        plt.title('ACC rise tau, method='+str(method))
                if direction.equals(decaydf):
                    plt.ylim(0,30)
                    if 'second' in fiber:          
                        plt.title('AUD decay tau, method='+str(method))
                    if 'first' in fiber:          
                        plt.title('ACC decay tau, method='+str(method))
                for i in direction.index:
                    names = ['EPSC']
                    values = [direction.at[i,fiber+' EPSC tau']]
                    plt.scatter(names,values,c='black')
                    
                    names = ['IPSC']
                    values = [direction.at[i,fiber+' IPSC tau']]
                    plt.scatter(names,values,c='orange')
                    
                fig = plt.figure()
                # fig.set_size_inches(3,5)
                if direction.equals(risedf):
                    plt.ylim(0,4)
                    if 'second' in fiber:          
                        plt.title('AUD rise tau, method='+str(method))
                    if 'first' in fiber:          
                        plt.title('ACC rise tau, method='+str(method))
                if direction.equals(decaydf):
                    plt.ylim(0,30)
                    if 'second' in fiber:          
                        plt.title('AUD decay tau, method='+str(method))
                    if 'first' in fiber:          
                        plt.title('ACC decay tau, method='+str(method))
                plt.bar(np.arange(2),[np.mean(direction[fiber+' EPSC tau']),np.mean(direction[fiber+' IPSC tau'])])
                plt.xticks(np.arange(2),('EPSC','IPSC'))
        
        
        for taudf in [risedf, decaydf]:
            for fiber in ['first', 'second']:
                fig = plt.figure()
                # fig.set_size_inches(3,5)   
                
                if taudf.equals(risedf):
                    plt.ylim(0,4)
                    if fiber == 'first':
                        plt.title('ACC rise, method='+str(method))
                    if fiber == 'second':
                        plt.title('AUD rise, method='+str(method))
                if taudf.equals(decaydf):
                    plt.ylim(0,30)
                    if fiber == 'first':
                        plt.title('ACC decay, method='+str(method))
                    if fiber == 'second':
                        plt.title('AUD decay, method='+str(method))        
                for i in list(taudf.index):    
                    names = ['EPSC', 'IPSC']
                    values = [taudf.at[i, fiber+' fiber EPSC tau'], taudf.at[i, fiber+' fiber IPSC tau']]   
                    plt.plot(names, values, color = 'lightgrey')
                names = ['EPSC', 'IPSC']
                values = [np.mean(taudf[fiber+' fiber EPSC tau']), np.mean(taudf[fiber+' fiber IPSC tau'])]   
                plt.plot(names, values, color = 'k')
                plt.ylabel('tau (ms)')
                plt.tight_layout
                
        
     
         
        
    #to plot EPSC and IPSC
    EPSCnames = [i for i in list(ACCtraces.columns) if 'EPSC' in i]
    EPSCmean = ACCtraces[EPSCnames].mean(axis=1)
    IPSCnames = [i for i in list(ACCtraces.columns) if 'IPSC' in i]
    IPSCmean = ACCtraces[IPSCnames].mean(axis=1)
    plt.figure()
    plt.title('ACC, method='+str(method))
    plt.plot(ACCtraces[[i for i in IPSCnames if 'F1ACC' in i]][:2000],color='navajowhite')
    plt.plot(ACCtraces[[i for i in EPSCnames if 'F1ACC' in i]][:2000],color='lightgrey')
    plt.plot(IPSCmean[:2000],color='orange',label='Vcom = 0mV')
    plt.plot(EPSCmean[:2000],color='k',label='Vcom = -70mV')
    plt.legend()  
    plt.ylim(-200,700)
    
    EPSCnames = [i for i in list(AUDtraces.columns) if 'EPSC' in i]
    EPSCmean = AUDtraces[EPSCnames].mean(axis=1)
    IPSCnames = [i for i in list(AUDtraces.columns) if 'IPSC' in i]
    IPSCmean = AUDtraces[IPSCnames].mean(axis=1)
    plt.figure()
    plt.title('AUD, method='+str(method))
    plt.plot(AUDtraces[[i for i in IPSCnames if 'F2AUD' in i]][:2000],color='navajowhite')
    plt.plot(AUDtraces[[i for i in EPSCnames if 'F2AUD' in i]][:2000],color='lightgrey')
    plt.plot(IPSCmean[:2000],color='orange',label='Vcom = 0mV')
    plt.plot(EPSCmean[:2000],color='k',label='Vcom = -70mV')
    plt.legend()
    plt.ylim(-200,700)
    
    
    #to plot EPSP
    plt.figure()
    plt.title('ACC')
    plt.plot(EPSPtraces_ACC,color='lightblue')
    plt.plot(np.mean(EPSPtraces_ACC,axis=1),color='blue')

    plt.figure()
    plt.title('AUD')
    plt.plot(EPSPtraces_AUD,color='lightblue')
    plt.plot(np.mean(EPSPtraces_AUD,axis=1),color='blue')    

    

    #to plot latency between EPSC and IPSC
    latencydf_first['ms delay'] = abs(latencydf_first['IPSC'] - latencydf_first['EPSC'])/10
    latencydf_second['ms delay'] = abs(latencydf_second['IPSC'] - latencydf_second['EPSC'])/10

    plt.figure()
    plt.ylim(0, 5)
    plt.ylabel('EPSC to IPSC latency (ms)')
    names = ['ACC'] * len(latencydf_first['ms delay'])
    values = [latencydf_first['ms delay']]
    plt.scatter(names,values)
    names = ['AUD'] * len(latencydf_second['ms delay'])
    values = [latencydf_second['ms delay']]
    plt.scatter(names,values)
    
   

    


#for ACC, see if kinetics pass formalization
    allData_ACC['IPSC decay'] = decaydf['first fiber IPSC tau']
    allData_ACC['IPSC rise'] = risedf['first fiber IPSC tau']
    
    allData_ACC['EPSP start'] = (allData_ACC['EPSP start']/10) - 10
    allData_ACC['EPSP peak'] = (allData_ACC['EPSP peak']/10) - 10
    allData_ACC['IPSC start'] = (allData_ACC['IPSC start']/10) - 10
    allData_ACC['IPSC peak'] = (allData_ACC['IPSC peak']/10) - 10
    

    allData_ACC['IPSC delay from stim onset + IPSC rise tau'] = allData_ACC['IPSC start'] + allData_ACC['IPSC rise']
    allData_ACC['time IPSC peak from stim onset + IPSC decay tau'] = allData_ACC['IPSC peak'] + allData_ACC['IPSC decay']
    
    #condition 1: IPSC delay from stim onset + IPSC rise tau < EPSP peak time from stim?
    allData_ACC['condition 1'] = allData_ACC['IPSC delay from stim onset + IPSC rise tau'] <= allData_ACC['EPSP peak']
    #condition 2: EPSP peak time from stim < time IPSC peak from stim onset + IPSC decay tau?
    allData_ACC['condition 2'] = allData_ACC['time IPSC peak from stim onset + IPSC decay tau'] >= allData_ACC['EPSP peak']
    

    
#for AUD, see if kinetics pass formalization
    allData_AUD['IPSC decay'] = decaydf['second fiber IPSC tau']
    allData_AUD['IPSC rise'] = risedf['second fiber IPSC tau']
    
    allData_AUD['EPSP start'] = (allData_AUD['EPSP start']/10) - 10
    allData_AUD['EPSP peak'] = (allData_AUD['EPSP peak']/10) - 10
    allData_AUD['IPSC start'] = (allData_AUD['IPSC start']/10) - 10
    allData_AUD['IPSC peak'] = (allData_AUD['IPSC peak']/10) - 10


    allData_AUD['IPSC delay from stim onset + IPSC rise tau'] = allData_AUD['IPSC start'] + allData_AUD['IPSC rise']
    allData_AUD['time IPSC peak from stim onset + IPSC decay tau'] = allData_AUD['IPSC peak'] + allData_AUD['IPSC decay']
    
    #condition 1: IPSC delay from stim onset + IPSC rise tau < EPSP peak time from stim?
    allData_AUD['condition 1'] = allData_AUD['IPSC delay from stim onset + IPSC rise tau'] <= allData_AUD['EPSP peak']
    #condition 2: EPSP peak time from stim < time IPSC peak from stim onset + IPSC decay tau?
    allData_AUD['condition 2'] = allData_AUD['time IPSC peak from stim onset + IPSC decay tau'] >= allData_AUD['EPSP peak']

    plt.figure()
    for i in allData_AUD['IPSC delay from stim onset + IPSC rise tau']:
        names = ['IPSC delay from stim onset + IPSC rise tau']
        values = i
        plt.scatter(names,values,c='black',marker = 'x')
    for i in allData_AUD['time IPSC peak from stim onset + IPSC decay tau']:
        names = ['time IPSC peak from stim onset + IPSC decay tau']
        values = i
        plt.scatter(names,values,c='orange',marker = 'x')



#%%
def mahalanobis(pairedpeakMouseRatio, drug):
    
        
    import numpy as np
    from scipy.stats import chi2
    from matplotlib import patches
    import matplotlib.pyplot as plt
        
    
    for delay in [0,50]:
        df = pairedpeakMouseRatio[[str(delay)+'ms_sensory',str(delay)+'ms_drug sensory']]
        df = df.dropna()
        df = df.to_numpy()    
        
        # Covariance matrix
        covariance = np.cov(df , rowvar=False)
        
        # Covariance matrix power of -1
        covariance_pm1 = np.linalg.matrix_power(covariance, -1)
        
        # Center point
        centerpoint = np.mean(df , axis=0)  
        
        
        # Distances between center point and 
        distances = []
        for i, val in enumerate(df):
              p1 = val
              p2 = centerpoint
              distance = (p1-p2).T.dot(covariance_pm1).dot(p1-p2)
              distances.append(distance)
        distances = np.array(distances)
        
        
        # Cutoff (threshold) value from Chi-Sqaure Distribution for detecting outliers 
        cutoff = chi2.ppf(0.8, df.shape[1])
      
        # Index of outliers
        outlierIndexes = np.where(distances > cutoff )
        
        print('--- Index of Outliers ----')
        print(outlierIndexes)
        
            
        ## Finding ellipse dimensions  
        lambda_, v = np.linalg.eig(covariance)
        lambda_ = np.sqrt(lambda_)
        
        # Ellipse patch
        ellipse = patches.Ellipse(xy=(centerpoint[0], centerpoint[1]),
                          width=lambda_[0]*np.sqrt(cutoff)*2, height=lambda_[1]*np.sqrt(cutoff)*2,
                          angle=np.rad2deg(np.arccos(v[0, 0])), edgecolor='#fab1a0')
        ellipse.set_facecolor('#0984e3')
        ellipse.set_alpha(0.5)
        fig = plt.figure()
        ax = plt.subplot()
        ax.add_artist(ellipse)
        plt.scatter(df[: , 0], df[ : , 1])
        plt.title(str(delay)+'ms delay',fontsize=13)
        plt.xlabel('ctr',fontsize=13)
        plt.ylabel(drug,fontsize=13)
        plt.ylim(0,2.5)
        plt.xlim(0,2.5)
        plt.xticks([0,0.25,0.5,0.75,1.0,1.25,1.5,1.75,2,2.25,2.5],[0,None,0.5,None,1.0,None,1.5,None,2.0,None,2.5],fontsize=12)
        plt.yticks([0,0.25,0.5,0.75,1.0,1.25,1.5,1.75,2,2.25,2.5],[0,None,0.5,None,1.0,None,1.5,None,2.0,None,2.5],fontsize=12)
        plt.show()
            
    

    
#%%

def internalPTXvalidation():

    import tkinter
    import pickle
    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt

    import pandas
    
    
    from pathlib import Path
    
    ACCpeaks = pd.DataFrame(columns=['standard','PTX'])
    AUDpeaks = pd.DataFrame(columns=['standard','PTX'])
    plt.figure()   
    
    for internal in ['standard', 'PTX']:
    
        if internal == 'standard':
            savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\EPSC_IPSC")
        if internal == 'PTX':
            savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\EPSC_IPSC internal PTX")
    
        # makes a list with all folder names including cellType:
        import os
        allnames = os.listdir(savedLoc)
    
     
        allIPSC = {}
    
        #partitions data into EPSP, IPSC and EPSCs, and plot both for every cell
        for iCell in allnames:
            print('processing...'+str(iCell)) 
            # point at data file to view
            cellPath = savedLoc / iCell
            
            for file in os.listdir(cellPath):
                if 'baseLED' in file:
                    continue
                tkinter.Tk().withdraw()
                loadedData = pickle.load(open(cellPath / file, 'rb'))
                for k in loadedData.keys():
                    if '_data' in k:
                        if '_0' in file:      
                            allIPSC[file] = {}
                            allIPSC[file]['traceData'] = loadedData[k]
                            allIPSC[file]['stim1onset'] = int(float(loadedData['StimTime'][0]) * loadedData['SampleRateAcq'])
                            allIPSC[file]['stim2onset'] = int(float(loadedData['StimTime'][1]) * loadedData['SampleRateAcq'])
                
        
    
    
        
        
        for iCell in allIPSC.keys():
            BLfirstIPSC = allIPSC[iCell]['traceData'][allIPSC[iCell]['stim1onset']-100:allIPSC[iCell]['stim1onset']+4000]-np.mean(
                                        allIPSC[iCell]['traceData'][allIPSC[iCell]['stim1onset']-100:allIPSC[iCell]['stim1onset']+4000][0:100])
            BLsecondIPSC = allIPSC[iCell]['traceData'][allIPSC[iCell]['stim2onset']-100:allIPSC[iCell]['stim2onset']+4000]-np.mean(
                                        allIPSC[iCell]['traceData'][allIPSC[iCell]['stim2onset']-100:allIPSC[iCell]['stim2onset']+4000][0:100])
            if 'NA' not in iCell:    
                ACCpeaks.at[iCell,internal] = max(BLfirstIPSC)
                AUDpeaks.at[iCell,internal] = max(BLsecondIPSC)
            if 'NA' in iCell:
                omittedFiber = iCell[iCell.index('NA')-2:iCell.index('NA')]            
                if omittedFiber == 'F1':                   
                    AUDpeaks.at[iCell,internal] = max(BLsecondIPSC)
                if omittedFiber == 'F2':
                    ACCpeaks.at[iCell,internal] = max(BLfirstIPSC)    
                        
    
    
    for fiber in [ACCpeaks, AUDpeaks]:
        plt.figure()
        plt.ylim(-100,700)
        if fiber.equals(ACCpeaks):
            plt.title('ACC')
        if fiber.equals(AUDpeaks):
            plt.title('AUD')
        for internal in ['standard', 'PTX']:
            fiber['label'] = internal
            values = fiber[internal].to_numpy()[fiber[internal].to_numpy() != np.nan]
            names = fiber['label']
            plt.bar(internal,np.mean(values),alpha=0.5)
            plt.scatter(names, values,color='k')
            plt.scatter(internal,np.mean(fiber[internal]),color='orange')






#%%analyze fiber distributions
#this is if analyzing distributions as pairs - with images taken from same slice for ACC-AUD or AUD-VIS


    import numpy as np
    import pandas as pd
    from matplotlib import pyplot as plt
    from pathlib import Path
    from scipy import stats as st
    
    savedLoc = r"Z:\Danny R\imaging\fiber distribution.xlsx"
    ACCAUD_df_ACC = pd.read_excel(savedLoc, sheet_name = 'ACC-AUD_curated', header=0, skiprows=[1,2], usecols='C,F,I,L,O,R,U,X,AA')
    ACCAUD_df_AUD = pd.read_excel(savedLoc, sheet_name = 'ACC-AUD_curated', header=0, skiprows=[1,2], usecols='D,G,J,M,P,S,V,Y,AB')
    
    AUDVIS_df_VIS = pd.read_excel(savedLoc, sheet_name = 'AUD-VIS_curated', header=0, skiprows=[1,2], usecols='C,F,I,L,O,R,U')
    AUDVIS_df_AUD = pd.read_excel(savedLoc, sheet_name = 'AUD-VIS_curated', header=0, skiprows=[1,2], usecols='D,G,J,M,P,S,V')
    
    
    ACCAUD_df_ACC_stats = ACCAUD_df_ACC.copy()
    ACCAUD_df_AUD_stats = ACCAUD_df_AUD.copy()
    AUDVIS_df_VIS_stats = AUDVIS_df_VIS.copy()
    AUDVIS_df_AUD_stats = AUDVIS_df_AUD.copy()
    
    for iData, iData_stats in [(ACCAUD_df_ACC, ACCAUD_df_ACC_stats),
                               (ACCAUD_df_AUD, ACCAUD_df_AUD_stats),
                               (AUDVIS_df_VIS, AUDVIS_df_VIS_stats),
                               (AUDVIS_df_AUD, AUDVIS_df_AUD_stats)]:
        
        #if normalizing fluorescence between 0 and 1:
        for col in iData.columns:
            colmax = max(iData[col])
            colmin = min(iData[col])
            iData[col] = (iData[col] - colmin) / (colmax-colmin)
        
        
        for row in list(iData.index): 
            float_arr = iData.loc[row,:]
            mean = float_arr.mean()  
            se = st.sem(float_arr, nan_policy = 'omit')
            n = len(float_arr)
            CI = se * st.t.ppf((1 + 0.95) / 2., n-1)
            iData_stats.at[row,'mean'] = mean
            iData_stats.at[row,'se'] = se
            iData_stats.at[row,'CI'] = CI
       
        error = 'sem'
        
        if error =='sem':    
            iData_stats['upper bound'] = iData_stats['mean'] + iData_stats['se']
            iData_stats['lower bound'] = iData_stats['mean'] - iData_stats['se']
        
        if error =='95CI':    
            iData_stats['upper bound'] = iData_stats['mean'] + iData_stats['CI']
            iData_stats['lower bound'] = iData_stats['mean'] - iData_stats['CI']
        

    
    plt.figure()
    plt.title(error)
    x = list(ACCAUD_df_ACC.index * 0.62) 
    plt.fill_between(x, ACCAUD_df_ACC_stats['upper bound'], ACCAUD_df_ACC_stats['lower bound'],alpha=0.5,interpolate=True,color='palegreen')
    plt.plot(x,ACCAUD_df_ACC_stats['mean'],color='chartreuse',label='ACC fibers')
    plt.fill_between(x, ACCAUD_df_AUD_stats['upper bound'], ACCAUD_df_AUD_stats['lower bound'],alpha=0.5,interpolate=True,color='violet')
    plt.plot(x,ACCAUD_df_AUD_stats['mean'],color='fuchsia',label='AUD fibers')
    plt.ylim(0,1)
    plt.legend()

    plt.figure()
    plt.title(error)
    x = list(AUDVIS_df_VIS.index * 0.62)
    plt.fill_between(x, AUDVIS_df_VIS_stats['upper bound'], AUDVIS_df_VIS_stats['lower bound'],alpha=0.5,interpolate=True,color='palegreen')
    plt.plot(x,AUDVIS_df_VIS_stats['mean'],color='chartreuse',label='VIS fibers')
    plt.fill_between(x, AUDVIS_df_AUD_stats['upper bound'], AUDVIS_df_AUD_stats['lower bound'],alpha=0.5,interpolate=True,color='violet')
    plt.plot(x,AUDVIS_df_AUD_stats['mean'],color='fuchsia',label='AUD fibers')
    plt.ylim(0,1)
    plt.legend()

    
    plt.figure()

    df = ACCAUD_df_AUD.copy()
    plt.title('AUD')
    
    sorting = []
    for i in df.columns:
        x = i
        y = np.argmax(df[i])
        sorting.append((x,y))
    sorted_by_second = sorted(sorting, key=lambda tup: tup[1])
    newIndex = [i[0] for i in sorted_by_second]
    df = df[newIndex]
        
    plt.imshow(df, cmap ="plasma",aspect='auto')
    plt.colorbar()
      


#%%analyze fiber distributions
#this is if analyzing distributions as individual fibers, even though some data were collected in pairs (eg. ACC and AUD from the same slice)


    import numpy as np
    import pandas as pd
    from matplotlib import pyplot as plt
    from pathlib import Path
    from scipy import stats as st
    
    savedLoc = r"Z:\Danny R\imaging\fiber distribution.xlsx"
    ACCAUD_df_ACC = pd.read_excel(savedLoc, sheet_name = 'ACC-AUD_curated', header=0, skiprows=[1,2], usecols='C,F,I,L,O,R,U,X,AA')
    ACCAUD_df_AUD = pd.read_excel(savedLoc, sheet_name = 'ACC-AUD_curated', header=0, skiprows=[1,2], usecols='D,G,J,M,P,S,V,Y,AB')
    
    AUDVIS_df_VIS = pd.read_excel(savedLoc, sheet_name = 'AUD-VIS_curated', header=0, skiprows=[1,2], usecols='C,F,I,L,O,R,U')
    AUDVIS_df_AUD = pd.read_excel(savedLoc, sheet_name = 'AUD-VIS_curated', header=0, skiprows=[1,2], usecols='D,G,J,M,P,S,V')
    
    
    ACC_df = ACCAUD_df_ACC.copy()
    AUD_df = pd.concat([ACCAUD_df_AUD.copy(), AUDVIS_df_AUD.copy()],axis=1)
    VIS_df = AUDVIS_df_VIS.copy()
    
    ACC_df_stats = pd.DataFrame()
    AUD_df_stats = pd.DataFrame()
    VIS_df_stats = pd.DataFrame()
    
    for iData, iData_stats in [(ACC_df, ACC_df_stats),
                               (AUD_df, AUD_df_stats),
                               (VIS_df, VIS_df_stats)]:
        
        #if normalizing fluorescence between 0 and 1:
        for col in iData.columns:
            colmax = max(iData[col])
            colmin = min(iData[col])
            iData[col] = (iData[col] - colmin) / (colmax-colmin)
        
        
        for row in list(iData.index): 
            float_arr = iData.loc[row,:]
            mean = float_arr.mean()  
            se = st.sem(float_arr, nan_policy = 'omit')
            n = len(float_arr)
            CI = se * st.t.ppf((1 + 0.95) / 2., n-1)
            iData_stats.at[row,'mean'] = mean
            iData_stats.at[row,'se'] = se
            iData_stats.at[row,'CI'] = CI
       
        error = 'sem'
        
        if error =='sem':    
            iData_stats['upper bound'] = iData_stats['mean'] + iData_stats['se']
            iData_stats['lower bound'] = iData_stats['mean'] - iData_stats['se']
        
        if error =='95CI':    
            iData_stats['upper bound'] = iData_stats['mean'] + iData_stats['CI']
            iData_stats['lower bound'] = iData_stats['mean'] - iData_stats['CI']
        

    
        plt.figure()
        
        x = list(iData_stats.index * 0.62) 
        plt.fill_between(x, iData_stats['upper bound'], iData_stats['lower bound'],alpha=0.5,interpolate=True,color='palegreen')  
        plt.plot(x,iData_stats['mean'],color='chartreuse',label=error+' n='+str(len(iData.columns)))
        plt.ylim(0,1)
        plt.legend()
        if iData.equals(ACC_df):
            plt.title('ACC')
        if iData.equals(AUD_df):
            plt.title('AUD')
        if iData.equals(VIS_df):
            plt.title('VIS')

    #get the raw values
    ACC_superficial = sum(ACC_df_stats['mean'][0:242]) #equivalent to 0-150um (use "x" for conversion)
    ACC_intermediate = sum(ACC_df_stats['mean'][243:645]) #equivalent to 150-400um (use "x" for conversion)
    ACC_deep = sum(ACC_df_stats['mean'][646:1291]) #equivalent to 400-800um (use "x" for conversion)
   
    AUD_superficial = sum(AUD_df_stats['mean'][0:242]) #equivalent to 0-150um (use "x" for conversion)
    AUD_intermediate = sum(AUD_df_stats['mean'][243:645]) #equivalent to 150-400um (use "x" for conversion)
    AUD_deep = sum(AUD_df_stats['mean'][646:1291]) #equivalent to 400-800um (use "x" for conversion)
  
    VIS_superficial = sum(VIS_df_stats['mean'][0:242]) #equivalent to 0-150um (use "x" for conversion)
    VIS_intermediate = sum(VIS_df_stats['mean'][243:645]) #equivalent to 150-400um (use "x" for conversion)
    VIS_deep = sum(VIS_df_stats['mean'][646:1291]) #equivalent to 400-800um (use "x" for conversion)      


    #make as ratio of all fibers in layer
    superficial_total = ACC_superficial + AUD_superficial + VIS_superficial
    ACC_superficial_ratio = ACC_superficial / superficial_total
    AUD_superficial_ratio = AUD_superficial / superficial_total
    VIS_superficial_ratio = VIS_superficial / superficial_total
    
    intermediate_total = ACC_intermediate + AUD_intermediate + VIS_intermediate
    ACC_intermediate_ratio = ACC_intermediate / intermediate_total
    AUD_intermediate_ratio = AUD_intermediate / intermediate_total
    VIS_intermediate_ratio = VIS_intermediate / intermediate_total    
    
    deep_total = ACC_deep + AUD_deep + VIS_deep
    ACC_deep_ratio = ACC_deep / deep_total
    AUD_deep_ratio = AUD_deep / deep_total
    VIS_deep_ratio = VIS_deep / deep_total    
    
    
    #organize all ratio data per layer
    ACCvalues = [ACC_superficial_ratio, ACC_intermediate_ratio, ACC_deep_ratio]
    AUDvalues = [AUD_superficial_ratio, AUD_intermediate_ratio, AUD_deep_ratio]
    VISvalues = [VIS_superficial_ratio, VIS_intermediate_ratio, VIS_deep_ratio]
    
    #plot
    plt.figure()
    labels = ['superficial','intermediate','deep']
    plt.bar(labels, ACCvalues, width = 0.8, label = 'ACC')
    
    bottom = ACCvalues
    plt.bar(labels, AUDvalues, width = 0.8, label = 'AUD',bottom=bottom)
    
    bottom = [0,0,0]
    for e, i in enumerate(ACCvalues):
        bottom[e] = i +AUDvalues[e]
    plt.bar(labels, VISvalues, width = 0.8, label = 'VIS',bottom=bottom)
    plt.legend()
    
    

#%%

def compareNMDAdecay():
    
    import tkinter
    from tkinter.filedialog import askopenfilename
    import pickle
    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt
    from scipy import signal
    import pandas
    
    import DR_tau_functions as gt
    
    from pathlib import Path


    savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\AMPA_NMDA")
    

    # makes a list with all folder names including cellType:
    import os
    
    decaydf_IB = pd.DataFrame(columns=['first fiber NMDA tau','second fiber NMDA tau'])
    decaydf_RS = pd.DataFrame(columns=['first fiber NMDA tau','second fiber NMDA tau'])
        
    for cellType, decaydf in [('pIB', decaydf_IB),
                              ('pRS', decaydf_RS)]:
        
        allnames = [i for i in os.listdir(savedLoc) if cellType in i]
    
    
        allAMPA = {}
        allNMDA = {}
    
        
        #partitions data into EPSP, IPSC and EPSCs, and plot both for every cell
        for iCell in allnames:
            print('processing...'+str(iCell)) 
            # point at data file to view
            cellPath = savedLoc / iCell
            plt.figure()
            plt.title(iCell)
            plt.ylabel('pA')
            plt.xlabel('100 points = 10ms')
            for file in os.listdir(cellPath): 
                tkinter.Tk().withdraw()
                loadedData = pickle.load(open(cellPath / file, 'rb'))
                for k in loadedData.keys():
                    if 'baseLED' not in file:
                        if '_data' in k:
                            plt.plot(loadedData[k])
                            if '_70' in file:      
                                allAMPA[file] = {}
                                allAMPA[file]['traceData'] = loadedData[k]
                                allAMPA[file]['stim1onset'] = int(float(loadedData['StimTime'][0]) * loadedData['SampleRateAcq'])
                                allAMPA[file]['stim2onset'] = int(float(loadedData['StimTime'][1]) * loadedData['SampleRateAcq'])
                            elif '_40' in file:
                                allNMDA[file] = {}
                                allNMDA[file]['traceData'] = loadedData[k]
                                allNMDA[file]['stim1onset'] = int(float(loadedData['StimTime'][0]) * loadedData['SampleRateAcq'])
                                allNMDA[file]['stim2onset'] = int(float(loadedData['StimTime'][1]) * loadedData['SampleRateAcq'])
                

        ACCtraces = pd.DataFrame()
        AUDtraces = pd.DataFrame() 
        
       
        for iCell in allNMDA.keys():
    
            BLfirstNMDA = allNMDA[iCell]['traceData'][allNMDA[iCell]['stim1onset']-100:allNMDA[iCell]['stim1onset']+4000]-np.mean(
                                    allNMDA[iCell]['traceData'][allNMDA[iCell]['stim1onset']-100:allNMDA[iCell]['stim1onset']+4000][0:100])
            BLsecondNMDA = allNMDA[iCell]['traceData'][allNMDA[iCell]['stim2onset']-100:allNMDA[iCell]['stim2onset']+4000]-np.mean(
                                    allNMDA[iCell]['traceData'][allNMDA[iCell]['stim2onset']-100:allNMDA[iCell]['stim2onset']+4000][0:100])
            threshold = 0.05
            firstNMDAstart = gt.getNMDAstart(BLfirstNMDA, threshold)
            secondNMDAstart = gt.getNMDAstart(BLsecondNMDA, threshold)
            
            
                    
         
            if 'NA' not in iCell:    
                ACCtraces[iCell+'_NMDA'] = BLfirstNMDA
                AUDtraces[iCell+'_NMDA'] = BLsecondNMDA
                
                
                
                #get decay tau for fiber 1
                tau = gt.getNMDAdecay(BLfirstNMDA)
                decaydf.at[iCell[:iCell.index('_F1')],'first fiber NMDA tau'] = tau
                
                #get decay tau for fiber 2
                tau = gt.getNMDAdecay(BLsecondNMDA)
                decaydf.at[iCell[:iCell.index('_F1')],'second fiber NMDA tau'] = tau
                
                
                
            #handling case when one or another fiber isn't being used
            if 'NA' in iCell:
                omittedFiber = iCell[iCell.index('NA')-2:iCell.index('NA')]
                
                if omittedFiber == 'F1':
    
                    
                    AUDtraces[iCell+'_NMDA'] = BLsecondNMDA
                    
                    #get decay tau for fiber 2
                    tau = gt.getNMDAdecay(BLsecondNMDA)
                    decaydf.at[iCell[:iCell.index('_F1')],'second fiber NMDA tau'] = tau
                    
                        
                if omittedFiber == 'F2':       
    
                    
                    ACCtraces[iCell+'_NMDA'] = BLfirstNMDA
                    
                    #get decay tau for fiber 1                
                    tau = gt.getNMDAdecay(BLfirstNMDA)
                    decaydf.at[iCell[:iCell.index('_F1')],'first fiber NMDA tau'] = tau
            

    for fiber in ['first', 'second']:
        fig = plt.figure()
        # fig.set_size_inches(3,5)   
        
        
        # plt.ylim(0,100)
        if fiber == 'first':
            plt.title('ACC NMDA decay')
        if fiber == 'second':
            plt.title('AUD NMDA decay')        

        for cellType, decaydf in [('pIB', decaydf_IB),
                              ('pRS', decaydf_RS)]:     
            names = [cellType] * len(decaydf)
            values = [i for i in decaydf[fiber+' fiber NMDA tau']]   
            plt.scatter(names, values, color = 'k', facecolors='none')
            
            # names = ['pRS'] * len(decaydf)
            # values = [i for i in decaydf[fiber+' fiber NMDA tau']]   
            # plt.scatter(names, values, color = 'k')
            
        plt.ylabel('tau (ms)')
        plt.tight_layout




    
#%%

def plotNMDAtrace(fiberTypes, cellType, IPSC, opsinSwapList, confidence, oneMapCells, error, order, show, imageloc, redblue, opsinConfig, delayBase):
    
    
   import tkinter
   from tkinter.filedialog import askopenfilename
   import pickle
   from pathlib import Path

    
   savedLoc = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\AMPA_NMDA")
   
   from matplotlib import pyplot as plt
   plt.figure('ACC')
   plt.figure('AUD')
   
   for cellType in ['pIB','pRS']:
       
        
        # make a list with all folder names including cellType:
        import os
        allnames = os.listdir(savedLoc)
        selectednames = [x for x in allnames if cellType in x]
        
        
        import pandas as pd
        import numpy as np
        
        all40data_ACC = pd.DataFrame()
        all70data_ACC = pd.DataFrame()
        all40data_AUD = pd.DataFrame()
        all70data_AUD = pd.DataFrame()
        
        for i in selectednames:
            
         
            print('processing...'+str(i)) 
            # point at data file to view
            cellPath = savedLoc / i
            workspacedf = pd.DataFrame()
            
    
            for file in os.listdir(cellPath):      
                if '_70' in file:
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    stim1start = int(float(loadedData['StimTime'][0]) * loadedData['SampleRateAcq'])
                    stim2start = int(float(loadedData['StimTime'][1]) * loadedData['SampleRateAcq'])
                    for k in loadedData.keys():
                        if '_data' in k:
                            if 'F1NA' not in file:
                                all70data_ACC[i] = loadedData[k][stim1start-1000:stim1start+5000]   
                            if 'F2NA' not in file:
                                all70data_AUD[i] = loadedData[k][stim2start-1000:stim2start+5000] 
                if '_40' in file:
                    tkinter.Tk().withdraw()
                    loadedData = pickle.load(open(cellPath / file, 'rb'))
                    stim1start = int(float(loadedData['StimTime'][0]) * loadedData['SampleRateAcq'])
                    stim2start = int(float(loadedData['StimTime'][1]) * loadedData['SampleRateAcq'])
                    for k in loadedData.keys():
                        if '_data' in k:
                            if 'F1NA' not in file:
                                all40data_ACC[i] = loadedData[k][stim1start-1000:stim1start+5000]
                            if 'F2NA' not in file:
                                all40data_AUD[i] = loadedData[k][stim2start-1000:stim2start+5000]           
                            
         
            
        for icol in all40data_ACC.columns:
            all40data_ACC[icol] = all40data_ACC[icol] - np.mean(all40data_ACC[icol][800:1000])
            all40data_ACC[icol] = all40data_ACC[icol] / max(all40data_ACC[icol][1000:1500])
            
        for icol in all40data_AUD.columns:
           all40data_AUD[icol] = all40data_AUD[icol] - np.mean(all40data_AUD[icol][800:1000])
           all40data_AUD[icol] = all40data_AUD[icol] / max(all40data_AUD[icol][1000:1500])
            
    
        #get CI stats
        CIstats = pd.DataFrame(index=['95% CI','sem','mean','upper bound','lower bound'])
        
        from matplotlib import pyplot as plt
        import numpy as np
        import scipy.stats
        
        
        for fiberData in [all40data_ACC, all40data_AUD]:     
           
            
          
            ggg = fiberData.transpose()
            
            for col in list(ggg.columns): 
                a = ggg[col].values
                float_arr = np.vstack(a[:]).astype(np.float)
                n = len(float_arr)
                m = ggg[col].mean()
                se = scipy.stats.sem(float_arr, nan_policy = 'omit')
                h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
                #h = np.nanstd(float_arr) for standard dev
                CIstats.at['95% CI',col]= h
                CIstats.at['sem',col] = se
                CIstats.at['mean',col]= m
                if error == '95CI':
                    CIstats.at['upper bound',col]= m + h     
                    CIstats.at['lower bound',col]= m - h  
                if error == 'sem':
                    CIstats.at['upper bound',col]= m + se     
                    CIstats.at['lower bound',col]= m - se  
                if error == 'std':    
                    print("'haven't done that yet")
                    
            from matplotlib import pyplot as plt
            
            
            x = CIstats.transpose()
            
            if cellType == 'pIB':
                plotColor = 'crimson'
            if cellType == 'pRS':
                plotColor = 'blue'    
     
            if fiberData.equals(all40data_ACC):
                plt.title('ACC')
                plt.figure('ACC')
                            
            if fiberData.equals(all40data_AUD):
                plt.title('AUD')
                plt.figure('AUD')
        
            plt.plot(x['mean'],plotColor)
            yerrUpper = np.asarray(x['upper bound'])
            yerrLower = np.asarray(x['lower bound'])
            flat_yerrUpper = yerrUpper.flatten()
            flat_yerrLower = yerrLower.flatten()
            
            plt.fill_between(x.index,flat_yerrUpper, flat_yerrLower,alpha=0.3,interpolate=True, linewidth = 0 ,color = plotColor,label=cellType)
    

            plt.legend()
            plt.show()
                

        
   return
    
    
#%%
def getAnimalNumbers(opsinSwapList):
    
    import tkinter
    from tkinter.filedialog import askdirectory
    tkinter.Tk().withdraw()
    dataloc =  r"Z:\Danny R\Slice Phys\Preprocessed data"
    dirPath = askdirectory(initialdir = dataloc)
    
    from pathlib import Path
    savedLoc = Path(dirPath)
    
    
    #if care about default opsin or not, 'yes'; otherwise, 'no'
    swapCare = 'no'
    
    
    import os
    # make a list with all folder names including cellType:
    allnames = os.listdir(savedLoc)
    if swapCare == 'yes':
        defaultnames = [x for x in allnames if x not in opsinSwapList]
        opsinswapnames = [x for x in allnames if x in opsinSwapList]
    else:
        defaultnames = allnames.copy()
        opsinswapnames = []
    
    
    cellnames_IB = [x for x in defaultnames if 'IB' in x]
    cellnames_RS = [x for x in defaultnames if 'RS' in x]
    
    cellNumber_all = len(allnames)
    cellNumber_IB = len(cellnames_IB)
    cellNumber_RS = len(cellnames_RS)
    
    def findnth(haystack, needle, n):
        parts= haystack.split(needle, n+1)
        if len(parts)<=n+1:
            return -1
        return len(haystack)-len(parts[-1])-len(needle)
        
    
    strippedID_all = []
    for i in allnames:
        cutspot = findnth(i,'_',2)
        if i[:cutspot] not in strippedID_all:
            strippedID_all.append(i[:cutspot])
    mouseNumber_all = len(strippedID_all)
    
    
    strippedID_IB = []
    for i in cellnames_IB:
        cutspot = findnth(i,'_',2)
        if i[:cutspot] not in strippedID_IB:
            strippedID_IB.append(i[:cutspot])
    mouseNumber_IB = len(strippedID_IB)
    
    strippedID_RS = []
    for i in cellnames_RS:
        cutspot = findnth(i,'_',2)
        if i[:cutspot] not in strippedID_RS:
            strippedID_RS.append(i[:cutspot])
    mouseNumber_RS = len(strippedID_RS)   
    
    
    print('all cells = '+str(cellNumber_all))
    print('all mice = '+str(mouseNumber_all))
    print('IB cells = ' + str(cellNumber_IB))
    print('IB mice = ' + str(mouseNumber_IB))
    print('RS cells = ' + str(cellNumber_RS))
    print('RS mice = ' + str(mouseNumber_RS))
    
    
    
    return


#%%
def retrogradeCellTypes():

    from matplotlib import pyplot as plt
    
    from pathlib import Path


    path_dStr = Path(r"Z:\Danny R\Slice Phys\Preprocessed data\current steps\-70\retrograde labelled\retro dStr")
    path_pons =  Path(r"Z:\Danny R\Slice Phys\Preprocessed data\current steps\-70\retrograde labelled\retro pons")
    
    
    import os
    # make a list with all folder names including cellType:
    allnames_dStr = os.listdir(path_dStr)
    allnames_pons = os.listdir(path_pons)

    
    dStr_IBcount = len([i for i in allnames_dStr if 'IB' in i])
    dStr_RScount = len([i for i in allnames_dStr if 'RS' in i])
    
    pons_IBcount = len([i for i in allnames_pons if 'IB' in i])
    pons_RScount = len([i for i in allnames_pons if 'RS' in i])
    
    plt.figure()
    plt.pie((dStr_IBcount,dStr_RScount),labels=('IB ('+str(dStr_IBcount)+')','RS ('+str(dStr_RScount)+')'))
    plt.legend()
    plt.title('dStr-projecting, n = '+str(len(allnames_dStr)))
    
    plt.figure()
    plt.pie((pons_IBcount,pons_RScount),labels=('IB ('+str(pons_IBcount)+')','RS ('+str(pons_RScount)+')'))
    plt.legend()
    plt.title('pons-projecting, n = '+str(len(allnames_pons)))    
    
    
    
    
    
    
    
    
    
    