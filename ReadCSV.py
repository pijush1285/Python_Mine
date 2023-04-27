# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 12:04:15 2022

@author: PIJHUSH
"""

import pandas as pd


data = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/RawSequence/RawCSseed.csv")                
len(data)
data.columns


data001_1 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Seed/csv/Mseed0.01_1.csv")
len(data001_1)
data001_1.columns




CommonArray1 = []
CommonArray2 = []
start        = []
count = 0
for i in range(len(data)):
    if(data['sequence'][i] == data001_1['sequence'][i]):
        start.append(data['# start'][i])
        CommonArray1.append(data['sequence'][i])
        CommonArray2.append(data001_1['sequence'][i])
        count += 1
        
  
print(count)       
print(len(data))
        

# Create DataFrame
cdata = {'start': start,'FromRawSeq': CommonArray1, 'MutatedSSeq': CommonArray2 }
df = pd.DataFrame(cdata)


       






        