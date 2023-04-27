# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 09:57:54 2022

@author: PIJHUSH
"""

import pandas as pd
import math

cd C:\Users\PIJHUSH\Desktop\sheared\Table3\OperationOnThetaTable3\5_Dataset_1000kby1k


RawSeed = pd.read_csv("ResultsThetak21P0.05_n1000.txt",header=0, sep=',')
RawSeed = pd.read_csv("ResultsThetak21P0.15_n1000.txt",header=0, sep=',')
RawSeed = pd.read_csv("ResultsThetak21P0.25_n1000.txt",header=0, sep=',')


#For loop
count = 0
loc = []
for xx in range(1000):
    lowval = RawSeed['ThetaLow'][xx]
    highval = RawSeed['ThetaHigh'][xx]
    number = 0.25 # This will change according to the input file such as 0.05, 0.15, 0.25 
    if lowval <= number <= highval:
       # print('found one')
        count = count + 1
    else:     
        if math.isnan (lowval) == False :
            loc.append(xx)
            #print('Not found one') 
        

print("True value:", count)
print("False value:",len(loc))
print("Blank value:", (1000-(count + len(loc)))) 
    
