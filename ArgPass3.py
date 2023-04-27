# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 00:18:14 2022

@author: PIJHUSH
"""

import sys
import getopt
from Bio import SeqIO
from random       import Random,seed as random_seed, \
                         random as unit_random, \
                         choice as random_choice, \
                         sample as random_sample
#from random import random, choice


def fasta_iter(fasta_name):
    """
    given a fasta file. yield tuples of header, sequence
    """ 
    seq_object=SeqIO.read(fasta_name,"fasta")
    header=seq_object.id
    seq=seq_object.seq[0:20]
    yield header, seq



def main(argv):
    arg_input = ""
    arg_output = ""
    arg_user = ""
    header   = ""
    arg_help = "{0} -i <input> -u <user> -o <output>".format(argv[0])
    
    try:
        opts, args = getopt.getopt(argv[1:], "hi:u:o:", ["help", "input=", 
        "user=", "output=", "header="])
    except:
        print(arg_help)
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)  # print the help message
            sys.exit(2)
        elif opt in ("-i", "--input"):
            arg_input = arg
        elif opt in ("-u", "--user"):
            arg_user = arg
        elif opt in ("-o", "--output"):
            arg_output = arg

    print('input:', arg_input)
    print('user:', arg_user)
    print('output:', arg_output)
    
    out=fasta_iter(arg_input)
    print('input:', arg_input)
    print('Sequence id:', out.header)


if __name__ == "__main__":
    main(sys.argv)