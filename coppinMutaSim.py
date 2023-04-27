# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 21:46:23 2022

@author: PIJHUSH
#https://www.biostars.org/p/12417/
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
    seq=seq_object.seq
    yield header, seq
    # fh = open(fasta_name)
    # # ditch the boolean (x[0]) and just keep the header or sequence since
    # # we know they alternate.
    # faiter = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))
    # for header in faiter:
    #     # drop the ">"
    #     header = header.next()[1:].strip()
    #     # join all sequence lines to one.
    #     seq = "".join(s.strip() for s in faiter.next())
    #     yield header, seq 
        
        
        
        

def main(fasta_name, mutation_freq):

    for header, seq in fasta_iter(fasta_name):
        seq = list(seq)
        for i, s in enumerate(seq):
            val = random()
            if val < mutation_freq:
                # choose a random nucleotide that's different.
                seq[i] = choice([x for x in "ACTG" if x != s.upper()])
        print(">%s\n%s" % (header, "".join(seq)))

if __name__ == "__main__":
    main(sys.argv[1], float(sys.argv[2]))
    
    
 
    
