# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 15:50:59 2023

@author: PIJHUSH
"""

import argparse

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-k', '--kmer', help='Provide the value of the k-mer')
parser.add_argument('-s', '--smer', help='Provide the value of the s-mer')
parser.add_argument('-w', '--window', help='Provide the value of the window')
parser.add_argument('-t', '--offset', help='Provide the value of the offset')



args = parser.parse_args()

if args.kmer:
    print('Argument 1:', args.kmer)

if args.smer:
    print('Argument 2:', args.smer)
    
    
if args.window:
    print('Argument 3:', args.window)
    
    
if args.offset:
    print('Argument 4:', args.offset)
