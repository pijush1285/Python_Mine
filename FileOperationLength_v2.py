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
df5_2  = pd.DataFrame()  
df5_3  = pd.DataFrame() 
df5_4  = pd.DataFrame() 

df10_2 = pd.DataFrame() 
df10_3 = pd.DataFrame() 
df10_4 = pd.DataFrame() 
df10_5 = pd.DataFrame() 
df10_6 = pd.DataFrame() 
df10_7 = pd.DataFrame() 
df10_8 = pd.DataFrame() 
df10_9 = pd.DataFrame() 


df15_2 = pd.DataFrame()
df15_3 = pd.DataFrame()
df15_4 = pd.DataFrame()
df15_5 = pd.DataFrame()
df15_6 = pd.DataFrame()
df15_7 = pd.DataFrame()
df15_8 = pd.DataFrame()
df15_9 = pd.DataFrame()
df15_10 = pd.DataFrame()
df15_11 = pd.DataFrame()
df15_12 = pd.DataFrame()
df15_13 = pd.DataFrame()
df15_14 = pd.DataFrame()


df20_2 = pd.DataFrame()
df20_3 = pd.DataFrame()
df20_4 = pd.DataFrame()
df20_5 = pd.DataFrame()
df20_6 = pd.DataFrame()
df20_7 = pd.DataFrame()
df20_8 = pd.DataFrame()
df20_9 = pd.DataFrame()
df20_10 = pd.DataFrame()
df20_11 = pd.DataFrame()
df20_12 = pd.DataFrame()
df20_13 = pd.DataFrame()
df20_14 = pd.DataFrame()
df20_15 = pd.DataFrame()
df20_16 = pd.DataFrame()
df20_17 = pd.DataFrame()
df20_18 = pd.DataFrame()
df20_19 = pd.DataFrame()


df25_2 = pd.DataFrame()
df25_3 = pd.DataFrame()
df25_4 = pd.DataFrame()
df25_5 = pd.DataFrame()
df25_6 = pd.DataFrame()
df25_7 = pd.DataFrame()
df25_8 = pd.DataFrame()
df25_9 = pd.DataFrame()
df25_10 = pd.DataFrame()
df25_11 = pd.DataFrame()
df25_12 = pd.DataFrame()
df25_13 = pd.DataFrame()
df25_14 = pd.DataFrame()
df25_15 = pd.DataFrame()
df25_16 = pd.DataFrame()
df25_17 = pd.DataFrame()
df25_18 = pd.DataFrame()
df25_19 = pd.DataFrame()
df25_20 = pd.DataFrame()
df25_21 = pd.DataFrame()
df25_22 = pd.DataFrame()
df25_23 = pd.DataFrame()
df25_24 = pd.DataFrame()


df30_2 = pd.DataFrame()
df30_3 = pd.DataFrame()
df30_4 = pd.DataFrame()
df30_5 = pd.DataFrame()
df30_6 = pd.DataFrame()
df30_7 = pd.DataFrame()
df30_8 = pd.DataFrame()
df30_9 = pd.DataFrame()
df30_10 = pd.DataFrame()
df30_11 = pd.DataFrame()
df30_12 = pd.DataFrame()
df30_13 = pd.DataFrame()
df30_14 = pd.DataFrame()
df30_15 = pd.DataFrame()
df30_16 = pd.DataFrame()
df30_17 = pd.DataFrame()
df30_18 = pd.DataFrame()
df30_19 = pd.DataFrame()
df30_20 = pd.DataFrame()
df30_21 = pd.DataFrame()
df30_22 = pd.DataFrame()
df30_23 = pd.DataFrame()
df30_24 = pd.DataFrame()
df30_25 = pd.DataFrame()
df30_26 = pd.DataFrame()
df30_27 = pd.DataFrame()
df30_28 = pd.DataFrame()
df30_29 = pd.DataFrame()




