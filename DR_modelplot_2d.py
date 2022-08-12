# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 12:23:28 2021

@author: Lur Lab 3
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


#set what we look at
y = 'T-Ca'
x = 'NMDA decay'
sliceParam = 'Na'
sliceVal = 0.065
delay = 'MPR%_Coincident'     #'MPR%_Coincident' or 'MPR%_50ms Delay'



#load all data
if 'Coincident' in delay:
    filepath = r'C:\Users\Lur Lab 3\Dropbox\Rindner et al\model figures\model figure data\4d plots\Tca_Na_NMDA decay_3dplot_coincident_without GABA_MEI.xlsx'
elif 'Delay' in delay:
    filepath = r'C:\Users\Lur Lab 3\Dropbox\Rindner et al\model figures\model figure data\4d plots\Tca_Na_NMDA decay_3dplot_50msdelay_without GABA_MEI.xlsx'
df = pd.read_excel(filepath, usecols="A:D")


#grab just what we're looking at
df2 = df[df[sliceParam]==sliceVal]
df2 = df2.drop(columns=[sliceParam])


# plot heatmap
plt.figure(figsize=(15,9))
pivot_table=df2.pivot(x, y, delay)
sb.heatmap(pivot_table, cmap="coolwarm", vmin= 1, vmax= 1.3, annot=True, annot_kws={"size":12}, fmt="0.2f", linewidth=2.5)
plt.ylabel(x, size= 25)
plt.xlabel(y, size=25)
plt.xticks(fontsize=15, rotation=45)
plt.yticks(fontsize=15, rotation=45)
plt.title(sliceParam+' '+str(sliceVal))








