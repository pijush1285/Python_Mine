# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 09:35:18 2022

@author: dasp5
"""

#pip install xlrd


import pandas as pd
import math


path='C:/Users/dasp5.NCBI_NT/Desktop/Out/Genome Length New Analysis Scripts/OpenSyncmerResults/1.Length_100/ReAnalysis/ProcessedOnText/'
file='Result1st100kmer5.xlsx'
stn=3
df_sheet = pd.read_excel(path+file, sheet_name='Sheet'+str(stn))
#print(df_sheet)



#For loop
count = 0
loc = []
for xx in range(1000):
    lowval = df_sheet['LengthLow'][xx]
    highval = df_sheet['LengthHigh'][xx]
    number = 100 # This will change according to the input file such as 0.05, 0.15, 0.25 
    if lowval < number and number < highval:
        count = count + 1
       # print('found one')        
    else:     
        if math.isnan (lowval) == False :
            loc.append(xx)
            #print('Not found one') 
        
        
print("True value:", count)
print( "s-mer size:", df_sheet['s'][1] )

print("False value:",len(loc))
print("Blank value:", (1000-(count + len(loc)))) 
        
        