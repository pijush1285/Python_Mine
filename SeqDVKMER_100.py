# -*- coding: utf-8 -*-
"""
Created on Sat May  7 01:24:24 2022

@author: PIJHUSH
"""

# Import libraries
import glob
import csv
from Bio import SeqIO


# Raw sequence reading
filename="C:/Users/PIJHUSH/Desktop/sheared/Simulated300/RawSequence/Simulated2M.fasta"
R_seq_object=SeqIO.read(filename,"fasta")
R_seq_id = R_seq_object.id
R_seq    = R_seq_object.seq


# Reading 100 fasta file.
path = 'C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Mutated'
csv_files = glob.glob(path + "/*.fasta")


csv_files[0]
seq_objectM = SeqIO.read(csv_files[0],"fasta")




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


def rbarCal(R_seq, sequenceM_1): 
    kmerSize=20
    mutatedkmer = count_mutated_kmers_linear(R_seq, sequenceM_1, 20)
    numKmers = len(sequenceM_1) - (kmerSize-1)
    UnmutatedKmer= numKmers - mutatedkmer
    rbar_1 = 1 - (UnmutatedKmer/numKmers)**(1/kmerSize)
    return rbar_1



# calculating Row bar
RBAR = []
for i in range(len(csv_files)):
    seq_objectM = SeqIO.read(csv_files[i],"fasta")
    rbar0_0i = rbarCal(R_seq, seq_objectM.seq)
    RBAR.append(rbar0_0i)
    print(rbar0_0i)



# open the file in the write mode
outpath = 'C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Seed'
f = open(outpath +'/rBar0.01.csv', 'w')
writer = csv.writer(f)
writer.writerow(RBAR)
f.close()

