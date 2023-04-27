# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 22:26:47 2023

@author: PIJHUSH
"""

import subprocess

cmd1 =  "python SeedandTheta_v5.py -k10 -s2 -t1"
cmd2 =  "python SeedandTheta_v5.py -k10 -s3 -t1"
cmd3 =  "python SeedandTheta_v5.py -k10 -s4 -t1"
cmd4 =  "python SeedandTheta_v5.py -k10 -s5 -t1"
cmd5 =  "python SeedandTheta_v5.py -k10 -s6 -t1"
cmd6 =  "python SeedandTheta_v5.py -k10 -s7 -t1"
cmd7 =  "python SeedandTheta_v5.py -k10 -s8 -t1"
cmd8 =  "python SeedandTheta_v5.py -k10 -s9 -t1"
cmd9 =  "python SeedandTheta_v5.py -k15 -s2 -t1"
cmd10 =  "python SeedandTheta_v5.py -k15 -s3 -t1"

# Execute the first command
subprocess.run(cmd1, shell=True)
subprocess.run(cmd2, shell=True)
subprocess.run(cmd3, shell=True)
subprocess.run(cmd4, shell=True)
subprocess.run(cmd5, shell=True)
subprocess.run(cmd6, shell=True)
subprocess.run(cmd7, shell=True)
subprocess.run(cmd8, shell=True)
subprocess.run(cmd9, shell=True)
subprocess.run(cmd10, shell=True)
