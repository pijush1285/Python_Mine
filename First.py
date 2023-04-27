# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

           
print("Hello World")

def jaccard_similarity(a, b):
    a = set(a)
    b = set(b)

    intersection = len(a.intersection(b))
    union = len(a.union(b))

    return intersection / union

def jaccard_containment(a, b):
    a = set(a)
    b = set(b)

    intersection = len(a.intersection(b))

    return intersection / len(a)


a = ['ATGG', 'AACC']
b = ['ATGG', 'CACA']
c = ['ATGC', 'CACA']


jaccard_similarity(a, a)
jaccard_similarity(b, a)


#matplotlib inline
# This is the way to install a package or module in python.
# pip install matplotlib-venn
from matplotlib_venn import venn2, venn3

venn2([set(a), set(b)])

venn2(subsets = (30, 10, 8), set_labels = ('Group A', 'Group B'))

venn3([set(a), set(b), set(c)])


def build_kmers(sequence, ksize):
    kmers = []
    n_kmers = len(sequence) - ksize + 1

    for i in range(n_kmers):
        kmer = sequence[i:i + ksize]
        kmers.append(kmer)

    return kmers

build_kmers('ATGGACCAGATATAGGGAGAGCCAGGTAGGACA', 21)


seq1 = 'ATGGACCAGATATAGGGAGAGCCAGGTAGGACA'
seq2 = 'ATGGACCAGATATTGGGAGAGCCGGGTAGGACA'


K = 10
kmers1 = build_kmers(seq1, K)
kmers2 = build_kmers(seq2, K)

print(K, jaccard_similarity(kmers1, kmers2))



