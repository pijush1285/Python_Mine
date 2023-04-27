# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 11:33:07 2022

@author: PIJHUSH
"""

# importing panda library
import pandas as pd
import os
  
# readinag given csv file
# and creating dataframe
#dataframe1 = pd.read_csv("MMseed0.01_20.txt")
#dataframe1.to_csv('MMseed0.01_20.csv', index = None)



#path = 'C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.1/MininizerSeed'
path = 'C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.2/MininizerSeed'

i = 1
for filename in os.listdir(path):
  #os.rename(path+'/'+filename, path+'/captured'+str(i)+'.jpg')
  dataframe1 = pd.read_csv(path+'/'+filename)
  dataframe1.to_csv(path+'/'+'MMseed0.2_'+str(i)+'.csv', index = None)
  i = i + 1
  
  
  
  