# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 06:14:15 2022

@author: PIJHUSH
"""

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

###############################################################################
# Experiment 3
# Generate simulated fasta file containing 2M read

#Read the sequence
filename="C:/Users/PIJHUSH/Desktop/Python with Spyder/Exp2/Sim_P_0.05a/FirstSeq.fasta"
seq_object=SeqIO.read(filename,"fasta")
seq_id=seq_object.id
sequence=seq_object.seq
len(sequence)


# Sequence crop from it with 169940 neucleotide and add it to the raw sequnce.
crop=sequence[0:169940]    #2000000-1830060
new_seq = sequence + (''.join(crop))
len(new_seq)


#new_seq=seq.seq[0:200]
new_id=str(seq_id)
new_rec = SeqRecord(Seq(new_seq),id=new_id, description="new_Seq_0:2M")
SeqIO.write(new_rec,"Simulated2M.fasta","fasta")

###############################################################################
# First 100 neucleotide fasta file. Only by changing the 0 we can get different 
# fasta sequences.
crop=sequence[0:10000]
len(crop)


new_id=str(seq_id)
new_rec = SeqRecord(Seq(crop),id=new_id, description="new_Seq_0:10000N")
SeqIO.write(new_rec,"Simulated10000N.fasta","fasta")



