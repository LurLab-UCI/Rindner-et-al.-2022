# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 19:14:07 2019

@author: Daniel Rindner

"""
#%% add folder to path, import modules
import sys
sys.path.append(r"Z:\Danny R\code\DR_scripts");

from pathlib import Path

import DR_preprocessing_functions as phys

import tkinter
from tkinter.filedialog import askopenfilename
import pickle

#%% load data

dataLoc = r"Z:\Danny R\Slice Phys\Raw data"
exp = phys.loadExpData(dataLoc)

#%% show individual sessions with original sweep legend

experiment = exp
session = 1

baseline = 1  #0 or 1 
BLstart = (990)      #baseline window
BLstop = (999)

phys.showSession(experiment, session, baseline, BLstart, BLstop)

#%% pickle current steps 

experiment = exp
session = None     #write session number (e.g. 3)
badTraces = [] #write sweep number here, separated by comma                                         
saveloc= r"Z:\Danny R\Slice Phys\Preprocessed data\current steps"

date = None  #write date (e.g. 191203)
genotype = None     #write genotype (e.g. wt, wtai)
mouseID = None      #write mouse ID (e.g. 128)
cellID = None     #write cell number (e.g. 3)

Vm = 'Vrest'      #either 'Vrest' or '70'

fig = 0         #add image? 0 for no, 1 for yes, figure is not baselined
plotMin = -130
plotMax = 50
plotStart = 700
plotStop = 7000
imageloc = r"C:\Users\Lur Lab 3\Desktop\imagedump"

phys.saveISteps(experiment, session, badTraces, saveloc, date, genotype, mouseID, cellID, imageloc, fig, plotMin, plotMax, plotStart, plotStop, Vm)
        
#%% pickle integration

experiment = exp
session = 5
badTraces = [] #write sweep number here, separated by comma                                         
BLstart = (900)  # baseline window for wavedump 900 - 990, None for GABA
BLstop = (990)
saveloc = r"C:\Users\Lur Lab 3\Desktop\wavedump"

save = 'average' # for subthreshold, usually use average - for suprathreshold need to save all traces so do all

date = None  #write date (e.g. 191203)
genotype = None     #write genotype (e.g. wt, wtai)
mouseID = None      #write mouse ID (e.g. 128)
cellID = None     #write cell number (e.g. 3)
delay = None        #write delay (e.g. 0,50,100,250) or 0000 for GABA single pulse data (and BL None)


fig = 0         #add image? 0 for no, 1 for yes, figure is not baselined
plotMin = -84
plotMax = plotMin + 20
plotStart = 750
plotStop = 5500
imageloc = r"Z:\Danny R\Slice Phys\image dump"

#only use if old data that used maps
color =  'blue'       #either blue or bluered or red or redblue, otherwise None
equivalentName = 'paired pulse map'   #either pulse 1 map, paired pulse map, pulse 2 map, paired pulse map_swap, otherwise None

if save == 'average':
    phys.saveSessionAvr(experiment, session, badTraces, saveloc, date, genotype, mouseID, cellID, delay, imageloc, fig, plotMin, plotMax, plotStart, plotStop, color, equivalentName, BLstart, BLstop)
elif save == 'all':
    phys.saveSessionAll(experiment, session, badTraces, saveloc, date, genotype, mouseID, cellID, delay, imageloc, fig, plotMin, plotMax, plotStart, plotStop, color, equivalentName)


#%% pickle TTX

experiment = exp
session = 2
badTraces = [] # write sweep number here, separated by comma                                         
BLstart = (None)  # baseline window for wavedump
BLstop = (None)
saveloc = r"C:\Users\Lur Lab 3\Desktop\wavedump"

date = None  #write date (e.g. 191203)
genotype = None     #write genotype (e.g. wt, wtai)
mouseID = None      #write mouse ID (e.g. 128)
cellID = None     #write cell number (e.g. 3)
drug = None    #write status (pre, TTX, 4AP, GLU or pre, AP5, NBQX) or if pickling EPSC and IPSC traces use '70' or '0' or '40' or 'baseLED' if looking for EPSP kinetics on EPSC/IPSC experiments

fiber1 = 'ACC'
fiber2 = 'AUD'

phys.saveTTX(experiment, session, badTraces, saveloc, date, genotype, mouseID, cellID, fiber1, fiber2, drug, BLstart, BLstop)


#%% Open pkl file

saveloc = r"Z:\Danny R\Slice Phys\Preprocessed data"

tkinter.Tk().withdraw()
filePath = askopenfilename(initialdir = saveloc)   # point at data file to view
loadedData = pickle.load(open(filePath, 'rb'))
