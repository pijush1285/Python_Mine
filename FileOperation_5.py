# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 20:12:24 2022


This program is developed because John has updated his package.
The package is downloaded on 12.10.2022.

@author: PIJHUSH
"""



import pandas as pd
import sys
#sys.path.append('C:/Users/PIJHUSH/Desktop/John/Codes/submer-central-limit-theorem-main-12.10.2022/programs')
#from argparse import ArgumentParser, RawTextHelpFormatter
#import jls_submer_clt_mgr
#from jls_submer_to_interval_util import to_length_interval



sys.path.insert(0,"C:/Users/PIJHUSH/Desktop/John/Codes/submer-central-limit-theorem-main-12.10.2022/modules")

#from argparse import ArgumentParser, RawTextHelpFormatter
from jls_submer_clt_mgr import to_syncmer_parametrized_Wilson_score_intervals_for_length
from jls_submer_to_interval_util import to_length_interval



        
# Using readlines()
#filename="C:/Users/PIJHUSH/Desktop/sheared/Simulated300/RandomeSimulated/Results_RGID_1.txt"
filename="C:/Users/PIJHUSH/Desktop/sheared/Simulated300/RandomeSimulated/1.st_100_simulated/Results_RGID_1.txt"
file1 = open(filename, 'r')
Lines = file1.readlines()
len(Lines)
  
# Define a data frame where the selected data eill be kept.
df = pd.DataFrame()


for x in range(len(Lines)):
    # Get a particular line 
    i=x
    #p = Lines[0]
    p = Lines[i]
    per_word = p.split()
    if per_word[1] == 'dna-seed-sim':
        print("Matched:", i)
        m_mer = per_word[2].split('m')[1]
        M_mer = per_word[3].split('M')[1]
        window = per_word[4].split('=')[1]
        s_mer = per_word[5].split('s')[1]
        filename = per_word[6].split('/')[6] # Need to be collected 'RGID_1.fasta'
        # Getting the Third line
        s = Lines[i+2]
        Third_word = s.split() 
        
               
        count_of_submers = int(Third_word[2])
        confidence = 0.95
        alpha_0 = 1.0 - confidence # for consistency with z-score
        #is_approximation = False
        k = int(M_mer)
        s = int(s_mer)
        ts = [0, k-s]
        eps = 0.0
        
        
        
        try:
            h = to_syncmer_parametrized_Wilson_score_intervals_for_length( count_of_submers, alpha_0, k, s, ts, eps ) #, is_approximation , is_estimate 
            interval = to_length_interval( h )
        except:
            interval = [None, None]
        
        
        df1 = pd.DataFrame({'k-mer' : [M_mer],
                       'syn-window' : [window],
                       's': [s_mer],
                       'seed' : [Third_word[2]],
                       'LengthLow' : interval[0],
                       'LengthHigh' : interval[1],
                       'filename': [filename]})
        df = df.append(df1, ignore_index=True)
    else:
        print("unmatched:", i)
        
        
       


file1.close()

df.to_csv("./FileOperationResults_1.txt") 
df.to_excel('./Results1.xlsx')