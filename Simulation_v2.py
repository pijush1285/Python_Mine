# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 08:50:57 2022

@author: PIJHUSH

To run the script use the command given below:
    run Simulation_v2.py FirstSeq.fasta 10 15
    10 -> Number of Mutation
    15 -> k-mer size
"""

import random
import sys
from Bio import SeqIO
from random import choice as random_choice
                          
#from random import random, choice



#######################################################
# Given a fasta file. yield tuples of header, sequence
#######################################################
def fasta_iter(fasta_name):
    seq_object=SeqIO.read(fasta_name,"fasta")
    header=seq_object.id
    seq=seq_object.seq[0:40]
    yield header, seq
    

# Generate mutation randomly    
def rand_mutation(number_ofMutation):
    sample_list = []
    #https://pynative.com/python-random-sample/
    sample_list = random.sample(range(0, 100), number_ofMutation)
    return sample_list
    

ntToMutations = {"A":"CGT","C":"AGT","G":"ACT","T":"ACG",
		         "a":"cgt","c":"agt","g":"act","t":"acg"}

# Implement error in the sequence
def apply_errors(seq2,errorPositions):
	mutatedSeq = list(seq2)
	for pos in errorPositions:
		nuc = seq2[pos]
		mutations = ntToMutations[nuc] if (nuc in ntToMutations) else "ACGT"
		mutatedSeq[pos] = random_choice(mutations)
	return "".join(mutatedSeq) 



# is_valid_kmer--
#	true if the kmer contains only ACGT characters (upper and lower case);
#	false otherwise
def is_valid_kmer(seq):
	validCount = sum([(nt in "ACGTacgt") for nt in seq])
	return (validCount == len(seq))


def count_mutated_kmers_linear(seq,mutatedSeq,kmerSize):
	assert (len(seq) == len(mutatedSeq))
	assert (len(seq) >= kmerSize)
	numKmers = len(seq) - (kmerSize-1)
	nMutated = 0
	for pos in range(numKmers):
		sKmer = seq[pos:pos+kmerSize]
		if (not is_valid_kmer(sKmer)): continue
		if (sKmer != mutatedSeq[pos:pos+kmerSize]):
			nMutated += 1       # pos is 'mutated'
	return nMutated


def main(fasta_name, number_ofMutation, kmerSize):

     for header, seq in fasta_iter(fasta_name):
         seq = seq
         header = header    
     print(">%s\n%s" % (header, "".join(seq))) 
     
     
     error_list=rand_mutation(number_ofMutation)
     print('The errors position in the sequence:', error_list )
     
     mutseq=apply_errors(seq, error_list)
     print('Mutated Sequence',">%s\n%s" % (header, mutseq)) 
     
     mutatedkmer = count_mutated_kmers_linear(seq,mutseq,kmerSize)
     # Total number of k-mer
     numKmers = len(seq) - (kmerSize-1)
     # Total number of unmutated k-mers
     UnmutatedKmer= numKmers - mutatedkmer
     
     print('Total number of k-mer:', numKmers )
     print('Total number of Unmutated k-mers:', UnmutatedKmer)
     print('Total number of Mutated k-mers:', mutatedkmer)
     
         
if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3])) 
             
         