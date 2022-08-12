# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 10:40:05 2022

@author: Lur Lab 3
"""
#%%
def getIPSCstart(trace, threshold):
    import numpy as np
    set1 = np.asarray(trace[:3000])
    set2 = np.asarray(trace[5:3005])
    derv = (set2 - set1)/5                     
    # thresh = 2
    r = np.arange(len(derv))[100:200]
    
    for index in r:
        if derv[index] < threshold :
            continue
        if derv[index] >= threshold:
            startIPSC = index
            break
        
    return startIPSC


#%%
def getEPSCstart(trace, threshold):
    import numpy as np
    set1 = np.asarray(trace[:3000])
    set2 = np.asarray(trace[5:3005])
    derv = (set2 - set1)/5                     
    # thresh = 2
    r = np.arange(len(derv))[100:200]

    for index in r:
        if derv[index] > -threshold:
            continue
        if derv[index] <= -threshold:
            startEPSC = index
            break
    return startEPSC

#%%
def getIPSCrise(trace, startIPSC):
    import numpy as np
    peakLoc = np.argmax(trace[:300])
    rise = trace[peakLoc]*0.632
    for idx, i in enumerate(trace[:peakLoc]):
        if i-rise < 0:
            continue
        elif i-rise >= 0:
            break
        
    # set1 = np.asarray(trace[:3000])
    # set2 = np.asarray(trace[5:3005])
    # derv = (set2 - set1)/5                     
    # # thresh = 2
    # r = np.arange(len(derv))
    
    # for index in r:
    #     if derv[index] < threshold :
    #         continue
    #     if derv[index] >= threshold:
    #         startIPSC = index
    #         break
    tau = (idx - startIPSC) / 10
    # tau = ((idx - startIPSC) / (peakLoc - startIPSC))
    
    return tau

#%%
def getEPSCrise(trace, startEPSC):
    import numpy as np
    peakLoc = np.argmin(trace[:300])
    rise = trace[peakLoc]*0.632
    for idx, i in enumerate(trace[:peakLoc]):
            if i-rise > 0:
                continue
            elif i-rise <= 0:
                break
            
    # set1 = np.asarray(trace[:3000])
    # set2 = np.asarray(trace[5:3005])
    # derv = (set2 - set1)/5                     
    # # thresh = -2
    # r = np.arange(len(derv))
    # for index in r:
    #     if derv[index] > -threshold:
    #         continue
    #     if derv[index] <= -threshold:
    #         startEPSC = index
    #         break
    tau = (idx - startEPSC) / 10
    # tau = ((idx - startEPSC) / (peakLoc - startEPSC))
    
    return tau

#%%
def getIPSCdecay(trace,traceEnd=300):
    import numpy as np
    peakLoc = np.argmax(trace[:traceEnd])
    decay = trace[peakLoc]*0.368
    for idx, i in enumerate(trace[peakLoc:]):
        if i-decay > 0:
            continue
        elif i-decay <= 0:
            break
    tau = idx / 10
    
    return tau
    
#%%
def getEPSCdecay(trace):
    import numpy as np
    peakLoc = np.argmin(trace[:300])
    decay = trace[peakLoc]*0.368
    for idx, i in enumerate(trace[peakLoc:]):
        if i-decay < 0:
            continue
        elif i-decay >= 0:
            break
    tau = idx / 10
    return tau



#%%
def getNMDAstart(trace, threshold):
    import numpy as np
    set1 = np.asarray(trace[:3000])
    set2 = np.asarray(trace[5:3005])
    derv = (set2 - set1)/5                     
    # thresh = 2
    r = np.arange(len(derv))[100:200]
    
    for index in r:
        if derv[index] < threshold :
            continue
        if derv[index] >= threshold:
            startNMDA = index
            break
        
    return startNMDA

#%%
def getNMDAdecay(trace):
    import numpy as np
    peakLoc = np.argmax(trace[:300])
    decay = trace[peakLoc]*0.368
    for idx, i in enumerate(trace[peakLoc:]):
        if i-decay > 0:
            continue
        elif i-decay <= 0:
            break
    tau = idx / 10
    
    return tau

