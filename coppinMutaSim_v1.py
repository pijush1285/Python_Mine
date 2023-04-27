# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 11:39:48 2022

@author: PIJHUSH
"""

from random import random, choice
import sys
#from itertools import groupby
from Bio import SeqIO


def fasta_iter(fasta_name):
    """
    given a fasta file. yield tuples of header, sequence
    """
    
    seq_object=SeqIO.read(fasta_name,"fasta")
    header=seq_object.id
    seq=seq_object.seq[0:20]
    yield header, seq
        
        

def main(fasta_name, mutation_freq):

    for header, seq in fasta_iter(fasta_name):
        seq1 = list(seq)
        for i, s in enumerate(seq1):
            val = random()
            if val < mutation_freq:
                # choose a random nucleotide that's different.
                seq1[i] = choice([x for x in "ACTG" if x != s.upper()])
        print(">%s\n%s" % (header, "".join(seq1)))
        print("######### Original Sequence ##########")
        print(seq)

if __name__ == "__main__":
    main(sys.argv[1], float(sys.argv[2]))
    
    
 
    