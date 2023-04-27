# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 14:53:24 2022

@author: dasp5

This code reads each text file and pick certain lines and store it 
in a data frame. Latter the data frame is printed in a excel file.
But in this case the line choosing is different.

"""


import pandas as pd
#import openpyxl
#import sys


# Define a data frame where the selected data Will be kept.
df7_2  = pd.DataFrame()  
df7_3  = pd.DataFrame() 
df7_4  = pd.DataFrame() 
df7_5  = pd.DataFrame()
df7_6  = pd.DataFrame()

df9_2 = pd.DataFrame() 
df9_3 = pd.DataFrame() 
df9_4 = pd.DataFrame() 
df9_5 = pd.DataFrame() 
df9_6 = pd.DataFrame() 
df9_7 = pd.DataFrame() 
df9_8 = pd.DataFrame()


df11_2 = pd.DataFrame()
df11_3 = pd.DataFrame()
df11_4 = pd.DataFrame()
df11_5 = pd.DataFrame()
df11_6 = pd.DataFrame()
df11_7 = pd.DataFrame()
df11_8 = pd.DataFrame()
df11_9 = pd.DataFrame()
df11_10 = pd.DataFrame()


df13_2 = pd.DataFrame()
df13_3 = pd.DataFrame()
df13_4 = pd.DataFrame()
df13_5 = pd.DataFrame()
df13_6 = pd.DataFrame()
df13_7 = pd.DataFrame()
df13_8 = pd.DataFrame()
df13_9 = pd.DataFrame()
df13_10 = pd.DataFrame()
df13_11 = pd.DataFrame()
df13_12 = pd.DataFrame()


df17_2 = pd.DataFrame()
df17_3 = pd.DataFrame()
df17_4 = pd.DataFrame()
df17_5 = pd.DataFrame()
df17_6 = pd.DataFrame()
df17_7 = pd.DataFrame()
df17_8 = pd.DataFrame()
df17_9 = pd.DataFrame()
df17_10 = pd.DataFrame()
df17_11 = pd.DataFrame()
df17_12 = pd.DataFrame()
df17_13 = pd.DataFrame()
df17_14 = pd.DataFrame()
df17_15 = pd.DataFrame()
df17_16 = pd.DataFrame()


df19_2 = pd.DataFrame()
df19_3 = pd.DataFrame()
df19_4 = pd.DataFrame()
df19_5 = pd.DataFrame()
df19_6 = pd.DataFrame()
df19_7 = pd.DataFrame()
df19_8 = pd.DataFrame()
df19_9 = pd.DataFrame()
df19_10 = pd.DataFrame()
df19_11 = pd.DataFrame()
df19_12 = pd.DataFrame()
df19_13 = pd.DataFrame()
df19_14 = pd.DataFrame()
df19_15 = pd.DataFrame()
df19_16 = pd.DataFrame()
df19_17 = pd.DataFrame()
df19_18 = pd.DataFrame()



df21_2 = pd.DataFrame()
df21_3 = pd.DataFrame()
df21_4 = pd.DataFrame()
df21_5 = pd.DataFrame()
df21_6 = pd.DataFrame()
df21_7 = pd.DataFrame()
df21_8 = pd.DataFrame()
df21_9 = pd.DataFrame()
df21_10 = pd.DataFrame()
df21_11 = pd.DataFrame()
df21_12 = pd.DataFrame()
df21_13 = pd.DataFrame()
df21_14 = pd.DataFrame()
df21_15 = pd.DataFrame()
df21_16 = pd.DataFrame()
df21_17 = pd.DataFrame()
df21_18 = pd.DataFrame()
df21_19 = pd.DataFrame()
df21_20 = pd.DataFrame()

df23_2 = pd.DataFrame()
df23_3 = pd.DataFrame()
df23_4 = pd.DataFrame()
df23_5 = pd.DataFrame()
df23_6 = pd.DataFrame()
df23_7 = pd.DataFrame()
df23_8 = pd.DataFrame()
df23_9 = pd.DataFrame()
df23_10 = pd.DataFrame()
df23_11 = pd.DataFrame()
df23_12 = pd.DataFrame()
df23_13 = pd.DataFrame()
df23_14 = pd.DataFrame()
df23_15 = pd.DataFrame()
df23_16 = pd.DataFrame()
df23_17 = pd.DataFrame()
df23_18 = pd.DataFrame()
df23_19 = pd.DataFrame()
df23_20 = pd.DataFrame()
df23_21 = pd.DataFrame()
df23_22 = pd.DataFrame()


df27_2 = pd.DataFrame()
df27_3 = pd.DataFrame()
df27_4 = pd.DataFrame()
df27_5 = pd.DataFrame()
df27_6 = pd.DataFrame()
df27_7 = pd.DataFrame()
df27_8 = pd.DataFrame()
df27_9 = pd.DataFrame()
df27_10 = pd.DataFrame()
df27_11 = pd.DataFrame()
df27_12 = pd.DataFrame()
df27_13 = pd.DataFrame()
df27_14 = pd.DataFrame()
df27_15 = pd.DataFrame()
df27_16 = pd.DataFrame()
df27_17 = pd.DataFrame()
df27_18 = pd.DataFrame()
df27_19 = pd.DataFrame()
df27_20 = pd.DataFrame()
df27_21 = pd.DataFrame()
df27_22 = pd.DataFrame()
df27_23 = pd.DataFrame()
df27_24 = pd.DataFrame()
df27_25 = pd.DataFrame()
df27_26 = pd.DataFrame()


df29_2 = pd.DataFrame()
df29_3 = pd.DataFrame()
df29_4 = pd.DataFrame()
df29_5 = pd.DataFrame()
df29_6 = pd.DataFrame()
df29_7 = pd.DataFrame()
df29_8 = pd.DataFrame()
df29_9 = pd.DataFrame()
df29_10 = pd.DataFrame()
df29_11 = pd.DataFrame()
df29_12 = pd.DataFrame()
df29_13 = pd.DataFrame()
df29_14 = pd.DataFrame()
df29_15 = pd.DataFrame()
df29_16 = pd.DataFrame()
df29_17 = pd.DataFrame()
df29_18 = pd.DataFrame()
df29_19 = pd.DataFrame()
df29_20 = pd.DataFrame()
df29_21 = pd.DataFrame()
df29_22 = pd.DataFrame()
df29_23 = pd.DataFrame()
df29_24 = pd.DataFrame()
df29_25 = pd.DataFrame()
df29_26 = pd.DataFrame()
df29_27 = pd.DataFrame()
df29_28 = pd.DataFrame()





#For loop
count = 1
for xx in range(100):
   # filename="C:/Users/dasp5.NCBI_NT/Desktop/Out/Genome Length New Analysis Scripts/Results/1.st_100_simulated/FinalEven/FileOperationResults_"+str(count)+".txt"
   # filename="C:/Users/dasp5.NCBI_NT/Desktop/Out/Genome Length New Analysis Scripts/Results/2.st_100_simulated/FinalEven/FileOperationResults_"+str(count)+".txt"
   # filename="C:/Users/dasp5.NCBI_NT/Desktop/Out/Genome Length New Analysis Scripts/Results/3.st_100_simulated/FinalEven/FileOperationResults_"+str(count)+".txt"
   # filename="C:/Users/dasp5.NCBI_NT/Desktop/Out/Genome Length New Analysis Scripts/Results/4.st_100_simulated/FinalEven/FileOperationResults_"+str(count)+".txt"
   # filename="C:/Users/dasp5.NCBI_NT/Desktop/Out/Genome Length New Analysis Scripts/Results/5.st_100_simulated/FinalEven/FileOperationResults_"+str(count)+".txt"
   # filename="C:/Users/dasp5.NCBI_NT/Desktop/Out/Genome Length New Analysis Scripts/Results/6.st_100_simulated/FinalEven/FileOperationResults_"+str(count)+".txt"
   # filename="C:/Users/dasp5.NCBI_NT/Desktop/Out/Genome Length New Analysis Scripts/Results/7.st_100_simulated/FinalEven/FileOperationResults_"+str(count)+".txt"
   # filename="C:/Users/dasp5.NCBI_NT/Desktop/Out/Genome Length New Analysis Scripts/Results/8.st_100_simulated/FinalEven/FileOperationResults_"+str(count)+".txt"
   # filename="C:/Users/dasp5.NCBI_NT/Desktop/Out/Genome Length New Analysis Scripts/Results/9.st_100_simulated/FinalEven/FileOperationResults_"+str(count)+".txt"
    filename="C:/Users/dasp5.NCBI_NT/Desktop/Out/Genome Length New Analysis Scripts/Results/10.st_100_simulated/FinalEven/FileOperationResults_"+str(count)+".txt"
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    #len(Lines)
    #print(filename)
     
    
    df7_2l  = [Lines[1]] 
    df7_2   = df7_2.append(df7_2l, ignore_index=True)
    df7_3l  = [Lines[2]] 
    df7_3   = df7_3.append(df7_3l, ignore_index=True)
    df7_4l  = [Lines[3]] 
    df7_4   = df7_4.append(df7_4l, ignore_index=True)
    df7_5l  = [Lines[4]] 
    df7_5   = df7_5.append(df7_5l, ignore_index=True)
    df7_6l  = [Lines[5]] 
    df7_6   = df7_6.append(df7_6l, ignore_index=True)
    
    
    df9_2l = [Lines[6]] 
    df9_2  = df9_2.append(df9_2l, ignore_index=True)
    df9_3l = [Lines[7]] 
    df9_3  = df9_3.append(df9_3l, ignore_index=True)
    df9_4l = [Lines[8]] 
    df9_4  = df9_4.append(df9_4l, ignore_index=True)
    df9_5l = [Lines[9]] 
    df9_5  = df9_5.append(df9_5l, ignore_index=True)
    df9_6l = [Lines[10]] 
    df9_6  = df9_6.append(df9_6l, ignore_index=True)
    df9_7l = [Lines[11]] 
    df9_7  = df9_7.append(df9_7l, ignore_index=True)
    df9_8l = [Lines[12]] 
    df9_8  = df9_8.append(df9_8l, ignore_index=True)
    
    
    df11_2l = [Lines[13]] 
    df11_2  = df11_2.append(df11_2l, ignore_index=True)
    df11_3l = [Lines[14]] 
    df11_3  = df11_3.append(df11_3l, ignore_index=True)
    df11_4l = [Lines[15]] 
    df11_4  = df11_4.append(df11_4l, ignore_index=True)
    df11_5l = [Lines[16]] 
    df11_5  = df11_5.append(df11_5l, ignore_index=True)
    df11_6l = [Lines[17]] 
    df11_6  = df11_6.append(df11_6l, ignore_index=True)
    df11_7l = [Lines[18]] 
    df11_7  = df11_7.append(df11_7l, ignore_index=True)
    df11_8l = [Lines[19]] 
    df11_8  = df11_8.append(df11_8l, ignore_index=True)
    df11_9l = [Lines[20]] 
    df11_9  = df11_9.append(df11_9l, ignore_index=True)
    df11_10l = [Lines[21]] 
    df11_10  = df11_10.append(df11_10l, ignore_index=True)
    
  
    df13_2l = [Lines[22]] 
    df13_2  = df13_2.append(df13_2l, ignore_index=True)
    df13_3l = [Lines[23]] 
    df13_3  = df13_3.append(df13_3l, ignore_index=True)
    df13_4l = [Lines[24]] 
    df13_4  = df13_4.append(df13_4l, ignore_index=True)
    df13_5l = [Lines[25]] 
    df13_5  = df13_5.append(df13_5l, ignore_index=True)
    df13_6l = [Lines[26]] 
    df13_6  = df13_6.append(df13_6l, ignore_index=True)
    df13_7l = [Lines[27]] 
    df13_7  = df13_7.append(df13_7l, ignore_index=True)
    df13_8l = [Lines[28]] 
    df13_8  = df13_8.append(df13_8l, ignore_index=True)
    df13_9l = [Lines[29]] 
    df13_9  = df13_9.append(df13_9l, ignore_index=True)
    df13_10l = [Lines[30]] 
    df13_10  = df13_10.append(df13_10l, ignore_index=True)
    df13_11l = [Lines[31]] 
    df13_11  = df13_11.append(df13_11l, ignore_index=True)
    df13_12l = [Lines[32]] 
    df13_12  = df13_12.append(df13_12l, ignore_index=True)
    
    
    df17_2l = [Lines[33]] 
    df17_2  = df17_2.append(df17_2l, ignore_index=True)
    df17_3l = [Lines[34]] 
    df17_3  = df17_3.append(df17_3l, ignore_index=True)
    df17_4l = [Lines[35]] 
    df17_4  = df17_4.append(df17_4l, ignore_index=True)
    df17_5l = [Lines[36]] 
    df17_5  = df17_5.append(df17_5l, ignore_index=True)
    df17_6l = [Lines[37]] 
    df17_6  = df17_6.append(df17_6l, ignore_index=True)
    df17_7l = [Lines[38]] 
    df17_7  = df17_7.append(df17_7l, ignore_index=True)
    df17_8l = [Lines[39]] 
    df17_8  = df17_8.append(df17_8l, ignore_index=True)
    df17_9l = [Lines[40]] 
    df17_9  = df17_9.append(df17_9l, ignore_index=True)
    df17_10l = [Lines[41]] 
    df17_10  = df17_10.append(df17_10l, ignore_index=True)
    df17_11l = [Lines[42]] 
    df17_11  = df17_11.append(df17_11l, ignore_index=True)
    df17_12l = [Lines[43]] 
    df17_12  = df17_12.append(df17_12l, ignore_index=True)
    df17_13l = [Lines[44]] 
    df17_13  = df17_13.append(df17_13l, ignore_index=True)
    df17_14l = [Lines[45]] 
    df17_14  = df17_14.append(df17_14l, ignore_index=True)
    df17_15l = [Lines[46]] 
    df17_15  = df17_15.append(df17_15l, ignore_index=True)
    df17_16l =  [Lines[47]] 
    df17_16  = df17_16.append(df17_16l, ignore_index=True)
  
    
    df19_2l = [Lines[48]] 
    df19_2  = df19_2.append(df19_2l, ignore_index=True)
    df19_3l = [Lines[49]] 
    df19_3  = df19_3.append(df19_3l, ignore_index=True)
    df19_4l = [Lines[50]] 
    df19_4  = df19_4.append(df19_4l, ignore_index=True)
    df19_5l = [Lines[51]] 
    df19_5  = df19_5.append(df19_5l, ignore_index=True)
    df19_6l = [Lines[52]] 
    df19_6  = df19_6.append(df19_6l, ignore_index=True)
    df19_7l = [Lines[53]] 
    df19_7  = df19_7.append(df19_7l, ignore_index=True)
    df19_8l = [Lines[54]] 
    df19_8  = df19_8.append(df19_8l, ignore_index=True)
    df19_9l = [Lines[55]] 
    df19_9  = df19_9.append(df19_9l, ignore_index=True)
    df19_10l = [Lines[56]] 
    df19_10  = df19_10.append(df19_10l, ignore_index=True)
    df19_11l = [Lines[57]] 
    df19_11  = df19_11.append(df19_11l, ignore_index=True)
    df19_12l = [Lines[58]] 
    df19_12  = df19_12.append(df19_12l, ignore_index=True)
    df19_13l = [Lines[59]] 
    df19_13  = df19_13.append(df19_13l, ignore_index=True)
    df19_14l = [Lines[60]] 
    df19_14  = df19_14.append(df19_14l, ignore_index=True)
    df19_15l = [Lines[61]] 
    df19_15  = df19_15.append(df19_15l, ignore_index=True)
    df19_16l = [Lines[62]] 
    df19_16  = df19_16.append(df19_16l, ignore_index=True)
    df19_17l = [Lines[63]] 
    df19_17  = df19_17.append(df19_17l, ignore_index=True)
    df19_18l = [Lines[64]] 
    df19_18  = df19_18.append(df19_18l, ignore_index=True)
    
    
    df21_2l = [Lines[65]] 
    df21_2 = df21_2.append(df21_2l, ignore_index=True)
    df21_3l = [Lines[66]] 
    df21_3 = df21_3.append(df21_3l, ignore_index=True)
    df21_4l = [Lines[67]] 
    df21_4 = df21_4.append(df21_4l, ignore_index=True)
    df21_5l = [Lines[68]] 
    df21_5 = df21_5.append(df21_5l, ignore_index=True)
    df21_6l = [Lines[69]] 
    df21_6 = df21_6.append(df21_6l, ignore_index=True)
    df21_7l = [Lines[70]] 
    df21_7 = df21_7.append(df21_7l, ignore_index=True)
    df21_8l = [Lines[71]] 
    df21_8 = df21_8.append(df21_8l, ignore_index=True)
    df21_9l = [Lines[72]] 
    df21_9 = df21_9.append(df21_9l, ignore_index=True)
    df21_10l = [Lines[73]] 
    df21_10 = df21_10.append(df21_10l, ignore_index=True)
    df21_11l = [Lines[74]] 
    df21_11 = df21_11.append(df21_11l, ignore_index=True)
    df21_12l = [Lines[75]] 
    df21_12 =df21_12.append(df21_12l, ignore_index=True)
    df21_13l = [Lines[76]] 
    df21_13 = df21_13.append(df21_13l, ignore_index=True)
    df21_14l = [Lines[77]] 
    df21_14 =df21_14.append(df21_14l, ignore_index=True)
    df21_15l = [Lines[78]] 
    df21_15 = df21_15.append(df21_15l, ignore_index=True)
    df21_16l = [Lines[79]] 
    df21_16 =df21_16.append(df21_16l, ignore_index=True)
    df21_17l = [Lines[80]] 
    df21_17 = df21_17.append(df21_17l, ignore_index=True)
    df21_18l = [Lines[81]] 
    df21_18 = df21_18.append(df21_18l, ignore_index=True)
    df21_19l = [Lines[82]] 
    df21_19 = df21_19.append(df21_19l, ignore_index=True)
    df21_20l = [Lines[83]] 
    df21_20 = df21_20.append(df21_20l, ignore_index=True)
    
    
    
    
    df23_2l =  [Lines[84]] 
    df23_2  =  df23_2.append(df23_2l, ignore_index=True)
    df23_3l =  [Lines[85]] 
    df23_3  =  df23_3.append(df23_3l, ignore_index=True)
    df23_4l =  [Lines[86]]  
    df23_4  =  df23_4.append(df23_4l, ignore_index=True)
    df23_5l =  [Lines[87]]  
    df23_5  =  df23_5.append(df23_5l, ignore_index=True)
    df23_6l =  [Lines[88]]  
    df23_6  =  df23_6.append(df23_6l, ignore_index=True)
    df23_7l =  [Lines[89]]  
    df23_7  =  df23_7.append(df23_7l, ignore_index=True)
    df23_8l =  [Lines[90]] 
    df23_8  =  df23_8.append(df23_8l, ignore_index=True)
    df23_9l =  [Lines[91]] 
    df23_9  =  df23_9.append(df23_9l, ignore_index=True)
    df23_10l =  [Lines[92]] 
    df23_10  =  df23_10.append(df23_10l, ignore_index=True)
    df23_11l =  [Lines[93]] 
    df23_11  =  df23_11.append(df23_11l, ignore_index=True)
    df23_12l =  [Lines[94]] 
    df23_12  =  df23_12.append(df23_12l, ignore_index=True)
    df23_13l =  [Lines[95]]  
    df23_13  =  df23_13.append(df23_13l, ignore_index=True)
    df23_14l =  [Lines[96]] 
    df23_14  =  df23_14.append(df23_14l, ignore_index=True)
    df23_15l =  [Lines[97]] 
    df23_15  =  df23_15.append(df23_15l, ignore_index=True)
    df23_16l =  [Lines[98]] 
    df23_16  =  df23_16.append(df23_16l, ignore_index=True)
    df23_17l =  [Lines[99]] 
    df23_17  =  df23_17.append(df23_17l, ignore_index=True)
    df23_18l =  [Lines[100]] 
    df23_18  =  df23_18.append(df23_18l, ignore_index=True)
    df23_19l =  [Lines[101]] 
    df23_19  =  df23_19.append(df23_19l, ignore_index=True)
    df23_20l =  [Lines[102]] 
    df23_20  =  df23_20.append(df23_20l, ignore_index=True)
    df23_21l =  [Lines[103]] 
    df23_21  =  df23_21.append(df23_21l, ignore_index=True)
    df23_22l =  [Lines[104]] 
    df23_22  =  df23_22.append(df23_22l, ignore_index=True)
    
    
    
    df27_2l = [Lines[105]] 
    df27_2  = df27_2.append(df27_2l, ignore_index=True)
    df27_3l = [Lines[106]] 
    df27_3  = df27_3.append(df27_3l, ignore_index=True)
    df27_4l = [Lines[107]] 
    df27_4  = df27_4.append(df27_4l, ignore_index=True)
    df27_5l = [Lines[108]] 
    df27_5  = df27_5.append(df27_5l, ignore_index=True)
    df27_6l = [Lines[109]] 
    df27_6  = df27_6.append(df27_6l, ignore_index=True)
    df27_7l = [Lines[110]] 
    df27_7  = df27_7.append(df27_7l, ignore_index=True)
    df27_8l = [Lines[111]] 
    df27_8  = df27_8.append(df27_8l, ignore_index=True)
    df27_9l = [Lines[112]] 
    df27_9  = df27_9.append(df27_9l, ignore_index=True)
    df27_10l = [Lines[113]] 
    df27_10  = df27_10.append(df27_10l, ignore_index=True)
    df27_11l = [Lines[114]] 
    df27_11  = df27_11.append(df27_11l, ignore_index=True)
    df27_12l = [Lines[115]] 
    df27_12  = df27_12.append(df27_12l, ignore_index=True)
    df27_13l = [Lines[116]] 
    df27_13  = df27_13.append(df27_13l, ignore_index=True)
    df27_14l = [Lines[117]] 
    df27_14  = df27_14.append(df27_14l, ignore_index=True)
    df27_15l = [Lines[118]] 
    df27_15  = df27_15.append(df27_15l, ignore_index=True)
    df27_16l = [Lines[119]] 
    df27_16  = df27_16.append(df27_16l, ignore_index=True)
    df27_17l = [Lines[120]] 
    df27_17  = df27_17.append(df27_17l, ignore_index=True)
    df27_18l = [Lines[121]] 
    df27_18  = df27_18.append(df27_18l, ignore_index=True)
    df27_19l = [Lines[122]] 
    df27_19  = df27_19.append(df27_19l, ignore_index=True)
    df27_20l = [Lines[123]] 
    df27_20  = df27_20.append(df27_20l, ignore_index=True)
    df27_21l = [Lines[124]] 
    df27_21  = df27_21.append(df27_21l, ignore_index=True)
    df27_22l = [Lines[125]] 
    df27_22  = df27_22.append(df27_22l, ignore_index=True)
    df27_23l = [Lines[126]] 
    df27_23  = df27_23.append(df27_23l, ignore_index=True)
    df27_24l = [Lines[127]] 
    df27_24  = df27_24.append(df27_24l, ignore_index=True)
    df27_25l = [Lines[128]] 
    df27_25  = df27_25.append(df27_25l, ignore_index=True)
    df27_26l = [Lines[129]] 
    df27_26  = df27_26.append(df27_26l, ignore_index=True)
    
    
    
    df29_2l = [Lines[130]]
    df29_2  = df29_2.append(df29_2l, ignore_index=True)
    df29_3l = [Lines[131]]
    df29_3  = df29_3.append(df29_3l, ignore_index=True)
    df29_4l = [Lines[132]]
    df29_4  = df29_4.append(df29_4l, ignore_index=True)
    df29_5l = [Lines[133]]
    df29_5  = df29_5.append(df29_5l, ignore_index=True)
    df29_6l = [Lines[134]]
    df29_6  = df29_6.append(df29_6l, ignore_index=True)
    df29_7l = [Lines[135]]
    df29_7  = df29_7.append(df29_7l, ignore_index=True)
    df29_8l = [Lines[136]]
    df29_8  = df29_8.append(df29_8l, ignore_index=True)
    df29_9l = [Lines[137]]
    df29_9  = df29_9.append(df29_9l, ignore_index=True)
    df29_10l = [Lines[138]]
    df29_10  = df29_10.append(df29_10l, ignore_index=True)
    df29_11l = [Lines[139]]
    df29_11  = df29_11.append(df29_11l, ignore_index=True)
    df29_12l = [Lines[140]]
    df29_12  = df29_12.append(df29_12l, ignore_index=True)
    df29_13l = [Lines[141]]
    df29_13  = df29_13.append(df29_13l, ignore_index=True)
    df29_14l = [Lines[142]]
    df29_14  = df29_14.append(df29_14l, ignore_index=True)
    df29_15l = [Lines[143]]
    df29_15  = df29_15.append(df29_15l, ignore_index=True)
    df29_16l = [Lines[144]]
    df29_16  = df29_16.append(df29_16l, ignore_index=True)
    df29_17l = [Lines[145]]
    df29_17  = df29_17.append(df29_17l, ignore_index=True)
    df29_18l = [Lines[146]]
    df29_18  = df29_18.append(df29_18l, ignore_index=True)
    df29_19l = [Lines[147]]
    df29_19  = df29_19.append(df29_19l, ignore_index=True)
    df29_20l = [Lines[148]]
    df29_20  = df29_20.append(df29_20l, ignore_index=True)
    df29_21l = [Lines[149]]
    df29_21  = df29_21.append(df29_21l, ignore_index=True)
    df29_22l = [Lines[150]]
    df29_22  = df29_22.append(df29_22l, ignore_index=True)
    df29_23l = [Lines[151]]
    df29_23  = df29_23.append(df29_23l, ignore_index=True)
    df29_24l = [Lines[152]]
    df29_24  = df29_24.append(df29_24l, ignore_index=True)
    df29_25l = [Lines[153]]
    df29_25  = df29_25.append(df29_25l, ignore_index=True)
    df29_26l = [Lines[154]]
    df29_26  = df29_26.append(df29_26l, ignore_index=True)
    df29_27l = [Lines[155]]
    df29_27  = df29_27.append(df29_27l, ignore_index=True)
    df29_28l = [Lines[156]]
    df29_28  = df29_28.append(df29_28l, ignore_index=True)
    count = count + 1
    
    

   
    
#Write all records
#cd C:\Users\dasp5.NCBI_NT\Desktop\Out\Genome Length New Analysis Scripts\Results\ProcessedOnTextEven

writer1 = pd.ExcelWriter('Result1000kmer7.xlsx', engine='xlsxwriter')
df7_2.to_excel(writer1, sheet_name='Sheet1')
df7_3.to_excel(writer1, sheet_name='Sheet2')
df7_4.to_excel(writer1, sheet_name='Sheet3')
df7_5.to_excel(writer1, sheet_name='Sheet4')
df7_6.to_excel(writer1, sheet_name='Sheet5')
writer1.save()

writer2 = pd.ExcelWriter('Result1000kmer9.xlsx', engine='xlsxwriter')
df9_2.to_excel(writer2, sheet_name='Sheet1')
df9_3.to_excel(writer2, sheet_name='Sheet2')
df9_4.to_excel(writer2, sheet_name='Sheet3')
df9_5.to_excel(writer2, sheet_name='Sheet4')
df9_6.to_excel(writer2, sheet_name='Sheet5')
df9_7.to_excel(writer2, sheet_name='Sheet6')
df9_8.to_excel(writer2, sheet_name='Sheet7')
writer2.save()


writer3 = pd.ExcelWriter('Result1000kmer11.xlsx', engine='xlsxwriter')
df11_2.to_excel(writer3, sheet_name='Sheet1')
df11_3.to_excel(writer3, sheet_name='Sheet2')
df11_4.to_excel(writer3, sheet_name='Sheet3')
df11_5.to_excel(writer3, sheet_name='Sheet4')
df11_6.to_excel(writer3, sheet_name='Sheet5')
df11_7.to_excel(writer3, sheet_name='Sheet6')
df11_8.to_excel(writer3, sheet_name='Sheet7')
df11_9.to_excel(writer3, sheet_name='Sheet8')
df11_10.to_excel(writer3, sheet_name='Sheet9')
writer3.save()



writer4 = pd.ExcelWriter('Result1000kmer13.xlsx', engine='xlsxwriter')
df13_2.to_excel(writer4, sheet_name='Sheet1')
df13_3.to_excel(writer4, sheet_name='Sheet2')
df13_4.to_excel(writer4, sheet_name='Sheet3')
df13_5.to_excel(writer4, sheet_name='Sheet4')
df13_6.to_excel(writer4, sheet_name='Sheet5')
df13_7.to_excel(writer4, sheet_name='Sheet6')
df13_8.to_excel(writer4, sheet_name='Sheet7')
df13_9.to_excel(writer4, sheet_name='Sheet8')
df13_10.to_excel(writer4, sheet_name='Sheet9')
df13_11.to_excel(writer4, sheet_name='Sheet10')
df13_12.to_excel(writer4, sheet_name='Sheet11')
writer4.save()


writer5 = pd.ExcelWriter('Result1000kmer17.xlsx', engine='xlsxwriter')
df17_2.to_excel(writer5, sheet_name = 'Sheet1')
df17_3.to_excel(writer5, sheet_name = 'Sheet2')
df17_4.to_excel(writer5, sheet_name = 'Sheet3')
df17_5.to_excel(writer5, sheet_name = 'Sheet4')
df17_6.to_excel(writer5, sheet_name = 'Sheet5')
df17_7.to_excel(writer5, sheet_name = 'Sheet6')
df17_8.to_excel(writer5, sheet_name = 'Sheet7')
df17_9.to_excel(writer5, sheet_name = 'Sheet8')
df17_10.to_excel(writer5, sheet_name = 'Sheet9')
df17_11.to_excel(writer5, sheet_name = 'Sheet10')
df17_12.to_excel(writer5, sheet_name = 'Sheet11')
df17_13.to_excel(writer5, sheet_name = 'Sheet12')
df17_14.to_excel(writer5, sheet_name = 'Sheet13')
df17_15.to_excel(writer5, sheet_name = 'Sheet14')
df17_16.to_excel(writer5, sheet_name = 'Sheet15')
writer5.save()


writer6 = pd.ExcelWriter('Result1000kmer19.xlsx', engine='xlsxwriter')
df19_2.to_excel(writer6, sheet_name = 'Sheet1')
df19_3.to_excel(writer6, sheet_name = 'Sheet2')
df19_4.to_excel(writer6, sheet_name = 'Sheet3')
df19_5.to_excel(writer6, sheet_name = 'Sheet4')
df19_6.to_excel(writer6, sheet_name = 'Sheet5')
df19_7.to_excel(writer6, sheet_name = 'Sheet6')
df19_8.to_excel(writer6, sheet_name = 'Sheet7')
df19_9.to_excel(writer6, sheet_name = 'Sheet8')
df19_10.to_excel(writer6, sheet_name = 'Sheet9')
df19_11.to_excel(writer6, sheet_name = 'Sheet10')
df19_12.to_excel(writer6, sheet_name = 'Sheet11')
df19_13.to_excel(writer6, sheet_name = 'Sheet12')
df19_14.to_excel(writer6, sheet_name = 'Sheet13')
df19_15.to_excel(writer6, sheet_name = 'Sheet14')
df19_16.to_excel(writer6, sheet_name = 'Sheet15')
df19_17.to_excel(writer6, sheet_name = 'Sheet16')
df19_18.to_excel(writer6, sheet_name = 'Sheet17')
writer6.save()


writer7 = pd.ExcelWriter('Result1000kmer21.xlsx', engine='xlsxwriter')
df21_2.to_excel(writer7, sheet_name = 'Sheet1')
df21_3.to_excel(writer7, sheet_name = 'Sheet2')
df21_4.to_excel(writer7, sheet_name = 'Sheet3')
df21_5.to_excel(writer7, sheet_name = 'Sheet4')
df21_6.to_excel(writer7, sheet_name = 'Sheet5')
df21_7.to_excel(writer7, sheet_name = 'Sheet6')
df21_8.to_excel(writer7, sheet_name = 'Sheet7')
df21_9.to_excel(writer7, sheet_name = 'Sheet8')
df21_10.to_excel(writer7, sheet_name = 'Sheet9')
df21_11.to_excel(writer7, sheet_name = 'Sheet10')
df21_12.to_excel(writer7, sheet_name = 'Sheet11')
df21_13.to_excel(writer7, sheet_name = 'Sheet12')
df21_14.to_excel(writer7, sheet_name = 'Sheet13')
df21_15.to_excel(writer7, sheet_name = 'Sheet14')
df21_16.to_excel(writer7, sheet_name = 'Sheet15')
df21_17.to_excel(writer7, sheet_name = 'Sheet16')
df21_18.to_excel(writer7, sheet_name = 'Sheet17')
df21_19.to_excel(writer7, sheet_name = 'Sheet18')
df21_20.to_excel(writer7, sheet_name = 'Sheet19')
writer7.save()


writer8 = pd.ExcelWriter('Result1000kmer23.xlsx', engine='xlsxwriter')
df23_2.to_excel(writer8, sheet_name = 'Sheet1')
df23_3.to_excel(writer8, sheet_name = 'Sheet2')
df23_4.to_excel(writer8, sheet_name = 'Sheet3')
df23_5.to_excel(writer8, sheet_name = 'Sheet4')
df23_6.to_excel(writer8, sheet_name = 'Sheet5')
df23_7.to_excel(writer8, sheet_name = 'Sheet6')
df23_8.to_excel(writer8, sheet_name = 'Sheet7')
df23_9.to_excel(writer8, sheet_name = 'Sheet8')
df23_10.to_excel(writer8, sheet_name = 'Sheet9')
df23_11.to_excel(writer8, sheet_name = 'Sheet10')
df23_12.to_excel(writer8, sheet_name = 'Sheet11')
df23_13.to_excel(writer8, sheet_name = 'Sheet12')
df23_14.to_excel(writer8, sheet_name = 'Sheet13')
df23_15.to_excel(writer8, sheet_name = 'Sheet14')
df23_16.to_excel(writer8, sheet_name = 'Sheet15')
df23_17.to_excel(writer8, sheet_name = 'Sheet16')
df23_18.to_excel(writer8, sheet_name = 'Sheet17')
df23_19.to_excel(writer8, sheet_name = 'Sheet18')
df23_20.to_excel(writer8, sheet_name = 'Sheet19')
df23_21.to_excel(writer8, sheet_name = 'Sheet20')
df23_22.to_excel(writer8, sheet_name = 'Sheet21')
writer8.save()


writer9 = pd.ExcelWriter('Result1000kmer27.xlsx', engine='xlsxwriter')
df27_2.to_excel(writer9, sheet_name = 'Sheet1')
df27_3.to_excel(writer9, sheet_name = 'Sheet2')
df27_4.to_excel(writer9, sheet_name = 'Sheet3')
df27_5.to_excel(writer9, sheet_name = 'Sheet4')
df27_6.to_excel(writer9, sheet_name = 'Sheet5')
df27_7.to_excel(writer9, sheet_name = 'Sheet6')
df27_8.to_excel(writer9, sheet_name = 'Sheet7')
df27_9.to_excel(writer9, sheet_name = 'Sheet8')
df27_10.to_excel(writer9, sheet_name = 'Sheet9')
df27_11.to_excel(writer9, sheet_name = 'Sheet10')
df27_12.to_excel(writer9, sheet_name = 'Sheet11')
df27_13.to_excel(writer9, sheet_name = 'Sheet12')
df27_14.to_excel(writer9, sheet_name = 'Sheet13')
df27_15.to_excel(writer9, sheet_name = 'Sheet14')
df27_16.to_excel(writer9, sheet_name = 'Sheet15')
df27_17.to_excel(writer9, sheet_name = 'Sheet16')
df27_18.to_excel(writer9, sheet_name = 'Sheet17')
df27_19.to_excel(writer9, sheet_name = 'Sheet18')
df27_20.to_excel(writer9, sheet_name = 'Sheet19')
df27_21.to_excel(writer9, sheet_name = 'Sheet20')
df27_22.to_excel(writer9, sheet_name = 'Sheet21')
df27_23.to_excel(writer9, sheet_name = 'Sheet22')
df27_24.to_excel(writer9, sheet_name = 'Sheet23')
df27_25.to_excel(writer9, sheet_name = 'Sheet24')
df27_26.to_excel(writer9, sheet_name = 'Sheet25')
writer9.save()


writer10 = pd.ExcelWriter('Result1000kmer29.xlsx', engine='xlsxwriter')
df29_2.to_excel(writer10, sheet_name = 'Sheet1') 
df29_3.to_excel(writer10, sheet_name = 'Sheet2') 
df29_4.to_excel(writer10, sheet_name = 'Sheet3') 
df29_5.to_excel(writer10, sheet_name = 'Sheet4') 
df29_6.to_excel(writer10, sheet_name = 'Sheet5') 
df29_7.to_excel(writer10, sheet_name = 'Sheet6') 
df29_8.to_excel(writer10, sheet_name = 'Sheet7') 
df29_9.to_excel(writer10, sheet_name = 'Sheet8') 
df29_10.to_excel(writer10, sheet_name = 'Sheet9') 
df29_11.to_excel(writer10, sheet_name = 'Sheet10') 
df29_12.to_excel(writer10, sheet_name = 'Sheet11') 
df29_13.to_excel(writer10, sheet_name = 'Sheet12') 
df29_14.to_excel(writer10, sheet_name = 'Sheet13') 
df29_15.to_excel(writer10, sheet_name = 'Sheet14') 
df29_16.to_excel(writer10, sheet_name = 'Sheet15') 
df29_17.to_excel(writer10, sheet_name = 'Sheet16') 
df29_18.to_excel(writer10, sheet_name = 'Sheet17') 
df29_19.to_excel(writer10, sheet_name = 'Sheet18') 
df29_20.to_excel(writer10, sheet_name = 'Sheet19') 
df29_21.to_excel(writer10, sheet_name = 'Sheet20') 
df29_22.to_excel(writer10, sheet_name = 'Sheet21') 
df29_23.to_excel(writer10, sheet_name = 'Sheet22') 
df29_24.to_excel(writer10, sheet_name = 'Sheet23') 
df29_25.to_excel(writer10, sheet_name = 'Sheet24') 
df29_26.to_excel(writer10, sheet_name = 'Sheet25') 
df29_27.to_excel(writer10, sheet_name = 'Sheet26')   
df29_28.to_excel(writer10, sheet_name = 'Sheet27') 
writer10.save()
   
    