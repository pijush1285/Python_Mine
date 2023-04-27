
import pandas as pd
import sys
import os
# This path is used for server.
sys.path.append('/home/dasp5/packages/submer-central-limit-theorem/modules')
# This path will be used for local machine.
#sys.path.append('C:/Users/PIJHUSH/Desktop/John/Codes/main')
from argparse import ArgumentParser, RawTextHelpFormatter
import jls_submer_clt_mgr
from jls_submer_to_interval_util import to_theta_interval



# Get the file path, variable, and output file name arguments from sys.argv
file1_path = sys.argv[1]
file2_path = sys.argv[2]
var1_value = sys.argv[3]
var2_value = sys.argv[4]


print("file1_path:", file1_path)
print("file2_path:", file2_path)
print("var1_value:", var1_value)
print("var2_value:", var2_value)




# Define a data frame where the selected data Will be kept.
df = pd.DataFrame()  

#For loop
count = 1
for xx in range(10):
    #Raw Seed file read.
    RawSeed = pd.read_csv(file1_path+"/1_Raw_seed/RawSeed_"+str(count)+".csv",header=1, sep='\t') 
    #RawSeed = pd.read_csv("/home/dasp5/dataset/Table3/1_Dataset_0.1kby1k/seeds/1_Raw_seed/RawSeed_"+str(count)+".csv",header=1, sep='\t') 
    # Mutated file read.
    MutSeed = pd.read_csv(file1_path+"/2_Mutated_0.05_seed/Mut_0.05Seed_"+str(count)+".csv",header=1,sep='\t')
    # Find out the common sequence between raw and mutated sequence file.
    # This is the number of the mutated file's sequence that does not include the mutation.
    #df3=pd.merge(RawSeed,MutSeed, how='inner') # This code also can be used.
    df3=pd.merge(RawSeed['sequence'],MutSeed['sequence'], how='inner')
    count_of_submers = len(MutSeed) # NUMBER_OF_SUBMERS
    count_of_unmutated_syncmers = len(df3) #NUMBER_OF_UNMUTATED_SUBMERS
    confidence = 0.95
    alpha_0 = 1.0 - confidence # for consistency with z-score
    #length = argument.length
    k = var1_value
    s = var2_value
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
    df = df.append(df1, ignore_index=True)
    print("###############Completed###############")
    print(count)
    count = count + 1
    
    
 #Write all records
directory_path = file2_path
fileName1 = 'Thetak10s3P0.05_n1000.txt'
fileName2 = 'Thetak10s3P0.05_n1000.xlsx'
file_path1 = os.path.join(directory_path, fileName1)
file_path2 = os.path.join(directory_path, fileName2)
df.to_csv(file_path1)
df.to_excel(file_path2) 

#df.to_excel(file2_path+"/Thetak10s3P0.05_n1000.xlsx") 
#df.to_csv(file2_path+"/Thetak10s3P0.05_n1000.txt") 
    