#For loop
count = 1
for xx in range(100):
   # filename="C:/Users/dasp5.NCBI_NT/Desktop/Out/OperationOnLength/1.st_100_simulatedTxt/FileOperationResults_"+str(count)+".txt"
   # filename="C:/Users/dasp5.NCBI_NT/Desktop/Out/OperationOnLength/2.nd_100_simulated/FileOperationResults_"+str(count)+".txt"
   # filename="C:/Users/dasp5.NCBI_NT/Desktop/Out/OperationOnLength/3.rd_100_simulated/FileOperationResults_"+str(count)+".txt"
   # filename="C:/Users/dasp5.NCBI_NT/Desktop/Out/OperationOnLength/4.th_100_simulated/FileOperationResults_"+str(count)+".txt"
   # filename="C:/Users/dasp5.NCBI_NT/Desktop/Out/OperationOnLength/5.th_100_simulated/FileOperationResults_"+str(count)+".txt"
   # filename="C:/Users/dasp5.NCBI_NT/Desktop/Out/OperationOnLength/6.th_100_simulated/FileOperationResults_"+str(count)+".txt"
   # filename="C:/Users/dasp5.NCBI_NT/Desktop/Out/OperationOnLength/7.th_100_simulated/FileOperationResults_"+str(count)+".txt"
   # filename="C:/Users/dasp5.NCBI_NT/Desktop/Out/OperationOnLength/8.th_100_simulated/FileOperationResults_"+str(count)+".txt"
   # filename="C:/Users/dasp5.NCBI_NT/Desktop/Out/OperationOnLength/9.th_100_simulated/FileOperationResults_"+str(count)+".txt"
    filename="C:/Users/dasp5.NCBI_NT/Desktop/Out/OperationOnLength/10.th_100_simulated/FileOperationResults_"+str(count)+".txt"
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    #len(Lines)
    #print(filename)
    
    df5_2a  =  [Lines[1]]                      
    df5_2   =  df5_2.append(df5_2a, ignore_index=True)
    df5_3a  =  [Lines[2]]
    df5_3   =  df5_3.append(df5_3a, ignore_index=True)
    df5_4a  =  [Lines[3]] 
    df5_4   =  df5_4.append(df5_4a, ignore_index=True)
    
    df10_2a =  [Lines[4]] 
    df10_2  =  df10_2.append(df10_2a, ignore_index=True)
    df10_3a =  [Lines[5]] 
    df10_3  =  df10_3.append(df10_3a, ignore_index=True)
    df10_4a =  [Lines[6]] 
    df10_4  =  df10_4.append(df10_4a, ignore_index=True)
    df10_5a =  [Lines[7]]  
    df10_5  =  df10_5.append(df10_5a, ignore_index=True)
    df10_6a =  [Lines[8]] 
    df10_6  =  df10_6.append(df10_6a, ignore_index=True)
    df10_7a =  [Lines[9]] 
    df10_7  =  df10_7.append(df10_7a, ignore_index=True)
    df10_8a =  [Lines[10]] 
    df10_8  =  df10_8.append(df10_8a, ignore_index=True)
    df10_9a =  [Lines[11]] 
    df10_9  =  df10_9.append(df10_9a, ignore_index=True)
    
    df15_2a = [Lines[12]] 
    df15_2  = df15_2.append(df15_2a, ignore_index=True)
    df15_3a = [Lines[13]] 
    df15_3  = df15_3.append(df15_3a, ignore_index=True)
    df15_4a = [Lines[14]] 
    df15_4  = df15_4.append(df15_4a, ignore_index=True)
    df15_5a = [Lines[15]] 
    df15_5  = df15_5.append(df15_5a, ignore_index=True)
    df15_6a = [Lines[16]]
    df15_6  = df15_6.append(df15_6a, ignore_index=True)
    df15_7a = [Lines[17]] 
    df15_7  = df15_7.append(df15_7a, ignore_index=True)
    df15_8a = [Lines[18]] 
    df15_8  = df15_8.append(df15_8a, ignore_index=True)
    df15_9a = [Lines[19]] 
    df15_9  = df15_9.append(df15_9a, ignore_index=True)
    df15_10a = [Lines[20]] 
    df15_10  = df15_10.append(df15_10a, ignore_index=True)
    df15_11a = [Lines[21]] 
    df15_11  = df15_11.append(df15_11a, ignore_index=True)
    df15_12a = [Lines[22]] 
    df15_12  = df15_12.append(df15_12a, ignore_index=True)
    df15_13a = [Lines[23]] 
    df15_13  = df15_13.append(df15_13a, ignore_index=True)
    df15_14a = [Lines[24]] 
    df15_14  = df15_14.append(df15_14a, ignore_index=True) 
    
    df20_2a  = [Lines[25]] 
    df20_2   = df20_2.append(df20_2a, ignore_index=True)
    df20_3a  = [Lines[26]] 
    df20_3   = df20_3.append(df20_3a, ignore_index=True)
    df20_4a  = [Lines[27]] 
    df20_4   = df20_4.append(df20_4a, ignore_index=True)
    df20_5a  = [Lines[28]] 
    df20_5   = df20_5.append(df20_5a, ignore_index=True)
    df20_6a  = [Lines[29]] 
    df20_6   = df20_6.append(df20_6a, ignore_index=True)
    df20_7a  = [Lines[30]] 
    df20_7   = df20_7.append(df20_7a, ignore_index=True)
    df20_8a  = [Lines[31]] 
    df20_8   = df20_8.append(df20_8a, ignore_index=True)
    df20_9a  = [Lines[32]] 
    df20_9   = df20_9.append(df20_9a, ignore_index=True)
    df20_10a = [Lines[33]] 
    df20_10  = df20_10.append(df20_10a, ignore_index=True)
    df20_11a = [Lines[34]] 
    df20_11  = df20_11.append(df20_11a, ignore_index=True)
    df20_12a = [Lines[35]] 
    df20_12  = df20_12.append(df20_12a, ignore_index=True)
    df20_13a = [Lines[36]] 
    df20_13  = df20_13.append(df20_13a, ignore_index=True)
    df20_14a = [Lines[37]] 
    df20_14  = df20_14.append(df20_14a, ignore_index=True)
    df20_15a = [Lines[38]] 
    df20_15  = df20_15.append(df20_15a, ignore_index=True)
    df20_16a = [Lines[39]] 
    df20_16  = df20_16.append(df20_16a, ignore_index=True)
    df20_17a = [Lines[40]] 
    df20_17  = df20_17.append(df20_17a, ignore_index=True)
    df20_18a = [Lines[41]] 
    df20_18  = df20_18.append(df20_18a, ignore_index=True)
    df20_19a = [Lines[42]] 
    df20_19  = df20_19.append(df20_19a, ignore_index=True)
    
    
    df25_2a =  [Lines[43]]
    df25_2  =  df25_2.append(df25_2a, ignore_index=True)
    df25_3a =  [Lines[44]]
    df25_3  =  df25_3.append(df25_3a, ignore_index=True)
    df25_4a =  [Lines[45]]
    df25_4  =  df25_4.append(df25_4a, ignore_index=True)
    df25_5a =  [Lines[46]]
    df25_5  =  df25_5.append(df25_5a, ignore_index=True)
    df25_6a =  [Lines[47]]
    df25_6  =  df25_6.append(df25_6a, ignore_index=True)
    df25_7a =  [Lines[48]]
    df25_7  =  df25_7.append(df25_7a, ignore_index=True)
    df25_8a =  [Lines[49]]
    df25_8  =  df25_8.append(df25_8a, ignore_index=True)
    df25_9a =  [Lines[50]]
    df25_9  =  df25_9.append(df25_9a, ignore_index=True)
    df25_10a = [Lines[51]]
    df25_10  = df25_10.append(df25_10a, ignore_index=True)
    df25_11a = [Lines[52]] 
    df25_11  = df25_11.append(df25_11a, ignore_index=True)
    df25_12a = [Lines[53]]
    df25_12  = df25_12.append(df25_12a, ignore_index=True)
    df25_13a = [Lines[54]]
    df25_13  = df25_13.append(df25_13a, ignore_index=True)
    df25_14a = [Lines[55]]
    df25_14  = df25_14.append(df25_14a, ignore_index=True)
    df25_15a = [Lines[56]]
    df25_15  = df25_15.append(df25_15a, ignore_index=True)
    df25_16a = [Lines[57]]
    df25_16  = df25_16.append(df25_16a, ignore_index=True)
    df25_17a = [Lines[58]] 
    df25_17  = df25_17.append(df25_17a, ignore_index=True)
    df25_18a = [Lines[59]]
    df25_18  = df25_18.append(df25_18a, ignore_index=True)
    df25_19a = [Lines[60]]
    df25_19  = df25_19.append(df25_19a, ignore_index=True)
    df25_20a = [Lines[61]]
    df25_20  = df25_20.append(df25_20a, ignore_index=True)
    df25_21a = [Lines[62]]
    df25_21  = df25_21.append(df25_21a, ignore_index=True)
    df25_22a = [Lines[63]]
    df25_22  = df25_22.append(df25_22a, ignore_index=True)
    df25_23a = [Lines[64]]
    df25_23  = df25_23.append(df25_23a, ignore_index=True)
    df25_24a = [Lines[65]]
    df25_24  = df25_24.append(df25_24a, ignore_index=True)
    
    
    df30_2a =  [Lines[66]]
    df30_2  =  df30_2.append(df30_2a, ignore_index=True)
    df30_3a =  [Lines[67]]
    df30_3  =  df30_3.append(df30_3a, ignore_index=True)
    df30_4a =  [Lines[68]] 
    df30_4  =  df30_4.append(df30_4a, ignore_index=True)
    df30_5a =  [Lines[69]] 
    df30_5  =  df30_5.append(df30_5a, ignore_index=True)
    df30_6a =  [Lines[70]] 
    df30_6  =  df30_6.append(df30_6a, ignore_index=True)
    df30_7a =  [Lines[71]]
    df30_7  =  df30_7.append(df30_7a, ignore_index=True)
    df30_8a =  [Lines[72]] 
    df30_8  =  df30_8.append(df30_8a, ignore_index=True)
    df30_9a =  [Lines[73]]
    df30_9  =  df30_9.append(df30_9a, ignore_index=True)
    df30_10a = [Lines[74]]
    df30_10  = df30_10.append(df30_10a, ignore_index=True)
    df30_11a = [Lines[75]]
    df30_11  = df30_11.append(df30_11a, ignore_index=True)
    df30_12a = [Lines[76]]
    df30_12  = df30_12.append(df30_12a, ignore_index=True)
    df30_13a = [Lines[77]]
    df30_13  = df30_13.append(df30_13a, ignore_index=True)
    df30_14a = [Lines[78]]
    df30_14  = df30_14.append(df30_14a, ignore_index=True)
    df30_15a = [Lines[79]]
    df30_15  = df30_15.append(df30_15a, ignore_index=True)
    df30_16a = [Lines[80]]
    df30_16  = df30_16.append(df30_16a, ignore_index=True)
    df30_17a = [Lines[81]]
    df30_17  = df30_17.append(df30_17a, ignore_index=True)
    df30_18a = [Lines[82]]
    df30_18  = df30_18.append(df30_18a, ignore_index=True)
    df30_19a = [Lines[83]] 
    df30_19  = df30_19.append(df30_19a, ignore_index=True)
    df30_20a = [Lines[84]]
    df30_20  = df30_20.append(df30_20a, ignore_index=True)
    df30_21a = [Lines[85]]
    df30_21  = df30_21.append(df30_21a, ignore_index=True)
    df30_22a = [Lines[86]]
    df30_22  = df30_22.append(df30_22a, ignore_index=True)
    df30_23a = [Lines[87]]
    df30_23  = df30_23.append(df30_23a, ignore_index=True)
    df30_24a = [Lines[88]]
    df30_24  = df30_24.append(df30_24a, ignore_index=True)
    df30_25a = [Lines[89]]
    df30_25  = df30_25.append(df30_25a, ignore_index=True)
    df30_26a = [Lines[90]]
    df30_26  = df30_26.append(df30_26a, ignore_index=True)
    df30_27a = [Lines[91]] 
    df30_27  = df30_27.append(df30_27a, ignore_index=True)
    df30_28a = [Lines[92]]
    df30_28  = df30_28.append(df30_28a, ignore_index=True)
    df30_29a = [Lines[93]] 
    df30_29  = df30_29.append(df30_29a, ignore_index=True)
    count = count + 1
    
    

   
    
