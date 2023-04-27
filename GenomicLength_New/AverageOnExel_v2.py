# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 23:24:31 2023

@author: dasp5
"""

import os
import pandas as pd
from statistics import mean
from statistics import stdev


path='C:/Users/dasp5.NCBI_NT/Desktop/Out/Genome Length New Analysis Scripts/OpenSyncmerResults1/5.ProcessedOnGL10L/'




#For loop
for yy in range(6):
    if yy == 0:
        file='Result1st100kmer5.xlsx'
    if yy == 1: 
        file='Result1st100kmer10.xlsx'
    if yy == 2: 
        file='Result1st100kmer15.xlsx'
    if yy == 3: 
        file='Result1st100kmer20.xlsx'
    if yy == 4: 
        file='Result1st100kmer25.xlsx'
    if yy == 5: 
        file='Result1st100kmer30.xlsx'
        
    xl = pd.ExcelFile(path+file)
    res = len(xl.sheet_names)
    df_avg = pd.DataFrame() 
    count = 1
    for xx in range(res):
        df_sheet = pd.read_excel(path+file, sheet_name='Sheet'+str(count))
    
        kmer = df_sheet['k-mer'][1]
        smer = df_sheet['s'][1]
        #avg_seed = mean(df_sheet['seed'])
        avg_lowval = mean(df_sheet['LengthLow'])
        avg_highval = mean(df_sheet['LengthHigh'])
        sd_lowval = stdev(df_sheet['LengthLow'])
        sd_highval = stdev(df_sheet['LengthHigh'])
    
    
        df1 = pd.DataFrame({'k-mer' : [kmer],
                            's-mer': [smer],
                            #'Average_Seed' : [avg_seed],
                            'Average_LengthLow' : [avg_lowval],
                            'Average_LengthHigh' : [avg_highval],
                            'StDev_LengthLow' : [sd_lowval],
                            'StDev_LengthHigh' : [sd_highval]
                            })
        df_avg = df_avg.append(df1, ignore_index=True)
        print(count)
        count = count + 1

    if yy == 0:
        os.chdir(path)
        df_avg.to_excel("./Result1st100kmer5_Summery_v1.xlsx") 
        print("K-mer-5: Completed")
    if yy == 1:
        os.chdir(path)
        df_avg.to_excel("./Result1st100kmer10_Summery_v1.xlsx") 
        print("K-mer-10: Completed")
    if yy == 2: 
        os.chdir(path)
        df_avg.to_excel("./Result1st100kmer15_Summery_v1.xlsx")
        print("K-mer-15: Completed")
    if yy == 3: 
        os.chdir(path)
        df_avg.to_excel("./Result1st100kmer20_Summery_v1.xlsx") 
        print("K-mer-20: Completed")
    if yy == 4: 
        os.chdir(path)
        df_avg.to_excel("./Result1st100kmer25_Summery_v1.xlsx") 
        print("K-mer-25: Completed")
    if yy == 5: 
        os.chdir(path)
        df_avg.to_excel("./Result1st100kmer30_Summery_v1.xlsx")
        print("K-mer-30: Completed")


 


 






