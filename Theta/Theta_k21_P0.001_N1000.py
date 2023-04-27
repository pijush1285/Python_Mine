"""
# First of all activate the python environment.
cd /home/dasp5/dataset/RandomSimulated
source myenv/bin/activate
# Next copy the code and named as  Theta_k21_P0.001_N1000.py
$python ./Theta_k21_P0.001_N1000.py
"""


import pandas as pd
import sys
# This path is used for server.
sys.path.append('/home/dasp5/dataset/RandomSimulated/1.st_100_simulated/LengthAuto_1/FileOperation_1/submer-central-limit-theorem/modules')
# This path will be used for local machine.
#sys.path.append('C:/Users/PIJHUSH/Desktop/John/Codes/main')
from argparse import ArgumentParser, RawTextHelpFormatter
import jls_submer_clt_mgr
from jls_submer_to_interval_util import to_theta_interval


# Define a data frame where the selected data Will be kept.
df = pd.DataFrame()  

#For loop
count = 1
for xx in range(1000):
    #Raw Seed file read.
    RawSeed = pd.read_csv("/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k/seeds/seed_21/Raw_seed/RawSeed_"+str(count)+".csv",header=1, sep='\t') 
    # Mutated file read.
    MutSeed = pd.read_csv("/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k/seeds/seed_21/Mut_0.001_seed/Mut_0.001Seed_"+str(count)+".csv",header=1,sep='\t')
    # Find out the common sequence between raw and mutated sequence file.
    # This is the number of the mutated file's sequence that does not include the mutation.
    df3=pd.merge(RawSeed,MutSeed, how='inner') # This code also can be used.
    #df3=pd.merge(RawSeed['sequence'],MutSeed['sequence'], how='inner')
    count_of_submers = len(MutSeed) # NUMBER_OF_SUBMERS
    count_of_unmutated_syncmers = len(df3) #NUMBER_OF_UNMUTATED_SUBMERS
    confidence = 0.95
    alpha_0 = 1.0 - confidence # for consistency with z-score
    #length = argument.length
    k = 21
    s = 6 
    try:
        h = jls_submer_clt_mgr.to_syncmer_closed_Wilson_score_intervals_for_theta( count_of_submers, count_of_unmutated_syncmers, alpha_0, k, s) #, length 
        interval = to_theta_interval( h )
    except:
        interval = [None, None]  
    # Catch the process data in a frame.
    df1 = pd.DataFrame({'k-mer' :[k],
               's-mer': [s],
               'Number_of_submer' : [count_of_submers],
               'Number_of_UnmutSubmer' : [count_of_unmutated_syncmers],
               'ThetaLow' : interval[0],
               'ThetaHigh' : interval[1],
               'filename': ["Mut_0.001Seed_"+str(count)+".csv"]})
    df = df.append(df1, ignore_index=True)
    #df = pd.concat(df, df1)
    print("###############Completed###############")
    print(count)
    count = count + 1
    
    
 #Write all records
df.to_excel("./ResultsThetak21P0.001_n1000.xlsx") 
df.to_csv("./ResultsThetak21P0.001_n1000.txt") 
    
    
