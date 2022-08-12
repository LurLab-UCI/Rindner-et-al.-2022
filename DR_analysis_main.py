# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 19:14:07 2019

@author: Daniel Rindner

"""
#%% add folder to path, import modules
import sys
sys.path.append(r"Z:\Danny R\code\DR_scripts");

import tkinter
from tkinter.filedialog import askopenfilename
import pickle

import DR_analysis_functions as af

#%% make list of experiments where opsins swapped

opsinSwapList, oneMapCells =  af.opsinSwapList()

#%% set delays

delay1 = 0
delay2 = 50
delay3 = 100
delay4 = 250

#%% Show individual traces with arithmetic sum and recorded

fiberTypes = [None, None]       #either 'ACC', 'A1', or 'V1'  

confidence = 0.95   #confidence interval

cell = None     #name of cell

order = None     #either 'FS' (for frontal-sensory) or 'SF' (for sensory-frontal)

af.singleCellTrace(cell, fiberTypes, delay1, delay2, delay3, delay4, opsinSwapList, oneMapCells, order)

#%% get multimodal synapse dynamics

#ask if RS or IB
fiberTypes = [None, None]       #either 'ACC', 'A1', or 'V1'  
cellType = None     #either 'IB' or 'RS'

#save individual cell graphs? no = 0, save = 1
show = 0
imageloc =  r"Z:\Danny R\Slice Phys\image dump"

pairedpeakRatio = af.mousemixedPulseAnalysis(fiberTypes, cellType, delay1, delay2, delay3, delay4, opsinSwapList, imageloc, show, oneMapCells, quality)

#%% plot figure for Vrest current steps

Vm = '70'

#add which traces to plot var
firstTrace = 2
step = 3
plotMin = -130
plotMax = 50
plotStart = 700
plotStop = 7000
imageloc = r"Z:\Danny R\Slice Phys\image dump"

af.plotISteps(plotMin,plotMax,plotStart,plotStop,imageloc,step,firstTrace,Vm)

#%% plotting subthreshold multimodal 95% confidence bands

#ask if RS or IB
fiberTypes = [None, None]       #either 'ACC', 'A1', or 'V1'  
cellType = None     #either 'IB' or 'RS'

confidence = 0.95   #confidence interval

quality = 'EPSP'            #either 'EPSP' or 'IPSC'

complete = 0        # either 0 (no) or 1 (yes) where only complete (all 4 delays) mice are included

average = 'mouse'   #either mouse or cell
plots = 'yes' 
show = 0
imageloc = r"Z:\Danny R\Slice Phys\image dump"

opsinSwapRatios, nonSwapRatios = af.plotmouseCI(fiberTypes, cellType, delay1, delay2, delay3, delay4, opsinSwapList, confidence, oneMapCells, quality, show, imageloc, complete, average, plots)

#%% do IPSC analysis
   
#ask if RS or IB
fiberTypes = [None, None]       #either 'ACC', 'A1', or 'V1'  
cellType = None     #either 'IB' or 'RS'

confidence = 0.95   #confidence interval
complete = 0        # either 0 (no) or 1 (yes) where only complete (all 4 delays) mice are included
show = 0            # either 0 (no) or 1 (yes)
imageloc = r"Z:\Danny R\Slice Phys\image dump" 

method = 'mixed pulse'   #either 'mixed pulse' which compares second peak to equivalent single or 'paired pulse' which compares second peak to first peak
    
#assumes no opsin swap mice included in IPSC analyses
opsinSwapRatios, nonSwapRatios  = af.IPSCpeakanalysis(fiberTypes, cellType, delay1, delay2, delay3, delay4, opsinSwapList, confidence, oneMapCells, show, imageloc, complete, method)

#%% calculate suprathreshold multimodal CIs


#ask if RS or IB, fiber type default A1, ACC
cellType = None     #either 'IB' or 'RS'

replacePolicy = [0]

addition = 'on'
averaging = 'cell'    #mouse or cell
point = 'global'    #this is where the GABA measurement is made - either '0' or '50' or '100' or 'global'

thresholdLower = 0.25
thresholdUpper = 0.75               

#raster assumes no opsin swap
rasterData = af.raster(cellType, delay1, delay2, delay3, delay4, replacePolicy, addition, thresholdLower, thresholdUpper, averaging, point)

#%% make graph of non-spiking suprathreshold GABA

#ask if RS or IB, fiber type default A1, ACC
cellType = None     #either 'IB' or 'RS'

baseline = 0        #either 0 (no) or 1 (yes)

#raster assumes no opsin swap
af.supraGABA(cellType, delay1, delay2, delay3, delay4, baseline)

#%% plot trace 

#ask if RS or IB
fiberTypes = [None, None]       #either 'ACC', 'A1', or 'V1'  
cellType = None     #either 'IB' or 'RS'

IPSC = 0    #either 1 if plotting IPSCs or 0 if not
confidence = 0.95   #confidence interval
error = '95CI'     #either 'sem' or '95CI' or 'std' OR IF 'pop' THEN ALL DATA IS PLOTTED  (only works if redblue is False)
opsinConfig = 'default'       #either 'default' or 'swap' or 'both'
delayBase = 'delay'         #either 'delay' or 'first pulse', decides whether the plots are baselined to first pulse or to just before each second pulse
order = 'FS'      #either 'FS' or 'SF' or 'both'
redblue = True     #true or false, decides whether you plot just red and blue single traces or all delays
show = 0        #save  graphs? no = 0, save = 1
imageloc =  r"Z:\Danny R\Slice Phys\image dump"

af.plottrace(fiberTypes, cellType, IPSC, delay1, delay2, delay3, delay4, opsinSwapList, confidence, oneMapCells, error, order, show, imageloc, redblue, opsinConfig, delayBase)

#%%plot all single input trace average with model

error = 'pop'     #either 'pop' for all, 'std', sem', '95CI' or 'maxmin' for highest and lowest
cellType = 'IB'
opsinConfig = 'default'       #either 'default' or 'swap' or 'both'


#adjusts for synaptic delay differences between recorded and model
ACC_data, A1_data, V1_data = af.plottrace2(cellType, opsinSwapList, opsinConfig, error)

#%% get mechanism and tau

#ask if RS or IB
fiberTypes = [None, None]       #either 'ACC', 'A1', or 'V1'  
cellType = None     #either 'IB' or 'RS'
confidence = 0.95   #confidence interval

drug = 'PTX'   #either 'AP5' or 'mib' or "TTX" or "PTX" or "time" or "PTX internal" or "QX314 internal"
order = 'FS'    #either 'FS' (for frontal-sensory) or 'SF' (for sensory-frontal)
tau = 0     #don't show = 0 , show = 1, shows whichever is first in order "SF" means shows "S", only from coincident
averaging = 'cell'      #either 'cell' or 'mouse'

#save  graphs? no = 0, save = 1
show = 0
imageloc = r"C:\Users\Jay\Desktop\test"
plots = 'yes'


if 'internal' not in drug:
    pairedpeakMouseRatio = af.intMechanism(fiberTypes, confidence, cellType, opsinSwapList, oneMapCells, drug, imageloc, show, order, tau, averaging, plots)
if 'internal' in drug:
    pairedpeakMouseRatio = af.intMechanismInternal(confidence, cellType, opsinSwapList, oneMapCells, drug, imageloc, show, order, tau, averaging, plots)

#%% test mechanism experiments for outliers using mahalanobis method (assumes you've run above cell)

af.mahalanobis(pairedpeakMouseRatio, drug)

#%% plot GABAa effect on EPSPs from -60mV

#does both cell types IB and RS at once

confidence = 0.95

#save  graphs? no = 0, save = 1
show = 0
imageloc = r"C:\Users\Jay\Desktop\test"

difPeak, difTime = af.GABAonEPSP(opsinSwapList, imageloc, confidence, show)

#%% correlate coincident MEI with GABAa effect on EPSPs from -60
# this code requires that you run the module above it (GABAonEPSP)

averaging = 'cell'      #either 'mouse' or by 'cell'

af.GABAtoMEIcorrelation(opsinSwapList, averaging, difPeak)

#%% get cell type metrics

intFunmouseAdd.plot3DcellMetrics()

#%% compare EPSP decay time constants across opsins

confidence = 0.95
showOpsinAvg = 1        #either 0 (no) or 1 (yes)
showHist = 0
showBar = 1

chr2_stats, chrimson_stats, chr2Tau, chrimsonTau, cellTypeTau = af.getEPSPDecayConstants(opsinSwapList, confidence, celltoRemove, showOpsinAvg, showHist, showBar)

#%% compare EPSP decay time constants across cell types

burstingRiseDF, regularRiseDF, burstingDecayDF, regularDecayDF = af.celltypeDecay(method)

#%% compare EPSP rise time constants across opsins

confidence = 0.95

showHist = 0    #either 0 (no) or 1 (yes)
showBar = 1

chr2Rise, chrimsonRise, cellTypeTau = af.getEPSPRiseConstants(opsinSwapList, confidence, celltoRemove, showHist, showBar)

#%%  get IPSC rise and decay time constants

ACCevokedIPSCtaudf, AUDevokedIPSCtaudf = af.getIPSCConstants()

#%% compare EPSP latency between opsins or just look at all latencies for TTX where showed recovery

chr2Latency, chrimsonLatency = intFunmouseAdd.getLatency(opsinSwapList)
af.compareLatency(chr2Latency, chrimsonLatency)
af.compareTTXLatency(chr2Latency, chrimsonLatency)

#%% analyze TTX experiments

fiberTypes = [None, None]       #either 'ACC', 'A1', or 'V1'  
cellType = None     #either 'IB' or 'RS'
legend = 0      #either 0 or 1, if 0 then no, if 1 then yes
failed = False   #either True or False, if True then looking at cells that we judged as not recovering, if False then looking at cells we judged as recovering

resultsTTX = af.getTTX(fiberTypes, cellType, failed, legend)

#%% show pie charts of PPC populations

#dual means recieves monosynaptic dual input
#'single means number of cells that didn't recieve dual monosynaptic input (either only one is mono and one is di, or didn't recieve both)

af.ppcPie(opsinSwapList)
af.cellPie()
allRise, allCounts = af.cellTypeMonoPie(opsinSwapList)

#%% determine confidence interval of all MEI for all experiments

complete = 0        # either 0 (no) or 1 (yes) where only complete (all 4 delays) mice are included
average = 'cell'   #either mouse or cell
fiberTypes = [None, None]       #either 'ACC', 'A1', or 'V1'  

confidence = 0.99

order = 'FS'
tau = 0 #don't show = 0 , show = 1, shows whichever is first in order "SF" means shows "S", only from coincident
quality = 'EPSP

#save graphs?
show = 0    #no = 0, save = 1
imageloc = r"Z:\Danny R\Slice Phys\image dump"

plots = 'no' #either no or yes, for just pulling MPRs, no need to plot

bounds = af.getallCI(fiberTypes, delay1, delay2, delay3, delay4, opsinSwapList, confidence, oneMapCells, quality, show, imageloc, complete, average, plots)

#%% plotting traces

fiberTypes = [None, None]       #either 'ACC', 'A1', or 'V1'  
cellType = None     #either 'IB' or 'RS'

af.plotTraces(cellType, FiberTypes)                       

#%% for extracting mouse and cell numbers for each experiment

af.getAnimalNumbers(opsinSwapList)
