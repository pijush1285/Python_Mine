# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 15:40:46 2021

@author: PIJHUSH
"""

#First install the package named pyfaidx using the code below.
#pip install pyfaidx
from pyfaidx import Fasta

genes = Fasta('C:/Users/PIJHUSH/Desktop/John/Toy_Taxonomy/erickson_accessions.fasta')

for line in genes['NZ_CP028341']:
   print(line)