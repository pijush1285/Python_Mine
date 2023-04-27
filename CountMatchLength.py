# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 10:23:06 2022

@author: PIJHUSH
"""

#pip install xlrd


import pandas as pd
import math


file='C:/Users/PIJHUSH/Desktop/sheared/Simulated300/Table Length 1000/Result1000kmer30.xlsx'
#df = pd.read_excel(file)
df_sheet = pd.read_excel(file, sheet_name='Sheet28')
#print(df_sheet)



#For loop
count = 0
loc = []
for xx in range(1000):
    lowval = df_sheet['LengthLow'][xx]
    highval = df_sheet['LengthHigh'][xx]
    number = 2000000 # This will change according to the input file such as 0.05, 0.15, 0.25 
    if lowval <= number <= highval:
       # print('found one')
        count = count + 1
    else:     
        if math.isnan (lowval) == False :
            loc.append(xx)
            #print('Not found one') 
        
        
print("True value:", count)
print( "s-mer size:", df_sheet['s'][1] )




print("False value:",len(loc))
print("Blank value:", (1000-(count + len(loc)))) 
        
        
        