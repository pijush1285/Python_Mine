# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 17:44:24 2022

@author: PIJHUSH
"""

#import biopython
from Bio import SeqIO
import pandas as pd


# Raw sequence reading
filename="C:/Users/PIJHUSH/Desktop/sheared/Simulated300/RawSequence/Simulated2M.fasta"
R_seq_object=SeqIO.read(filename,"fasta")
R_seq_id = R_seq_object.id
R_seq    = R_seq_object.seq


# Mutated Sequence reading.
path = 'C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Mutated'
seq_objectM_1 = SeqIO.read(path+'/'+'Mutated_0.01_1.fasta',"fasta")
seq_objectM_2 = SeqIO.read(path+'/'+'Mutated_0.01_2.fasta',"fasta")
seq_objectM_3 = SeqIO.read(path+'/'+'Mutated_0.01_3.fasta',"fasta")
seq_objectM_4 = SeqIO.read(path+'/'+'Mutated_0.01_4.fasta',"fasta")
seq_objectM_5 = SeqIO.read(path+'/'+'Mutated_0.01_5.fasta',"fasta")
seq_objectM_6 = SeqIO.read(path+'/'+'Mutated_0.01_6.fasta',"fasta")
seq_objectM_7 = SeqIO.read(path+'/'+'Mutated_0.01_7.fasta',"fasta")
seq_objectM_8 = SeqIO.read(path+'/'+'Mutated_0.01_8.fasta',"fasta")
seq_objectM_9 = SeqIO.read(path+'/'+'Mutated_0.01_9.fasta',"fasta")
seq_objectM_10 = SeqIO.read(path+'/'+'Mutated_0.01_10.fasta',"fasta")
seq_objectM_11 = SeqIO.read(path+'/'+'Mutated_0.01_11.fasta',"fasta")
seq_objectM_12 = SeqIO.read(path+'/'+'Mutated_0.01_12.fasta',"fasta")
seq_objectM_13 = SeqIO.read(path+'/'+'Mutated_0.01_13.fasta',"fasta")
seq_objectM_14 = SeqIO.read(path+'/'+'Mutated_0.01_14.fasta',"fasta")
seq_objectM_15 = SeqIO.read(path+'/'+'Mutated_0.01_15.fasta',"fasta")
seq_objectM_16 = SeqIO.read(path+'/'+'Mutated_0.01_16.fasta',"fasta")
seq_objectM_17 = SeqIO.read(path+'/'+'Mutated_0.01_17.fasta',"fasta")
seq_objectM_18 = SeqIO.read(path+'/'+'Mutated_0.01_18.fasta',"fasta")
seq_objectM_19 = SeqIO.read(path+'/'+'Mutated_0.01_19.fasta',"fasta")
seq_objectM_20 = SeqIO.read(path+'/'+'Mutated_0.01_20.fasta',"fasta")


# Mutated Sequence reading.
path = 'C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.1/Mutated'
seq_objectM_1 = SeqIO.read(path+'/'+'Mutated_0.1_1.fasta',"fasta")
seq_objectM_2 = SeqIO.read(path+'/'+'Mutated_0.1_2.fasta',"fasta")
seq_objectM_3 = SeqIO.read(path+'/'+'Mutated_0.1_3.fasta',"fasta")
seq_objectM_4 = SeqIO.read(path+'/'+'Mutated_0.1_4.fasta',"fasta")
seq_objectM_5 = SeqIO.read(path+'/'+'Mutated_0.1_5.fasta',"fasta")
seq_objectM_6 = SeqIO.read(path+'/'+'Mutated_0.1_6.fasta',"fasta")
seq_objectM_7 = SeqIO.read(path+'/'+'Mutated_0.1_7.fasta',"fasta")
seq_objectM_8 = SeqIO.read(path+'/'+'Mutated_0.1_8.fasta',"fasta")
seq_objectM_9 = SeqIO.read(path+'/'+'Mutated_0.1_9.fasta',"fasta")
seq_objectM_10 = SeqIO.read(path+'/'+'Mutated_0.1_10.fasta',"fasta")
seq_objectM_11 = SeqIO.read(path+'/'+'Mutated_0.1_11.fasta',"fasta")
seq_objectM_12 = SeqIO.read(path+'/'+'Mutated_0.1_12.fasta',"fasta")
seq_objectM_13 = SeqIO.read(path+'/'+'Mutated_0.1_13.fasta',"fasta")
seq_objectM_14 = SeqIO.read(path+'/'+'Mutated_0.1_14.fasta',"fasta")
seq_objectM_15 = SeqIO.read(path+'/'+'Mutated_0.1_15.fasta',"fasta")
seq_objectM_16 = SeqIO.read(path+'/'+'Mutated_0.1_16.fasta',"fasta")
seq_objectM_17 = SeqIO.read(path+'/'+'Mutated_0.1_17.fasta',"fasta")
seq_objectM_18 = SeqIO.read(path+'/'+'Mutated_0.1_18.fasta',"fasta")
seq_objectM_19 = SeqIO.read(path+'/'+'Mutated_0.1_19.fasta',"fasta")
seq_objectM_20 = SeqIO.read(path+'/'+'Mutated_0.1_20.fasta',"fasta")


# Mutated Sequence reading.
path = 'C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.2/Mutated'
seq_objectM_1 = SeqIO.read(path+'/'+'Mutated_0.2_1.fasta',"fasta")
seq_objectM_2 = SeqIO.read(path+'/'+'Mutated_0.2_2.fasta',"fasta")
seq_objectM_3 = SeqIO.read(path+'/'+'Mutated_0.2_3.fasta',"fasta")
seq_objectM_4 = SeqIO.read(path+'/'+'Mutated_0.2_4.fasta',"fasta")
seq_objectM_5 = SeqIO.read(path+'/'+'Mutated_0.2_5.fasta',"fasta")
seq_objectM_6 = SeqIO.read(path+'/'+'Mutated_0.2_6.fasta',"fasta")
seq_objectM_7 = SeqIO.read(path+'/'+'Mutated_0.2_7.fasta',"fasta")
seq_objectM_8 = SeqIO.read(path+'/'+'Mutated_0.2_8.fasta',"fasta")
seq_objectM_9 = SeqIO.read(path+'/'+'Mutated_0.2_9.fasta',"fasta")
seq_objectM_10 = SeqIO.read(path+'/'+'Mutated_0.2_10.fasta',"fasta")
seq_objectM_11 = SeqIO.read(path+'/'+'Mutated_0.2_11.fasta',"fasta")
seq_objectM_12 = SeqIO.read(path+'/'+'Mutated_0.2_12.fasta',"fasta")
seq_objectM_13 = SeqIO.read(path+'/'+'Mutated_0.2_13.fasta',"fasta")
seq_objectM_14 = SeqIO.read(path+'/'+'Mutated_0.2_14.fasta',"fasta")
seq_objectM_15 = SeqIO.read(path+'/'+'Mutated_0.2_15.fasta',"fasta")
seq_objectM_16 = SeqIO.read(path+'/'+'Mutated_0.2_16.fasta',"fasta")
seq_objectM_17 = SeqIO.read(path+'/'+'Mutated_0.2_17.fasta',"fasta")
seq_objectM_18 = SeqIO.read(path+'/'+'Mutated_0.2_18.fasta',"fasta")
seq_objectM_19 = SeqIO.read(path+'/'+'Mutated_0.2_19.fasta',"fasta")
seq_objectM_20 = SeqIO.read(path+'/'+'Mutated_0.2_20.fasta',"fasta")


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



rbar0_01 = rbarCal(R_seq, seq_objectM_1.seq)
rbar0_02 = rbarCal(R_seq, seq_objectM_2.seq)
rbar0_03 = rbarCal(R_seq, seq_objectM_3.seq)
rbar0_04 = rbarCal(R_seq, seq_objectM_4.seq)
rbar0_05 = rbarCal(R_seq, seq_objectM_5.seq)
rbar0_06 = rbarCal(R_seq, seq_objectM_6.seq)
rbar0_07 = rbarCal(R_seq, seq_objectM_7.seq)
rbar0_08 = rbarCal(R_seq, seq_objectM_8.seq)
rbar0_09 = rbarCal(R_seq, seq_objectM_9.seq)
rbar0_010 = rbarCal(R_seq, seq_objectM_10.seq)
rbar0_011 = rbarCal(R_seq, seq_objectM_11.seq)
rbar0_012 = rbarCal(R_seq, seq_objectM_12.seq)
rbar0_013 = rbarCal(R_seq, seq_objectM_13.seq)
rbar0_014 = rbarCal(R_seq, seq_objectM_14.seq)
rbar0_015 = rbarCal(R_seq, seq_objectM_15.seq)
rbar0_016 = rbarCal(R_seq, seq_objectM_16.seq)
rbar0_017 = rbarCal(R_seq, seq_objectM_17.seq)
rbar0_018 = rbarCal(R_seq, seq_objectM_18.seq)
rbar0_019 = rbarCal(R_seq, seq_objectM_19.seq)
rbar0_020 = rbarCal(R_seq, seq_objectM_20.seq)



rbaBar0_01 = pd.DataFrame({'rbaBar0_1': [rbar0_01, rbar0_02, rbar0_03, rbar0_04,
                                              rbar0_05, rbar0_06, rbar0_07, rbar0_08,
                                              rbar0_09, rbar0_010, rbar0_011, rbar0_012,
                                              rbar0_013, rbar0_014, rbar0_015, rbar0_016,
                                              rbar0_017, rbar0_018, rbar0_019, rbar0_020]})




