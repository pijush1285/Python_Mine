# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
###############################################################################
# This portion will be used for producing randome genome sequence with a define length.

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from random import choice

bases=["A","G","C","T"]

def getsequences(length):
  sequence=""
  for count in range(length):
    sequence+=choice(bases)
  return sequence

# Seed the random number generator with your value
random.seed(31415)
# Now the function is define below. We need to pass the number of file and the 
# Length of the genome sequence.
def RandomSequenceGenerator(number, length):
    count = 1
    for x in range(number):
            len1 = length
            sequence = getsequences(len1)  
            name = "RGID_"+str(count)
            new_id = str(name)
            new_rec = SeqRecord(Seq(sequence),id=new_id, description="new_Seq_0:2M")
            FastaFileName = str(name)+".fasta"
            SeqIO.write(new_rec, FastaFileName,"fasta")
            print("Fasta file generate completed number:", count)
            count = count + 1
            
			
			
# Call the function
RandomSequenceGenerator(1000, 1000)

###############################################################################
# Now it is required to insurt some mutation or error in the sequence.

import os
path='C:/Users/dasp5.NCBI_NT/Desktop/Table2/Packages/mutation-rate-intervals-main'
fasta='RGID_1.fasta'

cd C:/Users/PIJHUSH/Desktop/John/Codes/mutation-rate-intervals-main Package
os.system('type RGID_1.fasta | python simulate_nucleotide_errors.py K=20 P=0.001 --stats="MutStats.fasta" --mutated="Mutated1.fasta" ')



# Redownload the package:
$ git clone https://github.com/medvedevgroup/mutation-rate-intervals.git

pkj=/home/dasp5/packages/mutation-rate-intervals
ionput=/home/dasp5/dataset/Table2Analysis/Dataset_1kby_1k/Rawfasta_1kL/RGID_1.fasta
outputM=/home/dasp5/dataset/Table2Analysis/Dataset_1kby_1k/Mutated_0.001/Mutated/Mutated1.fasta
outputS=/home/dasp5/dataset/Table2Analysis/Dataset_1kby_1k/Mutated_0.001/Status/MutStats1.fasta
cat $ionput | python $pkj/simulate_nucleotide_errors.py K=20 P=0.001 --stats=$outputS --mutated=$outputM

# For loop example 
########################################
#Before going to run the script you need to activate the python environment
#$ pwd
#/home/dasp5/dataset/RandomSimulated
#$ source myenv/bin/activate


#!/bin/bash
# Tested using bash version 4.1.5

# Package Location
pkj=/home/dasp5/packages/mutation-rate-intervals

for ((i=1;i<=1000;i++)); 
do 
   input=/home/dasp5/dataset/Table2Analysis/Dataset_1kby_1k/Rawfasta_1kL/RGID_"$i".fasta
   outputM=/home/dasp5/dataset/Table2Analysis/Dataset_1kby_1k/Mutated_0.001/Mutated/Mutated_"$i".fasta
   outputS=/home/dasp5/dataset/Table2Analysis/Dataset_1kby_1k/Mutated_0.001/Status/MutStats_"$i".fasta
   cat $input | python $pkj/simulate_nucleotide_errors.py K=20 P=0.001 --stats=$outputS --mutated=$outputM
   
   echo $i
done


/home/dasp5/dataset/Table2Analysis/Dataset_1kby_1k/Mutate_0.01
/home/dasp5/dataset/Table2Analysis/Dataset_1kby_1k/Mutate_0.01/Mutated

###############################################################################
# Generate the seeds from the both sequences
#Before going to run the script you need to activate the python environment
#$ pwd
#/home/dasp5/dataset/RandomSimulated
#$ source myenv/bin/activate


#!/bin/bash

# Package Location
pkj=/home/dasp5/packages/noverlap/bin

for ((i=1;i<=1000;i++)); 
do 
   input=/home/dasp5/dataset/Table2Analysis/Dataset_1kby_1k/Rawfasta_1kL/RGID_"$i".fasta
   output=/home/dasp5/dataset/Table2Analysis/Dataset_1kby_1k/seeds/seed_11/Raw_seed/RawSeed_"$i".csv
   python $pkj/dna-seed-sim -m11 -M11 --syn-window=9 -s3 --seeds $input > $output
   echo "###########Compleated#############"
   echo $i
done


# This code is repeated in case of k-mer size 11, 21 and 41. The main dna-seed-sim line only 
# change according the k-mers size. This code is used multiple of times.

