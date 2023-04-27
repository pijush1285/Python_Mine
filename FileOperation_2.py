# -*- coding: utf-8 -*-
"""
Created on Fri May 20 04:23:10 2022

@author: PIJHUSH
"""



        
# Using readlines()
filename="C:/Users/PIJHUSH/Desktop/sheared/Simulated300/RandomeSimulated/Results_RGID_1.txt"
file1 = open(filename, 'r')
Lines = file1.readlines()
  
# Get a particular line 
p = Lines[0]
per_word = p.split()

# Break in to individual charecter
per_word[0]
per_word[1]   # Use ful for checking 'dna-seed-sim'
per_word[2]   # Need to be collected '-m5'
per_word[3]   # Need to be collected '-M5'
per_word[4]   # Need to be collected '--syn-window=4'
per_word[5]   # Need to be collected '-s2'
per_word[6]


m_mer = per_word[2].split('m')[1]
M_mer = per_word[3].split('M')[1]
window = per_word[4].split('=')[1]
s_mer = per_word[5].split('s')[1]
filename = per_word[6].split('/')[5] # Need to be collected 'RGID_1.fasta'


###############################################################################
# This line has no use
# Getting the second line
q = Lines[1]
second_word = q.split()

# Break in to individual charecter
second_word[0]
second_word[1]
second_word[2]
second_word[3]
second_word[4]
second_word[5]
###############################################################################
# Getting the Third line
s = Lines[2]
Third_word = s.split()

Third_word[0]    # Use ful for checking '1'
Third_word[1]
Third_word[2]    # Use ful for checking '1058551'
Third_word[3]
Third_word[4]




file1.close()


###################################################################
import pandas as pd

df = pd.DataFrame({'m' : [0],
                   'M' : [0],
                   'syn-window' : [0],
                   's': [0],
                   'seed' : [0],
                   'filename': ['']})

df1 = pd.DataFrame({'m' : [m_mer],
                   'M' : [M_mer],
                   'syn-window' : [window],
                   's': [s_mer],
                   'seed' : [Third_word[2]],
                   'filename': [filename]})



# Using append() method
df2 = df.append(df1)
print(df2)

df2 = df.append(df1, ignore_index=True)
print(df2)


#############################################################################
import sys
sys.path.append('C:/Users/PIJHUSH/Desktop/John/Codes/main')
#from argparse import ArgumentParser, RawTextHelpFormatter
import jls_submer_clt_mgr
from jls_submer_to_interval_util import to_length_interval


#parser = getArguments()
#argument = parser.parse_args()
#check( argument )  
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
h_output = {}
h_output["sig"] = confidence
h_output["method"] = "qualitative"
if is_estimate: 
    h_output["method"] = "estimate"
h_output["LengthLow"] = interval[0]
h_output["LengthHigh"] = interval[1]
output( h_output )   