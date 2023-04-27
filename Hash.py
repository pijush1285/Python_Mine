# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 16:50:50 2022

@author: PIJHUSH
"""
#K-mer
print(hash('TACGG' * 1000))
print(hash('TTACG' * 1000))
print(hash('TTTAC' * 1000))
print(hash('GTTTA' * 1000))
print(hash('TGTTT' * 1000))
print(hash('GTGTT' * 1000))
print(hash('AGTGT' * 1000))
print(hash('CAGTG' * 1000))
print(hash('CCAGT' * 1000))

#s-mer # This is satisfied Figure 1 in duttas paper
import random
random.seed(31415)
print(hash('TT'))
print(hash('TA'))
print(hash('AC'))
print(hash('CG'))

print(hash('CC'))
print(hash('CA'))
print(hash('AG'))
print(hash('GT'))


import random


def murmur64(k):  # also known as fmix64
    k ^= k >> 33
    k *= 0xff51afd7ed558ccd
    k %= 2 ** 64
    k ^= k >> 33
    k *= 0xc4ceb9fe1a85ec53
    k %= 2 ** 64
    k ^= k >> 33
    return k

alphabet = "acgt"
def seqCodeMurmur64(seq):
    a = len(alphabet)
    h = 0
    for i in seq:
        h = h * a + i
    assert h < 2 ** 64
    return murmur64(h)

print(seqCodeMurmur64('CC'))




# Parameterized syncmer

Str='CCAGTGTTTACGGCCAGT'


def count_kmers(read, k):
    counts = {}
    num_kmers = len(read) - k + 1
    for i in range(num_kmers):
        kmer = read[i:i+k]
        if kmer not in counts:
            counts[kmer] = 0
        counts[kmer] += 1
    return counts


count_kmers("GATGAT",3)
count_kmers(Str,5)
smer = count_kmers("CCAGT",2)






read = 'CCAGTGTTTACGG'
#import random
#random.seed(31415)
k = 5
s = 2
t = 2
counts = {}
hasVal = {}
num_kmers = len(read) - k + 1
for i in range(num_kmers):
    kmer = read[i:i+k]
    print("K-mer:",kmer, i)  
    num_smer = len(kmer) - s + 1
    for j in range(num_smer):
        smer = kmer[j:j+s]
        hasVal[j] = hash(smer)
        print(smer, j, hash(smer) )       
    dict_val = list(hasVal.values())    
    t_position = dict_val.index(min(hasVal.values())) 
    print("t-position:",  t_position)  
    if t == t_position:
        print("Selected k-mer:",kmer)
        if kmer not in counts:
            counts[kmer] = 0
        counts[kmer] += 1
        
    
        
     
min(hasVal[0], hasVal[1], hasVal[2], hasVal[3] )
print(counts)
min(hasVal.values())
min(hasVal.keys())     


     
dict_key = list(hasVal.keys())
dict_val = list(hasVal.values())    
my_position = dict_val.index(min(hasVal.values()))



# cd C:\\Users\\PIJHUSH\\Desktop\\Python with Spyder
# run dna-seed-sim-New.py -m10 -M10 --syn-window=8 -s3 --seeds Mutated.fasta
# run dna-seed-sim-New.py -m5 -M5 --syn-window=4 -s2 --seeds Mutated.fasta

# Open Syncmer
# run dna-seed-sim-New.py -m10 -M10 --syn-window=8 -s3 --syn-offset=0 --seeds Mutated.fasta
# run dna-seed-sim-New.py -m10 -M10 --syn-window=8 -s3 --syn-offset=1 --seeds Mutated.fasta
# run dna-seed-sim-New.py -m10 -M10 --syn-window=8 -s3 --syn-offset=2 --seeds Mutated.fasta

# run dna-seed-sim-New.py -m10 -M10 --syn-window=8 -s3 --syn-offset=5 --seeds Mutated.fasta
# run dna-seed-sim-New.py -m20 -M20 --syn-window=15 -s6 --syn-offset=10 --seeds Mutated.fasta

# run dna-seed-sim-New.py -m20 -M20 --syn-window=18 -s3 --syn-offset=10 --seeds Mutated.fasta



# This is the function of de Bruijn graph taken from the website given below.
# https://eaton-lab.org/slides/genomics/answers/nb-10.2-de-Bruijn.html
def get_debruijn_edges_from_kmers(kmers):
    """
    Every possible (k-1)mer (n-1 suffix and prefix of kmers) is assigned
    to a node, and we connect one node to another if the (k-1)mer overlaps 
    another. Nodes are (k-1)mers, edges are kmers.
    """
    # store edges as tuples in a set
    edges = set()
    
    # compare each (k-1)mer
    for k1 in kmers:
        for k2 in kmers:
            if k1 != k2:            
                # if they overlap then add to edges
                if k1[1:] == k2[:-1]:
                    edges.add((k1[:-1], k2[:-1]))
                if k1[:-1] == k2[1:]:
                    edges.add((k2[:-1], k1[:-1]))

    return edges
