# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 22:53:23 2022

@author: PIJHUSH
"""

#import biopython
from Bio import SeqIO
import math


###############################################################################
# Orginal Sequence reading.
#set file path
filename="C:/Users/PIJHUSH/Desktop/Python with Spyder/Exp2/Sim_P_0.05a/FirstSeq.fasta"
#read fasta file
seq_object=SeqIO.read(filename,"fasta")
#get sequence id
seq_id=seq_object.id
print(seq_id)
#get sequence itself
sequence=seq_object.seq
print(sequence)

header=seq_object.id
seq=seq_object.seq

# Write a fasta file with small sewuences e.g. 200 neucleotide.
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

new_seq=seq.seq[0:200]
new_id=str(seq.id)
new_rec = SeqRecord(Seq(new_seq),id=new_id, description="new_Seq_0:200")
SeqIO.write(new_rec,"NewSeq.fasta","fasta")


###############################################################################
# Mutated Sequence reading.

filenameM="C:/Users/PIJHUSH/Desktop/Python with Spyder/Exp2/Sim_P_0.05a/Mutated_0.05.fasta"
seq_objectM=SeqIO.read(filenameM,"fasta")
seq_idM=seq_objectM.id
print(seq_idM)
sequenceM=seq_objectM.seq
print(sequence)

headerM=seq_objectM.id
seqM=seq_objectM.seq


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




mutatedkmer=count_mutated_kmers_linear(seq, seqM, 20)
#print(count_mutated_kmers_linear(seq, seqM,20))
# Total number of k-mer
kmerSize=20
numKmers = len(seq) - (kmerSize-1)
# Total number of unmutated k-mers
UnmutatedKmer= numKmers - mutatedkmer
     
print('Total number of k-mer:', numKmers )
print('Total number of Unmutated k-mers:', UnmutatedKmer)
print('Total number of Mutated k-mers:', mutatedkmer)


###############################################################################
# Estimation of eta value according to the blanca's paper.

#Let n be the number of seeds in the read
n=numKmers
m=UnmutatedKmer
e=1/kmerSize*math.log(n/m, base=10)



###############################################################################
# Experiment 2
pkj="C:/Users/PIJHUSH/Desktop/John/Codes/mutation-rate-intervals"
#run $pkj/r1-to-nmut-hypothesis.py L=4.5M k=15 C=0.95 r1=0.01

print('Total number of k-mer:', numKmers )













