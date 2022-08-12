# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 13:39:13 2021

@author: Lur Lab 3
"""
#%%
import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d

#%%read in data

def read_data(filePath):
    
    data = pd.read_excel(filePath, usecols="A:D")

    return data

#%% make plot
    
def make3d(colorDimension):    
    
    ax1 = plt.figure().gca(projection='3d')
    plt.gca().invert_yaxis()
    
    x = 'NMDA decay'
    y = 'Na'
    z = 'T-Ca'
    

    vmin = 1.00
    vmax = 1.30
    
    scatplot = ax1.scatter(data[x], data[y], data[z], c=data[colorDimension], cmap='bwr', label='example', vmin=vmin, vmax=vmax, depthshade=True, alpha = 1, s=20)
    plt.colorbar(scatplot, label=colorDimension)
    
    plt.legend()
    ax1.set_xlabel(x)
    ax1.set_ylabel(y)
    ax1.set_zlabel(z)
    plt.show()
    
    
    
#%%main
coincidentPath = r'C:/Users/Lur Lab 3/Dropbox/Rindner et al/model figures/model figure data/4d plots/Tca_Na_NMDA decay_3dplot_coincident_without GABA_MEI.xlsx'
delayPath = r'C:/Users/Lur Lab 3/Dropbox/Rindner et al/model figures/model figure data/4d plots/Tca_Na_NMDA decay_3dplot_50msdelay_without GABA_MEI.xlsx'

for iPath in [coincidentPath, delayPath]:

    data = read_data(iPath)
    
    if 'coincident' in iPath:
        make3d('MPR%_Coincident')
    elif '50ms' in iPath:
        make3d('MPR%_50ms Delay')        