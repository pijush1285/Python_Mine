# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 17:50:14 2022
This is the newer version of Table 2 data analysis.
This code is used for analyszing the dataset where 
each sequence contains 10k neucleotide sequences.


# First of all activate the python environment.
cd /home/dasp5/dataset/RandomSimulated
source myenv/bin/activate

New my environment is created
cd /home/dasp5/packages
source myenv/bin/activate

# To run the code in the server use the script below
$python RandomSeq.py -n 1000 -l 10000

@author: PIJHUSH
"""

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from random import choice
import random
from argparse import ArgumentParser, RawTextHelpFormatter


def main(): 
    parser = getArguments()
    argument = parser.parse_args()
    check( argument ) 
    number_of_sequence = argument.seq_number
    sequence_length = argument.seq_length
    RandomSequenceGenerator(number_of_sequence, sequence_length)
    
    
def getsequences(length):
    bases=["A","G","C","T"]
    sequence=""
    for count in range(length):
        sequence+=choice(bases)
    return sequence

# Now the function is define below. We need to pass the number of file and the 
# Length of the genome sequence.
def RandomSequenceGenerator(number, length):
    random.seed(31415)
    count = 1
    for x in range(number):
            len1 = length
            sequence = getsequences(len1)  
            name = "RGID_"+str(count)
            new_id = str(name)
            new_rec = SeqRecord(Seq(sequence),id=new_id, description="Random_SeqLength_0:"+str(length)+".")
            FastaFileName = str(name)+".fasta"
            SeqIO.write(new_rec, FastaFileName,"fasta")
            print("Fasta file generate completed number:", count)
            count = count + 1
            

# Check and fixes arguments if possible.    
def check( argument ):
    if argument.seq_number <= 0:
        raise Exception( f'Error: seq_number = {argument.seq_number} <= 0.' )
    if argument.seq_length <= 0:
        raise Exception( f'Error: seq_length = {argument.seq_length} <= 0.' )
        
        
        
def getArguments():
    parser = ArgumentParser(description='The fasta files will be generated at random using this script.\n',
                            formatter_class=RawTextHelpFormatter)
    parser.add_argument("-n", "--seq_number", dest="seq_number", type=int, required=True, 
                        help="SEQ_NUMBER is the number of sequence you want to produce.", metavar="SEQ_NUMBER")
    parser.add_argument("-l", "--seq_length", dest="seq_length", type=int, required=True,
                        help="SEQ_LENGTH is the length of the sequence you want to produce.", metavar="SEQ_LENGTH") 
    return parser      
        
        
if __name__ == "__main__":
    main()

###############################################################################
# First make the directory name Mutated_0.001  Mutated_0.01  Mutated_0.1  Mutated_0.2
# After that make Mutated , Status direectory inside each directory previouslt created.
# Then set the path for each directory.

# First of all activate the python environment.
#cd /home/dasp5/dataset/RandomSimulated
#source myenv/bin/activate

#New my environment is created
#cd /home/dasp5/packages
#source myenv/bin/activate


#!/bin/bash 

#Package Location

pkj=/home/dasp5/packages/mutation-rate-intervals

for ((i=1;i<=1000;i++));
do
   ionput=/home/dasp5/dataset/Table3/1_Dataset_0.1kby1k/Raw_Fasta/RGID_"$i".fasta
   outputM=/home/dasp5/dataset/Table3/1_Dataset_0.1kby1k/Mutated_0.05/Mutated/Mutated_"$i".fasta
   outputS=/home/dasp5/dataset/Table3/1_Dataset_0.1kby1k/Mutated_0.05/Status/MutStats_"$i".fasta
   cat $ionput | python $pkj/simulate_nucleotide_errors.py K=20 P=0.05 --stats=$outputS --mutated=$outputM
   
   
   outputM1=/home/dasp5/dataset/Table3/1_Dataset_0.1kby1k/Mutated_0.15/Mutated/Mutated_"$i".fasta
   outputS1=/home/dasp5/dataset/Table3/1_Dataset_0.1kby1k/Mutated_0.15/Status/MutStats_"$i".fasta
   cat $ionput | python $pkj/simulate_nucleotide_errors.py K=20 P=0.15 --stats=$outputS1 --mutated=$outputM1
   
   outputM2=/home/dasp5/dataset/Table3/1_Dataset_0.1kby1k/Mutated_0.25/Mutated/Mutated_"$i".fasta
   outputS2=/home/dasp5/dataset/Table3/1_Dataset_0.1kby1k/Mutated_0.25/Status/MutStats_"$i".fasta
   cat $ionput | python $pkj/simulate_nucleotide_errors.py K=20 P=0.25 --stats=$outputS2 --mutated=$outputM2
   
   
   echo $i
   echo "***********Completed*********"
done

################################################################################
# Generate the seeds
#Before going to run the script you need to activate the python environment
#$ pwd
#cd /home/dasp5/dataset/RandomSimulated
#$ source myenv/bin/activate

#New my environment is created
#cd /home/dasp5/packages
#source myenv/bin/activate

# TO run the script : ./SeedScript.sh


#!/bin/bash

# Package Location
pkj=/home/dasp5/packages/noverlap/bin

comInputAdd=/home/dasp5/dataset/Table3/5_Dataset_1000kby1k
comOutputAdd=/home/dasp5/dataset/Table3/5_Dataset_1000kby1k/seeds

for ((i=1;i<=1000;i++)); 
do 
   input1=$comInputAdd/Raw_Fasta/RGID_"$i".fasta
   output1=$comOutputAdd/1_Raw_seed/RawSeed_"$i".csv
   python $pkj/dna-seed-sim -m21 -M21 --syn-window=16 -s6 --seeds $input1 > $output1
   
   input2=$comInputAdd/Mutated_0.05/Mutated/Mutated_"$i".fasta
   output2=$comOutputAdd/2_Mutated_0.05_seed/Mut_0.05Seed_"$i".csv
   python $pkj/dna-seed-sim -m21 -M21 --syn-window=16 -s6 --seeds $input2 > $output2
   
   input3=$comInputAdd/Mutated_0.15/Mutated/Mutated_"$i".fasta
   output3=$comOutputAdd/3_Mutated_0.15_seed/Mut_0.15Seed_"$i".csv
   python $pkj/dna-seed-sim -m21 -M21 --syn-window=16 -s6 --seeds $input3 > $output3
   
   
   input4=$comInputAdd/Mutated_0.25/Mutated/Mutated_"$i".fasta
   output4=$comOutputAdd/4_Mutated_0.25_seed/Mut_0.25Seed_"$i".csv
   python $pkj/dna-seed-sim -m21 -M21 --syn-window=16 -s6 --seeds $input4 > $output4

   
   echo "###########Compleated#############"
   echo $i
done

###############################################################################
"""
# First of all activate the python environment.
Run: $pwd
Run: $cd /home/dasp5/dataset/RandomSimulated/1.st_100_simulated/LengthAuto_1/FileOperation_1
Run: $source myenv/bin/activate
Run: $cd out_put_pwd 


