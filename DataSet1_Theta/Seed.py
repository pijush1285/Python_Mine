# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 11:53:43 2023

@author: PIJHUSH

The code is used for producing the seeds.


"""



import subprocess
import csv
import os


kmer = 21
smer = 6
window = 16
InputDirectory ='D:/JohnAllfromNIH/BackupArchive/Table3/1_Dataset_0.1kby1k/'

# Relative path to your Python code
a_py_path = 'D:/JohnAllfromNIH/BackupArchive/packages/noverlap/bin/dna-seed-sim'



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
dir1 = '1_Raw_seed'
dir2 = '2_Mutated_0.05_seed'
dir3 = '3_Mutated_0.15_seed'
dir4 = '4_Mutated_0.25_seed'
path = os.getcwd()+'/seedsk'+ str(kmer) +'s'+ str(smer)+'/'

# Create the directories
os.makedirs(os.path.join(path, dir1))
os.makedirs(os.path.join(path, dir2))
os.makedirs(os.path.join(path, dir3))
os.makedirs(os.path.join(path, dir4))





count = 1
for i in range(10):
    # Relative path to your input file
    input_file_path = InputDirectory+'Raw_Fasta/RGID_' + str(count) + '.fasta'
    #For open syncmer
    #result = subprocess.run(['python', a_py_path, '-m'+ str(kmer), '-M'+ str(kmer), '--syn-window='+ str(window), '-s2'+ str(smer), '--syn-offset=5', '--seeds', input_file_path], capture_output=True, text=True)
    #For closed syncmer verifing code.
    result = subprocess.run(['python', a_py_path, '-m'+ str(kmer), '-M'+ str(kmer), '--syn-window='+ str(window), '-s2'+ str(smer), '--seeds', input_file_path], capture_output=True, text=True)

    # Print the result to the console
    print(result.stdout)

    cwd = os.getcwd()
    main_output_dir = directory_name
    sub_dir = dir1
    absolute_output_path = os.path.join(cwd, main_output_dir,sub_dir)
    # Open the CSV file for writing
    with open(absolute_output_path +'/RawSeed_'+str(count)+'.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write each line of the output to a separate row in the CSV file
        for line in result.stdout.split('\n'):
                writer.writerow([line])
                
                
            
    # Relative path to your input file
    input_file_path1 = InputDirectory+'Mutated_0.05/Mutated/Mutated_' + str(count) + '.fasta'
    #result1 = subprocess.run(['python', a_py_path, '-m'+ str(kmer), '-M'+ str(kmer), '--syn-window='+ str(window), '-s2'+ str(smer), '--syn-offset=5', '--seeds', input_file_path1], capture_output=True, text=True)
    #For closed syncmer verifing code.
    result1 = subprocess.run(['python', a_py_path, '-m'+ str(kmer), '-M'+ str(kmer), '--syn-window='+ str(window), '-s2'+ str(smer), '--seeds', input_file_path1], capture_output=True, text=True)
    # Print the result to the console
    print(result1.stdout)     
                
    
    #cwd = os.getcwd()
    #main_output_dir = directory_name
    sub_dir1 = dir2
    absolute_output_path1 = os.path.join(cwd, main_output_dir,sub_dir1)
    # Open the CSV file for writing
    with open(absolute_output_path1 +'/Mut_0.05Seed_'+str(count)+'.csv', 'w', newline='') as csvfile1:
        writer = csv.writer(csvfile1)
        # Write each line of the output to a separate row in the CSV file
        for line in result1.stdout.split('\n'):
                writer.writerow([line])
    
    
    
    # Relative path to your input file
    input_file_path2 = InputDirectory+'Mutated_0.15/Mutated/Mutated_' + str(count) + '.fasta'
    #result2 = subprocess.run(['python', a_py_path, '-m'+ str(kmer), '-M'+ str(kmer), '--syn-window='+ str(window), '-s2'+ str(smer), '--syn-offset=5', '--seeds', input_file_path2], capture_output=True, text=True)
    #For closed syncmer verifing code.
    result2 = subprocess.run(['python', a_py_path, '-m'+ str(kmer), '-M'+ str(kmer), '--syn-window='+ str(window), '-s2'+ str(smer), '--seeds', input_file_path2], capture_output=True, text=True)
    
    # Print the result to the console
    print(result2.stdout)    
    
    
    #cwd = os.getcwd()
    #main_output_dir = directory_name
    sub_dir2 = dir3
    absolute_output_path2 = os.path.join(cwd, main_output_dir,sub_dir2)
    # Open the CSV file for writing
    with open(absolute_output_path2 +'/Mut_0.15Seed_'+str(count)+'.csv', 'w', newline='') as csvfile2:
        writer = csv.writer(csvfile2)
        # Write each line of the output to a separate row in the CSV file
        for line in result2.stdout.split('\n'):
                writer.writerow([line])
    
    
    
    
    # Relative path to your input file
    input_file_path3 = InputDirectory+'Mutated_0.25/Mutated/Mutated_' + str(count) + '.fasta'
    #result3 = subprocess.run(['python', a_py_path, '-m'+ str(kmer), '-M'+ str(kmer), '--syn-window='+ str(window), '-s2'+ str(smer), '--syn-offset=5', '--seeds', input_file_path3], capture_output=True, text=True)
    #For closed syncmer verifing code.
    result3 = subprocess.run(['python', a_py_path, '-m'+ str(kmer), '-M'+ str(kmer), '--syn-window='+ str(window), '-s2'+ str(smer), '--seeds', input_file_path3], capture_output=True, text=True)
    
    
    # Print the result to the console
    print(result3.stdout)    
    
    
    #cwd = os.getcwd()
    #main_output_dir = directory_name
    sub_dir3 = dir4
    absolute_output_path3 = os.path.join(cwd, main_output_dir,sub_dir3)
    # Open the CSV file for writing
    with open(absolute_output_path3 +'/Mut_0.25Seed_'+str(count)+'.csv', 'w', newline='') as csvfile3:
        writer = csv.writer(csvfile3)
        # Write each line of the output to a separate row in the CSV file
        for line in result3.stdout.split('\n'):
                writer.writerow([line])
                
    
    print('###############Completed###############')
    print(count)
    count = count + 1
