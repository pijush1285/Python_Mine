# -*- coding: utf-8 -*-
"""
Created on Sat May 14 12:01:31 2022
This program extract all those fasta sequences from a multifasta toy data set.
@author: PIJHUSH
"""

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq


filename="C:/Users/PIJHUSH/Desktop/sheared/ToyDataset/erickson_accessions.fasta"
seq_object=SeqIO.read(filename,"fasta")
seq_id=seq_object.id
sequence=seq_object.seq
len(sequence)

# For getting all the names of the fasta sequences
for record in SeqIO.parse(filename, "fasta"):
    print("%s %i" % (record.id, len(record)))
    
    

# Change the directory to store those sepqrated sequences
#cd C:/Users/PIJHUSH/Desktop/sheared/ToyDataset/SeperatedFasta

# Get all those sequences seperated which will be stored in a folder 
fasta_sequences = SeqIO.parse(filename,'fasta')
for fasta in fasta_sequences:
        name , sequence = fasta.id, str(fasta.seq)    
        new_id = str(name)
        new_rec = SeqRecord(Seq(sequence),id=new_id, description="new_Seq_0:10000N")
        FastaFileName = str(name)+".fasta"
        SeqIO.write(new_rec, FastaFileName,"fasta")
        
        
 
        
        
        
        