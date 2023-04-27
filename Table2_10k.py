# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 08:48:52 2022

@author: PIJHUSH

This is the newer version of Table 2 data analysis.
This code is used for analyszing the dataset where 
each sequence contains 10k neucleotide sequences.


# First of all activate the python environment.
cd /home/dasp5/dataset/RandomSimulated
source myenv/bin/activate

# To run the code in the server use the script below
$python RandomSeq.py -n 1000 -l 10000

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
# Mutation need to be inserted to the sequence.

# First of all activate the python environment.
#cd /home/dasp5/dataset/RandomSimulated
#source myenv/bin/activate


#!/bin/bash

#Package Location

pkj=/home/dasp5/packages/mutation-rate-intervals

for ((i=1;i<=1000;i++));
do
   ionput=/home/dasp5/dataset/Table2Analysis/Dataset_10kby_1k/Rawfasta_10kL/RGID_"$i".fasta
   outputM=/home/dasp5/dataset/Table2Analysis/Dataset_10kby_1k/Mutated_0.001/Mutated/Mutated_"$i".fasta
   outputS=/home/dasp5/dataset/Table2Analysis/Dataset_10kby_1k/Mutated_0.001/Status/MutStats_"$i".fasta
   cat $ionput | python $pkj/simulate_nucleotide_errors.py K=20 P=0.001 --stats=$outputS --mutated=$outputM
   echo $i
   echo "***********Completed*********"
done


#################### New version of this script ###############################
# First make the directory name Mutated_0.001  Mutated_0.01  Mutated_0.1  Mutated_0.2
# After that make Mutated , Status direectory inside each directory previouslt created.
# Then set the path for each directory.

# First of all activate the python environment.
#cd /home/dasp5/dataset/RandomSimulated
#source myenv/bin/activate


#!/bin/bash 

#Package Location

pkj=/home/dasp5/packages/mutation-rate-intervals

for ((i=1;i<=1000;i++));
do
   ionput=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k/Rawfasta_100kL/RGID_"$i".fasta
   outputM=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k/Mutated_0.001/Mutated/Mutated_"$i".fasta
   outputS=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k/Mutated_0.001/Status/MutStats_"$i".fasta
   cat $ionput | python $pkj/simulate_nucleotide_errors.py K=20 P=0.001 --stats=$outputS --mutated=$outputM
   
   
   outputM1=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k/Mutated_0.01/Mutated/Mutated_"$i".fasta
   outputS1=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k/Mutated_0.01/Status/MutStats_"$i".fasta
   cat $ionput | python $pkj/simulate_nucleotide_errors.py K=20 P=0.01 --stats=$outputS1 --mutated=$outputM1
   
   outputM2=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k/Mutated_0.1/Mutated/Mutated_"$i".fasta
   outputS2=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k/Mutated_0.1/Status/MutStats_"$i".fasta
   cat $ionput | python $pkj/simulate_nucleotide_errors.py K=20 P=0.1 --stats=$outputS2 --mutated=$outputM2
   
   outputM3=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k/Mutated_0.2/Mutated/Mutated_"$i".fasta
   outputS3=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k/Mutated_0.2/Status/MutStats_"$i".fasta
   cat $ionput | python $pkj/simulate_nucleotide_errors.py K=20 P=0.2 --stats=$outputS3 --mutated=$outputM3
   
   echo $i
   echo "***********Completed*********"
done

###############################################################################
# Generate the seeds
#Before going to run the script you need to activate the python environment
#$ pwd
#cd /home/dasp5/dataset/RandomSimulated
#$ source myenv/bin/activate


#!/bin/bash

# Package Location
pkj=/home/dasp5/packages/noverlap/bin

