# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 14:53:55 2022

@author: dasp5
"""

#pip install xlrd


import pandas as pd
from statistics import mean
from statistics import stdev


path='C:/Users/dasp5.NCBI_NT/Desktop/Out/Genome Length New Analysis Scripts/OpenSyncmerResults/1.Length_100/ReAnalysis/ProcessedOnText/'
file='Result1st100kmer30.xlsx'
#df = pd.read_excel(file)
#df_sheet = pd.read_excel(path+file, sheet_name='Sheet1')
#print(df_sheet)

df_avg = pd.DataFrame() 

count = 1
for xx in range(20):
    df_sheet = pd.read_excel(path+file, sheet_name='Sheet'+str(count))
    
    kmer = df_sheet['k-mer'][1]
    smer = df_sheet['s'][1]
    avg_seed = mean(df_sheet['seed'])
    avg_lowval = mean(df_sheet['LengthLow'])
    avg_highval = mean(df_sheet['LengthHigh'])
    sd_lowval = stdev(df_sheet['LengthLow'])
    sd_highval = stdev(df_sheet['LengthHigh'])
    
    
    df1 = pd.DataFrame({'k-mer' : [kmer],
               's-mer': [smer],
               'Average_Seed' : [avg_seed],
               'Average_LengthLow' : [avg_lowval],
               'Average_LengthHigh' : [avg_highval],
               'StDev_LengthLow' : [sd_lowval],
               'StDev_LengthHigh' : [sd_highval]
               })
    df_avg = df_avg.append(df1, ignore_index=True)
    print(count)
    count = count + 1

#cd C:\Users\dasp5.NCBI_NT\Desktop\Out\Genome Length New Analysis Scripts\OpenSyncmerResults\1.Length_100\ReAnalysis\ProcessedOnText
df_avg.to_excel("./Result1st100kmer30_Summery_v1.xlsx") 


######################################################################################


import pandas as pd
from statistics import mean
from statistics import stdev


path='C:/Users/dasp5.NCBI_NT/Desktop/Out/Genome Length New Analysis Scripts/OpenSyncmerResults/1.Length_100/ReAnalysis/ProcessedOnText/'
file='Result1st100kmer25.xlsx'

df_avg = pd.DataFrame() 

count = 1
for xx in range(23):
    df_sheet = pd.read_excel(path+file, sheet_name='Sheet'+str(count))
    
    kmer = df_sheet['k-mer'][1]
    smer = df_sheet['s'][1]
    avg_seed = mean(df_sheet['seed'])
    avg_lowval = mean(df_sheet['LengthLow'])
    avg_highval = mean(df_sheet['LengthHigh'])
    sd_lowval = stdev(df_sheet['LengthLow'])
    sd_highval = stdev(df_sheet['LengthHigh'])
    
    
    df1 = pd.DataFrame({'k-mer' : [kmer],
               's-mer': [smer],
               'Average_Seed' : [avg_seed],
               'Average_LengthLow' : [avg_lowval],
               'Average_LengthHigh' : [avg_highval],
               'StDev_LengthLow' : [sd_lowval],
               'StDev_LengthHigh' : [sd_highval]
               })
    df_avg = df_avg.append(df1, ignore_index=True)
    print(count)
    count = count + 1

#cd C:\Users\dasp5.NCBI_NT\Desktop\Out\Genome Length New Analysis Scripts\OpenSyncmerResults\1.Length_100\ReAnalysis\ProcessedOnText
df_avg.to_excel("./Result1st100kmer25_Summery_v1.xlsx") 



######################################################################################

import pandas as pd
from statistics import mean
from statistics import stdev


path='C:/Users/dasp5.NCBI_NT/Desktop/Out/Genome Length New Analysis Scripts/OpenSyncmerResults/1.Length_100/ReAnalysis/ProcessedOnText/'
file='Result1st100kmer20.xlsx'

df_avg = pd.DataFrame() 

count = 1
for xx in range(18):
    df_sheet = pd.read_excel(path+file, sheet_name='Sheet'+str(count))
    
    kmer = df_sheet['k-mer'][1]
    smer = df_sheet['s'][1]
    avg_seed = mean(df_sheet['seed'])
    avg_lowval = mean(df_sheet['LengthLow'])
    avg_highval = mean(df_sheet['LengthHigh'])
    sd_lowval = stdev(df_sheet['LengthLow'])
    sd_highval = stdev(df_sheet['LengthHigh'])
    
    
    df1 = pd.DataFrame({'k-mer' : [kmer],
               's-mer': [smer],
               'Average_Seed' : [avg_seed],
               'Average_LengthLow' : [avg_lowval],
               'Average_LengthHigh' : [avg_highval],
               'StDev_LengthLow' : [sd_lowval],
               'StDev_LengthHigh' : [sd_highval]
               })
    df_avg = df_avg.append(df1, ignore_index=True)
    print(count)
    count = count + 1

#cd C:\Users\dasp5.NCBI_NT\Desktop\Out\Genome Length New Analysis Scripts\OpenSyncmerResults\1.Length_100\ReAnalysis\ProcessedOnText
df_avg.to_excel("./Result1st100kmer20_Summery_v1.xlsx") 


######################################################################################


import pandas as pd
from statistics import mean
from statistics import stdev


path='C:/Users/dasp5.NCBI_NT/Desktop/Out/Genome Length New Analysis Scripts/OpenSyncmerResults/1.Length_100/ReAnalysis/ProcessedOnText/'
file='Result1st100kmer15.xlsx'

df_avg = pd.DataFrame() 

count = 1
for xx in range(13):
    df_sheet = pd.read_excel(path+file, sheet_name='Sheet'+str(count))
    
    kmer = df_sheet['k-mer'][1]
    smer = df_sheet['s'][1]
    avg_seed = mean(df_sheet['seed'])
    avg_lowval = mean(df_sheet['LengthLow'])
    avg_highval = mean(df_sheet['LengthHigh'])
    sd_lowval = stdev(df_sheet['LengthLow'])
    sd_highval = stdev(df_sheet['LengthHigh'])
    
    
    df1 = pd.DataFrame({'k-mer' : [kmer],
               's-mer': [smer],
               'Average_Seed' : [avg_seed],
               'Average_LengthLow' : [avg_lowval],
               'Average_LengthHigh' : [avg_highval],
               'StDev_LengthLow' : [sd_lowval],
               'StDev_LengthHigh' : [sd_highval]
               })
    df_avg = df_avg.append(df1, ignore_index=True)
    print(count)
    count = count + 1

#cd C:\Users\dasp5.NCBI_NT\Desktop\Out\Genome Length New Analysis Scripts\OpenSyncmerResults\1.Length_100\ReAnalysis\ProcessedOnText
df_avg.to_excel("./Result1st100kmer15_Summery_v1.xlsx") 



######################################################################################


import pandas as pd
from statistics import mean
from statistics import stdev


path='C:/Users/dasp5.NCBI_NT/Desktop/Out/Genome Length New Analysis Scripts/OpenSyncmerResults/1.Length_100/ReAnalysis/ProcessedOnText/'
file='Result1st100kmer10.xlsx'

df_avg = pd.DataFrame() 

count = 1
for xx in range(8):
    df_sheet = pd.read_excel(path+file, sheet_name='Sheet'+str(count))
    
    kmer = df_sheet['k-mer'][1]
    smer = df_sheet['s'][1]
    avg_seed = mean(df_sheet['seed'])
    avg_lowval = mean(df_sheet['LengthLow'])
    avg_highval = mean(df_sheet['LengthHigh'])
    sd_lowval = stdev(df_sheet['LengthLow'])
    sd_highval = stdev(df_sheet['LengthHigh'])
    
    
    df1 = pd.DataFrame({'k-mer' : [kmer],
               's-mer': [smer],
               'Average_Seed' : [avg_seed],
               'Average_LengthLow' : [avg_lowval],
               'Average_LengthHigh' : [avg_highval],
               'StDev_LengthLow' : [sd_lowval],
               'StDev_LengthHigh' : [sd_highval]
               })
    df_avg = df_avg.append(df1, ignore_index=True)
    print(count)
    count = count + 1

#cd C:\Users\dasp5.NCBI_NT\Desktop\Out\Genome Length New Analysis Scripts\OpenSyncmerResults\1.Length_100\ReAnalysis\ProcessedOnText
df_avg.to_excel("./Result1st100kmer10_Summery_v1.xlsx") 


######################################################################################


import pandas as pd
from statistics import mean
from statistics import stdev


path='C:/Users/dasp5.NCBI_NT/Desktop/Out/Genome Length New Analysis Scripts/OpenSyncmerResults/1.Length_100/ReAnalysis/ProcessedOnText/'
file='Result1st100kmer5.xlsx'

df_avg = pd.DataFrame() 

count = 1
for xx in range(3):
    df_sheet = pd.read_excel(path+file, sheet_name='Sheet'+str(count))
    
    kmer = df_sheet['k-mer'][1]
    smer = df_sheet['s'][1]
    avg_seed = mean(df_sheet['seed'])
    avg_lowval = mean(df_sheet['LengthLow'])
    avg_highval = mean(df_sheet['LengthHigh'])
    sd_lowval = stdev(df_sheet['LengthLow'])
    sd_highval = stdev(df_sheet['LengthHigh'])
    
    
    df1 = pd.DataFrame({'k-mer' : [kmer],
               's-mer': [smer],
               'Average_Seed' : [avg_seed],
               'Average_LengthLow' : [avg_lowval],
               'Average_LengthHigh' : [avg_highval],
               'StDev_LengthLow' : [sd_lowval],
               'StDev_LengthHigh' : [sd_highval]
               })
    df_avg = df_avg.append(df1, ignore_index=True)
    print(count)
    count = count + 1

#cd C:\Users\dasp5.NCBI_NT\Desktop\Out\Genome Length New Analysis Scripts\OpenSyncmerResults\1.Length_100\ReAnalysis\ProcessedOnText
df_avg.to_excel("./Result1st100kmer5_Summery_v1.xlsx") 