#Write all records
#cd C:\Users\dasp5.NCBI_NT\Desktop\Out\OperationOnLength\ProcessedOnText_v1

writer = pd.ExcelWriter('Result1st100kmer5.xlsx', engine='xlsxwriter')
df5_2.to_excel(writer, sheet_name='Sheet1')
df5_3.to_excel(writer, sheet_name='Sheet2')
df5_4.to_excel(writer, sheet_name='Sheet3')
writer.save()


writer1 = pd.ExcelWriter('Result1st100kmer10.xlsx', engine='xlsxwriter')
df10_2.to_excel(writer1, sheet_name='Sheet1')
df10_3.to_excel(writer1, sheet_name='Sheet2')
df10_4.to_excel(writer1, sheet_name='Sheet3')
df10_5.to_excel(writer1, sheet_name='Sheet4')
df10_6.to_excel(writer1, sheet_name='Sheet5')
df10_7.to_excel(writer1, sheet_name='Sheet6')
df10_8.to_excel(writer1, sheet_name='Sheet7')
df10_9.to_excel(writer1, sheet_name='Sheet8')
writer1.save()



writer2 = pd.ExcelWriter('Result1st100kmer15.xlsx', engine='xlsxwriter')
df15_2.to_excel(writer2, sheet_name='Sheet1')
df15_3.to_excel(writer2, sheet_name='Sheet2')
df15_4.to_excel(writer2, sheet_name='Sheet3')
df15_5.to_excel(writer2, sheet_name='Sheet4')
df15_6.to_excel(writer2, sheet_name='Sheet5')
df15_7.to_excel(writer2, sheet_name='Sheet6')
df15_8.to_excel(writer2, sheet_name='Sheet7')
df15_9.to_excel(writer2, sheet_name='Sheet8')
df15_10.to_excel(writer2, sheet_name='Sheet9')
df15_11.to_excel(writer2, sheet_name='Sheet10')
df15_12.to_excel(writer2, sheet_name='Sheet11')
df15_13.to_excel(writer2, sheet_name='Sheet12')
df15_14.to_excel(writer2, sheet_name='Sheet13')
writer2.save()


