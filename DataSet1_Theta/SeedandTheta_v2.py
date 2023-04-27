# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 11:53:43 2023

@author: PIJHUSH

The code is used for producing the seeds.
This virson will include the theta calculation with the seed calculation.
In this virson I will not write the values of seed which will generate during the program.
Now I have added a progress bar with the program let see what happened.


"""


import pandas as pd
import subprocess
#import csv
import os
import io
import sys
from tqdm import tqdm


########################################################################################################

# This path is used for server.
sys.path.append('C:/Users/PIJHUSH/Desktop/John/Codes/main')                     # Location in my computer
#sys.path.append('/home/dasp5/packages/submer-central-limit-theorem/modules')   # Do not use it .Location in the server
#sys.path.append('/home/dasp5/packages/submer-central-limit-theorem-Oldv0')     # Location in the server

# Those are the mandatory input which need to take care when run the program.
# I must put the program the current directory. Please change the directory path 
# according the current directory.
kmer = 21
smer = 6
window = 16
#t = 5                 # Used for Open Syncmer 
InputDirectory = 'D:/JohnAllfromNIH/BackupArchive/Table3/1_Dataset_0.1kby1k/'   # Location in my computer
#InputDirectory = '/home/dasp5/dataset/Table3/1_Dataset_0.1kby1k/'               # Location in the server


# Relative path to your Python code. This the path for the novolap package.
a_py_path = 'D:/JohnAllfromNIH/BackupArchive/packages/noverlap/bin/dna-seed-sim'  # Location in my computer
#a_py_path = '/home/dasp5/packages/noverlap/bin/dna-seed-sim'                     # Location in the server

########################################################################################################


#From argparse import ArgumentParser, RawTextHelpFormatter
import jls_submer_clt_mgr
from jls_submer_to_interval_util import to_theta_interval


# First check where the current directory is residing. If find else where then
os.chdir(InputDirectory)
# print the current working directory to confirm the change
print("Current working directory:", os.getcwd())


# Define the directory name and path
directory_name = 'seedsk'+ str(kmer) +'s'+ str(smer)
directory_path = os.getcwd()+'/'
# Get the current working directory
cwd = os.getcwd()

# Create the new directory
os.makedirs(directory_path + directory_name, exist_ok=True)

# Define the directory names and path
# dir1 = '1_Raw_seed'
# dir2 = '2_Mutated_0.05_seed'
# dir3 = '3_Mutated_0.15_seed'
# dir4 = '4_Mutated_0.25_seed'
dir5 =  'Theta'
path = os.getcwd()+'/seedsk'+ str(kmer) +'s'+ str(smer)+'/'

# Create the directories
# os.makedirs(os.path.join(path, dir1))
# os.makedirs(os.path.join(path, dir2))
# os.makedirs(os.path.join(path, dir3))
# os.makedirs(os.path.join(path, dir4))
os.makedirs(os.path.join(path, dir5))



df1r = pd.DataFrame()  
df2r = pd.DataFrame() 
df3r = pd.DataFrame()
count = 1
for i in tqdm(range(1000)):
    # Relative path to your input file
    input_file_path = InputDirectory+'Raw_Fasta/RGID_' + str(count) + '.fasta'
    #For open syncmer
    #result = subprocess.run(['python', a_py_path, '-m'+ str(kmer), '-M'+ str(kmer), '--syn-window='+ str(window), '-s2'+ str(smer), '--syn-offset='+str(t), '--seeds', input_file_path], capture_output=True, text=True)
    #For closed syncmer verifing code.
    result = subprocess.run(['python', a_py_path, '-m'+ str(kmer), '-M'+ str(kmer), '--syn-window='+ str(window), '-s2'+ str(smer), '--seeds', input_file_path], capture_output=True, text=True)

    # Print the result to the console
    #print(result.stdout)

    # cwd = os.getcwd()
    # main_output_dir = directory_name
    # sub_dir = dir1
    # absolute_output_path = os.path.join(cwd, main_output_dir,sub_dir)
    # # Open the CSV file for writing
    # with open(absolute_output_path +'/RawSeed_'+str(count)+'.csv', 'w', newline='') as csvfile:
    #     writer = csv.writer(csvfile)
    #     # Write each line of the output to a separate row in the CSV file
    #     for line in result.stdout.split('\n'):
    #             writer.writerow([line])
                
                
            
    # Relative path to your input file
    input_file_path1 = InputDirectory+'Mutated_0.05/Mutated/Mutated_' + str(count) + '.fasta'
    #result1 = subprocess.run(['python', a_py_path, '-m'+ str(kmer), '-M'+ str(kmer), '--syn-window='+ str(window), '-s2'+ str(smer), '--syn-offset='+str(t), '--seeds', input_file_path1], capture_output=True, text=True)
    #For closed syncmer verifing code.
    result1 = subprocess.run(['python', a_py_path, '-m'+ str(kmer), '-M'+ str(kmer), '--syn-window='+ str(window), '-s2'+ str(smer), '--seeds', input_file_path1], capture_output=True, text=True)
    # Print the result to the console
    #print(result1.stdout)     
                
    
    #cwd = os.getcwd()
    #main_output_dir = directory_name
    # sub_dir1 = dir2
    # absolute_output_path1 = os.path.join(cwd, main_output_dir,sub_dir1)
    # # Open the CSV file for writing
    # with open(absolute_output_path1 +'/Mut_0.05Seed_'+str(count)+'.csv', 'w', newline='') as csvfile1:
    #     writer = csv.writer(csvfile1)
    #     # Write each line of the output to a separate row in the CSV file
    #     for line in result1.stdout.split('\n'):
    #             writer.writerow([line])
    
    
    
    # Relative path to your input file
    input_file_path2 = InputDirectory+'Mutated_0.15/Mutated/Mutated_' + str(count) + '.fasta'
    #result2 = subprocess.run(['python', a_py_path, '-m'+ str(kmer), '-M'+ str(kmer), '--syn-window='+ str(window), '-s2'+ str(smer), '--syn-offset='+str(t), '--seeds', input_file_path2], capture_output=True, text=True)
    #For closed syncmer verifing code.
    result2 = subprocess.run(['python', a_py_path, '-m'+ str(kmer), '-M'+ str(kmer), '--syn-window='+ str(window), '-s2'+ str(smer), '--seeds', input_file_path2], capture_output=True, text=True)
    
    # Print the result to the console
    #print(result2.stdout)    
    
    
    #cwd = os.getcwd()
    #main_output_dir = directory_name
    # sub_dir2 = dir3
    # absolute_output_path2 = os.path.join(cwd, main_output_dir,sub_dir2)
    # # Open the CSV file for writing
    # with open(absolute_output_path2 +'/Mut_0.15Seed_'+str(count)+'.csv', 'w', newline='') as csvfile2:
    #     writer = csv.writer(csvfile2)
    #     # Write each line of the output to a separate row in the CSV file
    #     for line in result2.stdout.split('\n'):
    #             writer.writerow([line])
    
    
    
    
    # Relative path to your input file
    input_file_path3 = InputDirectory+'Mutated_0.25/Mutated/Mutated_' + str(count) + '.fasta'
    #result3 = subprocess.run(['python', a_py_path, '-m'+ str(kmer), '-M'+ str(kmer), '--syn-window='+ str(window), '-s2'+ str(smer), '--syn-offset='+str(t), '--seeds', input_file_path3], capture_output=True, text=True)
    #For closed syncmer verifing code.
    result3 = subprocess.run(['python', a_py_path, '-m'+ str(kmer), '-M'+ str(kmer), '--syn-window='+ str(window), '-s2'+ str(smer), '--seeds', input_file_path3], capture_output=True, text=True)
    
    
    # Print the result to the console
    #print(result3.stdout)    
    
    
    #cwd = os.getcwd()
    #main_output_dir = directory_name
    # sub_dir3 = dir4
    # absolute_output_path3 = os.path.join(cwd, main_output_dir,sub_dir3)
    # # Open the CSV file for writing
    # with open(absolute_output_path3 +'/Mut_0.25Seed_'+str(count)+'.csv', 'w', newline='') as csvfile3:
    #     writer = csv.writer(csvfile3)
    #     # Write each line of the output to a separate row in the CSV file
    #     for line in result3.stdout.split('\n'):
    #             writer.writerow([line])
    
    
    
    # Find out the common sequence between raw and mutated sequence file.
    # This is the number of the mutated file's sequence that does not include the mutation.
      
    RawSeed = pd.read_csv(io.StringIO(result.stdout),header=1, sep='\t') 
    MutSeed = pd.read_csv(io.StringIO(result1.stdout),header=1, sep='\t') 
    
    #print(RawSeed)
    df3 = pd.merge(RawSeed['sequence'],MutSeed['sequence'], how='inner')
    
    
    count_of_submers = len(MutSeed) # NUMBER_OF_SUBMERS
    count_of_unmutated_syncmers = len(df3) #NUMBER_OF_UNMUTATED_SUBMERS
    confidence = 0.95
    alpha_0 = 1.0 - confidence # for consistency with z-score
    #length = argument.length
    k = kmer
    s = smer
    
    try:
        h = jls_submer_clt_mgr.to_syncmer_closed_Wilson_score_intervals_for_theta( count_of_submers, count_of_unmutated_syncmers, alpha_0, k, s) #, length 
        interval = to_theta_interval( h )
    except:
        interval = [None, None]  
    # Catch the process data in a frame.
    df1 = pd.DataFrame({'k-mer' : [k],
               's-mer': [s],
               'Number_of_submer' : [count_of_submers],
               'Number_of_UnmutSubmer' : [count_of_unmutated_syncmers],
               'ThetaLow' : interval[0],
               'ThetaHigh' : interval[1],
               'filename': ["Mut_0.05Seed_"+str(count)+".csv"]})
    #df1r = df1r.append(df1, ignore_index=True)
    df1r = pd.concat([df1r, df1], ignore_index=True)
    
    
    
    MutSeed1 = pd.read_csv(io.StringIO(result2.stdout),header=1, sep='\t') 
    
    
    df4=pd.merge(RawSeed['sequence'],MutSeed1['sequence'], how='inner')
    count_of_submers1 = len(MutSeed1) # NUMBER_OF_SUBMERS
    count_of_unmutated_syncmers1 = len(df4) #NUMBER_OF_UNMUTATED_SUBMERS
    confidence = 0.95
    alpha_0 = 1.0 - confidence # for consistency with z-score
    #length = argument.length
    #k = 21
    #s = 6
    try:
        h1 = jls_submer_clt_mgr.to_syncmer_closed_Wilson_score_intervals_for_theta( count_of_submers1, count_of_unmutated_syncmers1, alpha_0, k, s) #, length 
        interval1 = to_theta_interval( h1 )
    except:
        interval1 = [None, None]  
    # Catch the process data in a frame.
    dfm2 = pd.DataFrame({'k-mer' : [k],
               's-mer': [s],
               'Number_of_submer' : [count_of_submers1],
               'Number_of_UnmutSubmer' : [count_of_unmutated_syncmers1],
               'ThetaLow' : interval1[0],
               'ThetaHigh' : interval1[1],
               'filename': ["Mut_0.15Seed_"+str(count)+".csv"]})
    #df2r = df2r.append(dfm2, ignore_index=True)
    df2r = pd.concat([df2r, dfm2], ignore_index=True)
    
    
    
    MutSeed3 = pd.read_csv(io.StringIO(result3.stdout),header=1, sep='\t') 
    
    df5=pd.merge(RawSeed['sequence'],MutSeed3['sequence'], how='inner')
    count_of_submers2 = len(MutSeed3) # NUMBER_OF_SUBMERS
    count_of_unmutated_syncmers2 = len(df5) #NUMBER_OF_UNMUTATED_SUBMERS
    confidence = 0.95
    alpha_0 = 1.0 - confidence # for consistency with z-score
    #length = argument.length
    #k = 21
    #s = 6
    try:
        h2 = jls_submer_clt_mgr.to_syncmer_closed_Wilson_score_intervals_for_theta( count_of_submers2, count_of_unmutated_syncmers2, alpha_0, k, s) #, length 
        interval2 = to_theta_interval( h2 )
    except:
        interval2 = [None, None]  
    # Catch the process data in a frame.
    dfm3 = pd.DataFrame({'k-mer' : [k],
               's-mer': [s],
               'Number_of_submer' : [count_of_submers2],
               'Number_of_UnmutSubmer' : [count_of_unmutated_syncmers2],
               'ThetaLow' : interval2[0],
               'ThetaHigh' : interval2[1],
               'filename': ["Mut_0.25Seed_"+str(count)+".csv"]})
    #df3r = df3r.append(dfm3, ignore_index=True)
    df3r = pd.concat([df3r, dfm3], ignore_index=True)
    
    

    #print('###############Completed###############')
    #print(count)
    count = count + 1
    
    
    
    
# Write all records
absolute_output_path5 = os.path.join(cwd, directory_name, dir5)


df1r.to_excel(absolute_output_path5+"/Thetak"+str(kmer)+"s"+str(smer)+"P0.05_n1k.xlsx") 
df1r.to_csv(absolute_output_path5+"/Thetak"+str(kmer)+"s"+str(smer)+"P0.05_n1k.txt")
#Write all records
df2r.to_excel(absolute_output_path5+"/Thetak"+str(kmer)+"s"+str(smer)+"P0.15_n1k.xlsx") 
df2r.to_csv(absolute_output_path5+"/Thetak"+str(kmer)+"s"+str(smer)+"P0.15_n1k.txt") 
#Write all records
df3r.to_excel(absolute_output_path5+"/Thetak"+str(kmer)+"s"+str(smer)+"P0.25_n1k.xlsx") 
df3r.to_csv(absolute_output_path5+"/Thetak"+str(kmer)+"s"+str(smer)+"P0.25_n1k.txt") 
    