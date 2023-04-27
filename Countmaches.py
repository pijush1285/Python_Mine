# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 10:17:17 2022

@author: PIJHUSH
"""

import pandas as pd
import math

cd C:\Users\PIJHUSH\Desktop\sheared\Table2\Dataset_100kby_1k\seed_11

RawSeed = pd.read_csv("ResultsThetak11P0.001_n100k.txt",header=0, sep=',')
RawSeed = pd.read_csv("ResultsThetak11P0.01_n100k.txt",header=0, sep=',')
RawSeed = pd.read_csv("ResultsThetak11P0.1_n100k.txt",header=0, sep=',')
RawSeed = pd.read_csv("ResultsThetak11P0.2_n100k.txt",header=0, sep=',')


cd C:\Users\PIJHUSH\Desktop\sheared\Table2\Dataset_100kby_1k\seed_21

RawSeed = pd.read_csv("ResultsThetak21P0.001_n100k.txt",header=0, sep=',')
RawSeed = pd.read_csv("ResultsThetak21P0.01_n100k.txt",header=0, sep=',')
RawSeed = pd.read_csv("ResultsThetak21P0.1_n100k.txt",header=0, sep=',')
RawSeed = pd.read_csv("ResultsThetak21P0.2_n100k.txt",header=0, sep=',')


cd C:\Users\PIJHUSH\Desktop\sheared\Table2\Dataset_100kby_1k\seed_31

RawSeed = pd.read_csv("ResultsThetak31P0.001_n100k.txt",header=0, sep=',')
RawSeed = pd.read_csv("ResultsThetak31P0.01_n100k.txt",header=0, sep=',')
RawSeed = pd.read_csv("ResultsThetak31P0.1_n100k.txt",header=0, sep=',')
RawSeed = pd.read_csv("ResultsThetak31P0.2_n100k.txt",header=0, sep=',')


cd C:\Users\PIJHUSH\Desktop\sheared\Table2\Dataset_100kby_1k\seed_41

RawSeed = pd.read_csv("ResultsThetak41P0.001_n100k.txt",header=0, sep=',')
RawSeed = pd.read_csv("ResultsThetak41P0.01_n100k.txt",header=0, sep=',')
RawSeed = pd.read_csv("ResultsThetak41P0.1_n100k.txt",header=0, sep=',')
RawSeed = pd.read_csv("ResultsThetak41P0.2_n100k.txt",header=0, sep=',')



#For loop
count = 0
loc = []
for xx in range(1000):
    lowval = RawSeed['ThetaLow'][xx]
    highval = RawSeed['ThetaHigh'][xx]
    number = 0.2 # This will change according to the input file such as 0.001, 0.01, 0.1, 0.2 
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
    



#The error in the estimate is 

    