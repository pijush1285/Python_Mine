# -*- coding: utf-8 -*-
"""
Created on Thu May 26 09:29:19 2022

@author: PIJHUSH
FileOperation 4 this code is developed for the server virsion.

>Creating a virtual environment
$ virtualenv -p python3 myenv
>Activating and deactivating a virtualenv
$ source myenv/bin/activate
(myenv)$ which python
>Installing packages
$ source myenv/bin/activate
(myenv)$ pip install bx-python
>To deactivate (return to the global-only context), just run: deactivate
>New pip install in this environment: when use make the below two lines into a single line: 
/home/dasp5/dataset/RandomSimulated/1.st_100_simulated/LengthAuto_1/FileOperation_1/
myenv/bin/python -m pip install --upgrade pip

#pip install pandas
#pip install syspath
#pip install mpmath
#pip install scipy
#pip install openpyxl

# In the server open a blank page by using nano.
After that pest all the code below and save the file name Script.py.
After that use the code given below to run the script:
    $python ./Script.py

"""

import pandas as pd
import sys
sys.path.append('/home/dasp5/dataset/RandomSimulated/1.st_100_simulated/LengthAuto_1/FileOperation_1/submer-central-limit-theorem/modules')
#from argparse import ArgumentParser, RawTextHelpFormatter
import jls_submer_clt_mgr
from jls_submer_to_interval_util import to_length_interval



# For loop utilization for all files
count = 1
for xx in range(100):
    filename="/home/dasp5/dataset/RandomSimulated/3.rd_100_simulated/LengthAuto_3/Results_RGID_"+str(count)+".txt"
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    len(Lines)
    print(filename)   
    # Define a data frame where the selected data Will be kept.
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
            #filename = per_word[6].split('/')[5] # Need to be collected 'RGID_1.fasta'
            filename = per_word[6].split('/')[6] # Need to be collected 'RGID_1.fasta'
            # Getting the Third line
            s = Lines[i+2]
            Third_word = s.split() 
            
            count_of_submers = int(Third_word[2])
            confidence = 0.95
            alpha_0 = 1.0 - confidence # for consistency with z-score
            #is_estimate = 'qualitative'
            k = int(M_mer)
            s = int(s_mer)
            try:
                h = jls_submer_clt_mgr.to_syncmer_closed_Wilson_score_intervals_for_length( count_of_submers, alpha_0, k, s) #, is_estimate 
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
        #df.to_excel("./FileOperationResults_"+str(count)+".xlsx") 
        df.to_csv("./FileOperationResults_"+str(count)+".txt") 
    count = count + 1