writer3 = pd.ExcelWriter('Result1st100kmer20.xlsx', engine='xlsxwriter')
df20_2.to_excel(writer3, sheet_name = 'Sheet1')
df20_3.to_excel(writer3, sheet_name = 'Sheet2')
df20_4.to_excel(writer3, sheet_name = 'Sheet3')
df20_5.to_excel(writer3, sheet_name = 'Sheet4')
df20_6.to_excel(writer3, sheet_name = 'Sheet5')
df20_7.to_excel(writer3, sheet_name = 'Sheet6')
df20_8.to_excel(writer3, sheet_name = 'Sheet7')
df20_9.to_excel(writer3, sheet_name = 'Sheet8')
df20_10.to_excel(writer3, sheet_name = 'Sheet9')
df20_11.to_excel(writer3, sheet_name = 'Sheet10')
df20_12.to_excel(writer3, sheet_name = 'Sheet11')
df20_13.to_excel(writer3, sheet_name = 'Sheet12')
df20_14.to_excel(writer3, sheet_name = 'Sheet13')
df20_15.to_excel(writer3, sheet_name = 'Sheet14')
df20_16.to_excel(writer3, sheet_name = 'Sheet15')
df20_17.to_excel(writer3, sheet_name = 'Sheet16')
df20_18.to_excel(writer3, sheet_name = 'Sheet17')
df20_19.to_excel(writer3, sheet_name = 'Sheet18')
writer3.save()