#New my environment is created
#cd /home/dasp5/packages
#source myenv/bin/activate


# Next copy the code and named as  Theta_k21_P0.001_N1000.py
$python ./Theta_k21_P0.25_N1000.py
"""


import pandas as pd
import sys
# This path is used for server.
sys.path.append('/home/dasp5/packages/submer-central-limit-theorem/modules')
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
    RawSeed = pd.read_csv("/home/dasp5/dataset/Table3/2_Dataset_1kby1k/seeds/1_Raw_seed/RawSeed_"+str(count)+".csv",header=1, sep='\t') 
    # Mutated file read.
    MutSeed = pd.read_csv("/home/dasp5/dataset/Table3/2_Dataset_1kby1k/seeds/4_Mutated_0.25_seed/Mut_0.25Seed_"+str(count)+".csv",header=1,sep='\t')
    # Find out the common sequence between raw and mutated sequence file.
    # This is the number of the mutated file's sequence that does not include the mutation.
    #df3=pd.merge(RawSeed,MutSeed, how='inner') # This code also can be used.
    df3=pd.merge(RawSeed['sequence'],MutSeed['sequence'], how='inner')
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
    df1 = pd.DataFrame({'k-mer' : [k],
               's-mer': [s],
               'Number_of_submer' : [count_of_submers],
               'Number_of_UnmutSubmer' : [count_of_unmutated_syncmers],
               'ThetaLow' : interval[0],
               'ThetaHigh' : interval[1],
               'filename': ["Mut_0.25Seed_"+str(count)+".csv"]})
    df = df.append(df1, ignore_index=True)
    print("###############Completed###############")
    print(count)
    count = count + 1
    
    
 #Write all records
df.to_excel("./ResultsThetak21P0.25_n1000.xlsx") 
df.to_csv("./ResultsThetak21P0.25_n1000.txt") 
    

