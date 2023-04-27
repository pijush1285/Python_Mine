# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 15:47:45 2022

@author: dasp5

This code reads each text file and pick certain lines and store it 
in a data frame. Latter the data frame is printed in a excel file.

"""

import pandas as pd
import openpyxl
#import sys


# Define a data frame where the selected data Will be kept.
df5  = pd.DataFrame()  
df10 = pd.DataFrame() 
df15 = pd.DataFrame()
df20 = pd.DataFrame()
df25 = pd.DataFrame()
df30 = pd.DataFrame()


#For loop
count = 1
for xx in range(100):
    #Raw Seed file read.
    #RawSeed = pd.read_csv("C:/Users/dasp5.NCBI_NT/Desktop/Out/OperationOnLength/1.st_100_simulatedTxt/FileOperationResults_"+str(count)+".txt",header=1, sep='\t') 
    filename="C:/Users/dasp5.NCBI_NT/Desktop/Out/OperationOnLength/10.th_100_simulated/FileOperationResults_"+str(count)+".txt"
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    #len(Lines)
    #print(filename)
    df1 = Lines[1:4]                                    # K-mer size is 5
    df5 = df5.append(df1, ignore_index=True)
    df2 = Lines[4:12]                                   # K-mer size is 10
    df10 = df10.append(df2, ignore_index=True)
    df3 = Lines[12:25]                                  # K-mer size is 15
    df15 = df15.append(df3, ignore_index=True)
    df4 = Lines[25:43]                                  # K-mer size is 20
    df20 = df20.append(df4, ignore_index=True)
    df5a = Lines[43:66]                                 # K-mer size is 25
    df25 = df25.append(df5a, ignore_index=True)
    df6 = Lines[66:94]                                  # K-mer size is 30
    df30 = df30.append(df6, ignore_index=True)
    count = count + 1
    
   
    
#Write all records
cd C:\Users\dasp5.NCBI_NT\Desktop\Out\OperationOnLength\ProcessedOnText
df5.to_excel("./Result1st100kmer5.xlsx") 
df10.to_excel("./Result1st100kmer10.xlsx")
df15.to_excel("./Result1st100kmer15.xlsx")
df20.to_excel("./Result1st100kmer20.xlsx")
df25.to_excel("./Result1st100kmer25.xlsx")
df30.to_excel("./Result1st100kmer30.xlsx")   



   
    