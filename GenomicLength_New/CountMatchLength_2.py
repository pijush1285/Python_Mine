# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 20:16:47 2022


This code is developed again. In this case you only have to put the file name and the path.
Remember to change the actual genomic length "number" such as 100, 1000, 10000 etc.

@author: dasp5
"""


#pip install xlrd
import pandas as pd
import math


# File name and the path.
path='C:/Users/dasp5.NCBI_NT/Desktop/Out/Genome Length New Analysis Scripts/OpenSyncmerResults1/5.ProcessedOnGL10L/'
file='Result1st100kmer30.xlsx'


# dataframe for getting the result values
df_acq = pd.DataFrame() 

xl = pd.ExcelFile(path+file)
res = len(xl.sheet_names)


sheet = 1
# Remember when change excel ranges changes in n-2.
# Also remenber to use the actual genomic length in "number" variable.
for yy in range(res):  #3, 8, 13, 18, 23, 28
    df_sheet = pd.read_excel(path+file, sheet_name='Sheet'+str(sheet))
    #For loop
    count = 0
    loc = []
    for xx in range(1000):
        lowval = df_sheet['LengthLow'][xx]
        highval = df_sheet['LengthHigh'][xx]
        number = 1000000 # This will change according to the input file such as 0.05, 0.15, 0.25 
        if lowval <= number <= highval:
           # print('found one')
            count = count + 1
        else:     
            if math.isnan (lowval) == False :
                loc.append(xx)
                #print('Not found one') 
            
            
    df1 = pd.DataFrame({'True value' : [count],
                   's-mer size': [df_sheet['s'][1]],
                   'False value' : [len(loc)],
                   'Blank value' : [(1000-(count + len(loc)))]
                   })
    df_acq = df_acq.append(df1, ignore_index=True)
    print(sheet)
    sheet = sheet + 1



print(df_acq['True value'])
# Copy the output result from "df_acq" manually and pest it in exccel.
        

        
        