writer4 = pd.ExcelWriter('Result1st100kmer25.xlsx', engine='xlsxwriter')
df25_2.to_excel(writer4, sheet_name = 'Sheet1')
df25_3.to_excel(writer4, sheet_name = 'Sheet2')
df25_4.to_excel(writer4, sheet_name = 'Sheet3')
df25_5.to_excel(writer4, sheet_name = 'Sheet4')
df25_6.to_excel(writer4, sheet_name = 'Sheet5')
df25_7.to_excel(writer4, sheet_name = 'Sheet6')
df25_8.to_excel(writer4, sheet_name = 'Sheet7')
df25_9.to_excel(writer4, sheet_name = 'Sheet8')
df25_10.to_excel(writer4, sheet_name = 'Sheet9')
df25_11.to_excel(writer4, sheet_name = 'Sheet10')
df25_12.to_excel(writer4, sheet_name = 'Sheet11')
df25_13.to_excel(writer4, sheet_name = 'Sheet12')
df25_14.to_excel(writer4, sheet_name = 'Sheet13')
df25_15.to_excel(writer4, sheet_name = 'Sheet14')
df25_16.to_excel(writer4, sheet_name = 'Sheet15')
df25_17.to_excel(writer4, sheet_name = 'Sheet16')
df25_18.to_excel(writer4, sheet_name = 'Sheet17')
df25_19.to_excel(writer4, sheet_name = 'Sheet18')
df25_20.to_excel(writer4, sheet_name = 'Sheet19')
df25_21.to_excel(writer4, sheet_name = 'Sheet20')
df25_22.to_excel(writer4, sheet_name = 'Sheet21')
df25_23.to_excel(writer4, sheet_name = 'Sheet22')
df25_24.to_excel(writer4, sheet_name = 'Sheet23')
writer4.save()