for ((i=1;i<=1000;i++)); 
do 
   input1=/home/dasp5/dataset/Table2Analysis/Dataset_10kby_1k/Rawfasta_10kL/RGID_"$i".fasta
   output1=/home/dasp5/dataset/Table2Analysis/Dataset_10kby_1k/seeds/seed_11/Raw_seed/RawSeed_"$i".csv
   python $pkj/dna-seed-sim -m11 -M11 --syn-window=9 -s3 --seeds $input1 > $output1
   
   input2=/home/dasp5/dataset/Table2Analysis/Dataset_10kby_1k/Mutated_0.001/Mutated/Mutated_"$i".fasta
   output2=/home/dasp5/dataset/Table2Analysis/Dataset_10kby_1k/seeds/seed_11/Mut_0.001_seed/Mut_0.001Seed_"$i".csv
   python $pkj/dna-seed-sim -m11 -M11 --syn-window=9 -s3 --seeds $input2 > $output2
   
   input3=/home/dasp5/dataset/Table2Analysis/Dataset_10kby_1k/Mutated_0.01/Mutated/Mutated_"$i".fasta
   output3=/home/dasp5/dataset/Table2Analysis/Dataset_10kby_1k/seeds/seed_11/Mut_0.01_seed/Mut_0.01Seed_"$i".csv
   python $pkj/dna-seed-sim -m11 -M11 --syn-window=9 -s3 --seeds $input3 > $output3
   
   
   input4=/home/dasp5/dataset/Table2Analysis/Dataset_10kby_1k/Mutated_0.1/Mutated/Mutated_"$i".fasta
   output4=/home/dasp5/dataset/Table2Analysis/Dataset_10kby_1k/seeds/seed_11/Mut_0.1_seed/Mut_0.1Seed_"$i".csv
   python $pkj/dna-seed-sim -m11 -M11 --syn-window=9 -s3 --seeds $input4 > $output4


   input5=/home/dasp5/dataset/Table2Analysis/Dataset_10kby_1k/Mutated_0.2/Mutated/Mutated_"$i".fasta
   output5=/home/dasp5/dataset/Table2Analysis/Dataset_10kby_1k/seeds/seed_11/Mut_0.2_seed/Mut_0.2Seed_"$i".csv
   python $pkj/dna-seed-sim -m11 -M11 --syn-window=9 -s3 --seeds $input5 > $output5
   
   
   echo "###########Compleated#############"
   echo $i
done


################################################################################
#Seed 21

#!/bin/bash

# Package Location
pkj=/home/dasp5/packages/noverlap/bin

comInputAdd=/home/dasp5/dataset/Table2Analysis/Dataset_10kby_1k
comOutputAdd=/home/dasp5/dataset/Table2Analysis/Dataset_10kby_1k/seeds/seed_21

for ((i=1;i<=1000;i++)); 
do 
   input1=$comInputAdd/Rawfasta_10kL/RGID_"$i".fasta
   output1=$comOutputAdd/Raw_seed/RawSeed_"$i".csv
   python $pkj/dna-seed-sim -m21 -M21 --syn-window=16 -s6 --seeds $input1 > $output1
   
   input2=$comInputAdd/Mutated_0.001/Mutated/Mutated_"$i".fasta
   output2=$comOutputAdd/Mut_0.001_seed/Mut_0.001Seed_"$i".csv
   python $pkj/dna-seed-sim -m21 -M21 --syn-window=16 -s6 --seeds $input2 > $output2
   
   input3=$comInputAdd/Mutated_0.01/Mutated/Mutated_"$i".fasta
   output3=$comOutputAdd/Mut_0.01_seed/Mut_0.01Seed_"$i".csv
   python $pkj/dna-seed-sim -m21 -M21 --syn-window=16 -s6 --seeds $input3 > $output3
   
   
   input4=$comInputAdd/Mutated_0.1/Mutated/Mutated_"$i".fasta
   output4=$comOutputAdd/Mut_0.1_seed/Mut_0.1Seed_"$i".csv
   python $pkj/dna-seed-sim -m21 -M21 --syn-window=16 -s6 --seeds $input4 > $output4


   input5=$comInputAdd/Mutated_0.2/Mutated/Mutated_"$i".fasta
   output5=$comOutputAdd/Mut_0.2_seed/Mut_0.2Seed_"$i".csv
   python $pkj/dna-seed-sim -m21 -M21 --syn-window=16 -s6 --seeds $input5 > $output5
   
   
   echo "###########Compleated#############"
   echo $i
done

################################################################################
#Seed 31

#!/bin/bash

