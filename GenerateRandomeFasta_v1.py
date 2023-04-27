# -*- coding: utf-8 -*-
"""
Created on Sat May 21 02:45:28 2022

@author: PIJHUSH
"""


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
RandomeSequenceGenerator(10, 2000000)