writer5 = pd.ExcelWriter('Result1st100kmer30.xlsx', engine='xlsxwriter')
df30_2.to_excel(writer5, sheet_name = 'Sheet1') 
df30_3.to_excel(writer5, sheet_name = 'Sheet2') 
df30_4.to_excel(writer5, sheet_name = 'Sheet3') 
df30_5.to_excel(writer5, sheet_name = 'Sheet4') 
df30_6.to_excel(writer5, sheet_name = 'Sheet5') 
df30_7.to_excel(writer5, sheet_name = 'Sheet6') 
df30_8.to_excel(writer5, sheet_name = 'Sheet7') 
df30_9.to_excel(writer5, sheet_name = 'Sheet8') 
df30_10.to_excel(writer5, sheet_name = 'Sheet9') 
df30_11.to_excel(writer5, sheet_name = 'Sheet10') 
df30_12.to_excel(writer5, sheet_name = 'Sheet11') 
df30_13.to_excel(writer5, sheet_name = 'Sheet12') 
df30_14.to_excel(writer5, sheet_name = 'Sheet13') 
df30_15.to_excel(writer5, sheet_name = 'Sheet14') 
df30_16.to_excel(writer5, sheet_name = 'Sheet15') 
df30_17.to_excel(writer5, sheet_name = 'Sheet16') 
df30_18.to_excel(writer5, sheet_name = 'Sheet17') 
df30_19.to_excel(writer5, sheet_name = 'Sheet18') 
df30_20.to_excel(writer5, sheet_name = 'Sheet19') 
df30_21.to_excel(writer5, sheet_name = 'Sheet20') 
df30_22.to_excel(writer5, sheet_name = 'Sheet21') 
df30_23.to_excel(writer5, sheet_name = 'Sheet22') 
df30_24.to_excel(writer5, sheet_name = 'Sheet23') 
df30_25.to_excel(writer5, sheet_name = 'Sheet24') 
df30_26.to_excel(writer5, sheet_name = 'Sheet25') 
df30_27.to_excel(writer5, sheet_name = 'Sheet26')   
df30_28.to_excel(writer5, sheet_name = 'Sheet27') 
df30_29.to_excel(writer5, sheet_name = 'Sheet28') 
writer5.save()

   
    