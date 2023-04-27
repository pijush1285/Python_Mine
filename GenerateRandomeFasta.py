# -*- coding: utf-8 -*-
"""
Created on Sat May 14 22:32:44 2022

Genetare randome sequence

@author: PIJHUSH
"""
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from random import choice

###############################################################################
# This is experimental portion oc the code.
# Define length of sequence
length=100
#supply list of nucleotides
bases=["A","G","C","T"]
print(bases)

# Generate a sequence
# create empty sequence
sequence =""
#randomly select base and add to sequence(repeat 100 times for length=100)
for i in range(length):
    base=choice(bases)
    sequence+=base
    
print(sequence)

# Create function to generate sequences
def getsequences(length):
  sequence=""
  for count in range(length):
    sequence+=choice(bases)
  return sequence

#where "getsequences" is the function name
getsequences(length)


###############################################################################
# Make this Sequence a fasta file
# Generate 2M Reads.
length = 2000000
Simulated2m = getsequences(length)
len(Simulated2m)

# Write this read into a fasta file with header
seq_id = "RGID_1"
new_id=str(seq_id)
new_rec = SeqRecord(Seq(Simulated2m),id=new_id, description="new_Seq_0:2M")
SeqIO.write(new_rec,"RGID_1.fasta","fasta")

###############################################################################
# Now convert this into automated fasta sequence generatior function.
# Initially learning to use the loop
count = 1
for x in range(6):
        length = 2000000
        sequence = getsequences(length)  
        name = "RGID_"+str(count)
        new_id = str(name)
        new_rec = SeqRecord(Seq(sequence),id=new_id, description="new_Seq_0:2M")
        FastaFileName = str(name)+".fasta"
        SeqIO.write(new_rec, FastaFileName,"fasta")
        count = count + 1

# Experiment:
count = 1
for x in range(6):
    name = "RGID_"+str(count)
    print(name)
    count = count + 1
    
# Now the function is define below. We need to pass the number of file and the 
# Length of the genome sequence.
def RandomeSequenceGenerator(number, length):
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
RandomeSequenceGenerator(100, 2000000)


