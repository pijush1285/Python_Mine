# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 19:21:06 2023

@author: PIJHUSH
"""


import pandas as pd
import subprocess
import csv
import os
import io
import sys

# This path is used for server.
#sys.path.append('/home/dasp5/packages/submer-central-limit-theorem/modules')
# This path will be used for local machine.
sys.path.append('C:/Users/PIJHUSH/Desktop/John/Codes/main')
#from argparse import ArgumentParser, RawTextHelpFormatter
import jls_submer_clt_mgr
from jls_submer_to_interval_util import to_theta_interval



# according the current directory.
kmer = 10
smer = 4
window = 7
t = 5



InputDirectory = 'D:/JohnAllfromNIH/BackupArchive/Table3/1_Dataset_0.1kby1k/'
InputDirectory = 'D:/JohnAllfromNIH/BackupArchive/Table3/5_Dataset_1000kby1k/'





# Relative path to your Python code. This the path for the novolap package.
a_py_path = 'D:/JohnAllfromNIH/BackupArchive/packages/noverlap/bin/dna-seed-sim'
# Package Location inside the server is given below.
#a_py_path = '/home/dasp5/packages/noverlap/bin/dna-seed-sim'



count = 1
input_file_path = InputDirectory+'Raw_Fasta/RGID_' + str(count) + '.fasta'

# Closed Syncmer
result = subprocess.run(['python', a_py_path, '-m'+ str(kmer), '-M'+ str(kmer), 
                         '--syn-window='+ str(window), '-s'+ str(smer), 
                         '--seeds', input_file_path], 
                        capture_output=True, text=True)

# Open Syncmer
result = subprocess.run(['python', a_py_path, '-m'+ str(kmer), '-M'+ str(kmer), 
                         '--syn-window='+ str(window), '-s'+ str(smer), 
                         '--syn-offset='+str(t), '--seeds', input_file_path], 
                        capture_output=True, text=True)

print(result.stdout)



# Open the CSV file for writing
with open(InputDirectory +'RawSeed_'+str(count)+'.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write each line of the output to a separate row in the CSV file
    for line in result.stdout.split('\n'):
            writer.writerow([line])




# Relative path to your input file
input_file_path1 = InputDirectory+'Mutated_0.05/Mutated/Mutated_' + str(count) + '.fasta'


# Closed Syncmer 
result1 = subprocess.run(['python', a_py_path, '-m'+ str(kmer), '-M'+ str(kmer), 
                          '--syn-window='+ str(window), '-s'+ str(smer), 
                           '--seeds', input_file_path1], 
                         capture_output=True, text=True)



# Open Syncmer
result1 = subprocess.run(['python', a_py_path, '-m'+ str(kmer), '-M'+ str(kmer), 
                          '--syn-window='+ str(window), '-s'+ str(smer), 
                          '--syn-offset='+str(t), '--seeds', input_file_path1], 
                         capture_output=True, text=True)

# Print the result to the console
print(result1.stdout)  




with open(InputDirectory +'Mut_0.05Seed_'+str(count)+'.csv', 'w', newline='') as csvfile1:
     writer = csv.writer(csvfile1)
     # Write each line of the output to a separate row in the CSV file
     for line in result1.stdout.split('\n'):
             writer.writerow([line])
             


RawSeed = pd.read_csv(io.StringIO(result.stdout),header=1, sep='\t') 
MutSeed = pd.read_csv(io.StringIO(result1.stdout),header=1, sep='\t') 
 
print(RawSeed)
print(MutSeed)


df3 = pd.merge(RawSeed['sequence'],MutSeed['sequence'], how='inner')
df3 = set(RawSeed['sequence']).intersection(MutSeed['sequence'])

 
 
count_of_submers = len(MutSeed) # NUMBER_OF_SUBMERS
count_of_unmutated_syncmers = len(df3) #NUMBER_OF_UNMUTATED_SUBMERS
confidence = 0.95
alpha_0 = 1.0 - confidence # for consistency with z-score
 #length = argument.length
k = kmer
s = smer


names1 = RawSeed['sequence']
names2 = MutSeed['sequence']

common_names = set(names1).intersection(names2)
len(common_names)



cd D:\JohnAllfromNIH\BackupArchive\packages\submer-central-limit-theorem-010323\programs
ls
run theta-confidence-from-parametrized-syncmer-count.py -h
ls
run theta-confidence-from-parametrized-syncmer-count.py -k 10 -s 3 -t 0 7 -n 100 -u 90 -c 0.95


run theta-confidence-from-parametrized-syncmer-count.py -k 10 -s 2 -t 6 -n 106642 -u 54961 -c 0.95




# Johns old package.
cd C:\Users\PIJHUSH\Desktop\John\Codes\main

run theta-from-closed-syncmer-count.py -h
run theta-from-open-syncmer-count -h

run theta-from-open-syncmer-count -k10 -s2 -t5 -n11 -u5 -c 0.95


run theta-from-closed-syncmer-count.py -k10 -s4 -n 287809 -u 148662 -c 0.95



run theta-from-open-syncmer-count.py -k 10 -s 2 -t5 -n 106642 -u 54961 -c 0.95

run theta-from-open-syncmer-count.py -k 10 -s 2 -t6 -n 140371 -u 72594 -c 0.95

run theta-from-open-syncmer-count.py -k 10 -s 2 -t 6 -n 140693 -u 72457 -c 0.95