###############################################################################
# Now the code I have to developed is match the seeds between raw sequence and the seed in 
# mutated sequences and estimate the number of maches and the miss matches.



import pandas as pd

# Reading the syncmer (k-mers = 20, s=6) from raw sequence.
RawSeed = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/Table 2/new/RawSeed_1.csv",header=1, sep='\t')                

# Reading the syncmer (k-mers = 20, s=6) from p=0.01 mutated sequence.
MutSeed = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/Table 2/new/Mut_0.001Seed_1.csv",header=1,sep='\t')


# Find out common closed syncmer between raw and mutated sequence.
def common(RawClosedSyncmerSeq, mutClosedSyncmerSeq):
    CommonArray1 = []
    CommonArray2 = []
    start        = []
    count = 0
    for i in range(len(RawClosedSyncmerSeq)):
        if(RawClosedSyncmerSeq['sequence'][i] == mutClosedSyncmerSeq['sequence'][i]):
            start.append(RawClosedSyncmerSeq['# start'][i])
            CommonArray1.append(RawClosedSyncmerSeq['sequence'][i])
            CommonArray2.append(mutClosedSyncmerSeq['sequence'][i])
            count += 1
    cdata = {'start': start,'FromRawSeq': CommonArray1, 'MutatedSSeq': CommonArray2 }
    cdf = pd.DataFrame(cdata)
    count2 = len(RawClosedSyncmerSeq)
    return(count, count2, cdf)


# Getting the return values in to variables.
CommonSyncmerNumber1 , numberSMunmut1, CommonSyncmer1 = common(RawSeed, MutSeed)



# usage: theta-from-closed-syncmer-count.py [-h] 
# -k KMER_LENGTH 
# -s SMER_LENGTH 
# -n NUMBER_OF_SUBMERS 
# -u NUMBER_OF_UNMUTATED_SUBMERS [-c CONFIDENCE] [-l LENGTH]

python3 theta-from-closed-syncmer-count.py  -k 10 -s 3 -n 100 -u 90 -c 0.95



RawSeed.drop(index=0)

RawSeed = RawSeed.drop(label)
RawSeed = RawSeed.iloc[1: , :]


###############################################################################
"""
# First of all activate the python environment.
cd /home/dasp5/dataset/RandomSimulated/1.st_100_simulated/LengthAuto_1/FileOperation_1
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
for xx in range(100):
    #Raw Seed file read.
    RawSeed = pd.read_csv("/home/dasp5/dataset/Table2Analysis/Dataset_1kby_1k/seeds/seed_11/Raw_seed/RawSeed_"+str(count)+".csv",header=1, sep='\t') 
    # Mutated file read.
    MutSeed = pd.read_csv("/home/dasp5/dataset/Table2Analysis/Dataset_1kby_1k/seeds/seed_11/Mut_0.001_seed/Mut_0.001Seed_"+str(count)+".csv",header=1,sep='\t')
    # Find out the common sequence between raw and mutated sequence file.
    # This is the number of the mutated file's sequence that does not include the mutation.
    #df3=pd.merge(RawSeed,MutSeed, how='inner') # This code also can be used.
    df3=pd.merge(RawSeed['sequence'],MutSeed['sequence'], how='inner')
    count_of_submers = len(MutSeed) # NUMBER_OF_SUBMERS
    count_of_unmutated_syncmers = len(df3) #NUMBER_OF_UNMUTATED_SUBMERS
    confidence = 0.95
    alpha_0 = 1.0 - confidence # for consistency with z-score
    #length = argument.length
    k = 11
    s = 3 
    try:
        h = jls_submer_clt_mgr.to_syncmer_closed_Wilson_score_intervals_for_theta( count_of_submers, count_of_unmutated_syncmers, alpha_0, k, s) #, length 
        interval = to_theta_interval( h )
    except:
        interval = [None, None]  
    # Catch the process data in a frame.
    df1 = pd.DataFrame({'k-mer' : [k],
               's-mer': [s],
               'Number_of_submer' : [count_of_submers],
               'Number_of_UnmutSubmer' : [count_of_unmutated_syncmers],
               'ThetaLow' : interval[0],
               'ThetaHigh' : interval[1],
               'filename': ["Mut_0.001Seed_"+str(count)+".csv"]})
    df = df.append(df1, ignore_index=True)
    print("###############Completed###############)
    print(count)
    count = count + 1
    
    
 #Write all records
df.to_excel("./ResultsThetak11P0.001_n1000.xlsx") 
df.to_csv("./ResultsThetak11P0.001_n1000.txt") 
    
    