# Package Location
pkj=/home/dasp5/packages/noverlap/bin

comInputAdd=/home/dasp5/dataset/Table2Analysis/Dataset_10kby_1k
comOutputAdd=/home/dasp5/dataset/Table2Analysis/Dataset_10kby_1k/seeds/seed_31

for ((i=1;i<=1000;i++)); 
do 
   input1=$comInputAdd/Rawfasta_10kL/RGID_"$i".fasta
   output1=$comOutputAdd/Raw_seed/RawSeed_"$i".csv
   python $pkj/dna-seed-sim -m31 -M31 --syn-window=22 -s10 --seeds $input1 > $output1
   
   input2=$comInputAdd/Mutated_0.001/Mutated/Mutated_"$i".fasta
   output2=$comOutputAdd/Mut_0.001_seed/Mut_0.001Seed_"$i".csv
   python $pkj/dna-seed-sim -m31 -M31 --syn-window=22 -s10 --seeds $input2 > $output2
   
   input3=$comInputAdd/Mutated_0.01/Mutated/Mutated_"$i".fasta
   output3=$comOutputAdd/Mut_0.01_seed/Mut_0.01Seed_"$i".csv
   python $pkj/dna-seed-sim -m31 -M31 --syn-window=22 -s10 --seeds $input3 > $output3
   
   
   input4=$comInputAdd/Mutated_0.1/Mutated/Mutated_"$i".fasta
   output4=$comOutputAdd/Mut_0.1_seed/Mut_0.1Seed_"$i".csv
   python $pkj/dna-seed-sim -m31 -M31 --syn-window=22 -s10 --seeds $input4 > $output4


   input5=$comInputAdd/Mutated_0.2/Mutated/Mutated_"$i".fasta
   output5=$comOutputAdd/Mut_0.2_seed/Mut_0.2Seed_"$i".csv
   python $pkj/dna-seed-sim -m31 -M31 --syn-window=22 -s10 --seeds $input5 > $output5
   
   
   echo "###########Compleated#############"
   echo $i
done

################################################################################
#Seed 41


#!/bin/bash

# Package Location
pkj=/home/dasp5/packages/noverlap/bin

comInputAdd=/home/dasp5/dataset/Table2Analysis/Dataset_10kby_1k
comOutputAdd=/home/dasp5/dataset/Table2Analysis/Dataset_10kby_1k/seeds/seed_41

for ((i=1;i<=1000;i++)); 
do 
   input1=$comInputAdd/Rawfasta_10kL/RGID_"$i".fasta
   output1=$comOutputAdd/Raw_seed/RawSeed_"$i".csv
   python $pkj/dna-seed-sim -m41 -M41 --syn-window=30 -s12 --seeds $input1 > $output1
   
   input2=$comInputAdd/Mutated_0.001/Mutated/Mutated_"$i".fasta
   output2=$comOutputAdd/Mut_0.001_seed/Mut_0.001Seed_"$i".csv
   python $pkj/dna-seed-sim -m41 -M41 --syn-window=30 -s12 --seeds $input2 > $output2
   
   input3=$comInputAdd/Mutated_0.01/Mutated/Mutated_"$i".fasta
   output3=$comOutputAdd/Mut_0.01_seed/Mut_0.01Seed_"$i".csv
   python $pkj/dna-seed-sim -m41 -M41 --syn-window=30 -s12 --seeds $input3 > $output3
   
   
   input4=$comInputAdd/Mutated_0.1/Mutated/Mutated_"$i".fasta
   output4=$comOutputAdd/Mut_0.1_seed/Mut_0.1Seed_"$i".csv
   python $pkj/dna-seed-sim -m41 -M41 --syn-window=30 -s12 --seeds $input4 > $output4


   input5=$comInputAdd/Mutated_0.2/Mutated/Mutated_"$i".fasta
   output5=$comOutputAdd/Mut_0.2_seed/Mut_0.2Seed_"$i".csv
   python $pkj/dna-seed-sim -m41 -M41 --syn-window=30 -s12 --seeds $input5 > $output5
   
   
   echo "###########Compleated#############"
   echo $i
done
