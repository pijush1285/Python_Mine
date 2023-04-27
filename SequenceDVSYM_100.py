# -*- coding: utf-8 -*-
"""
Created on Fri May  6 08:08:08 2022

@author: PIJHUSH
Read multiple csv file.
"""


# Import libraries
import glob
import pandas as pd
import csv


data = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/RawSequence/RawCSseed.csv")

# Get CSV files list from a folder
path = 'C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Seed/csv'
path = 'C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.1/CSMSeed/csv'
path = 'C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.2/CSMSeed/csv'
csv_files = glob.glob(path + "/*.csv")


######################################################

# Find out common closed syncmer between raw and mutated sequence.
def common(RawClosedSyncmerSeq, mutClosedSyncmerSeq):
    CommonArray1 = []
    CommonArray2 = []
    start        = []
    count = 0
    for i in range(len(RawClosedSyncmerSeq)):
        if(RawClosedSyncmerSeq['sequence'][i] == mutClosedSyncmerSeq['sequence'][i]):
            start.append(RawClosedSyncmerSeq['# start'][i])
            CommonArray1.append(RawClosedSyncmerSeq['sequence'][i])
            CommonArray2.append(mutClosedSyncmerSeq['sequence'][i])
            count += 1
    cdata = {'start': start,'FromRawSeq': CommonArray1, 'MutatedSSeq': CommonArray2 }
    cdf = pd.DataFrame(cdata)
    count2 = len(RawClosedSyncmerSeq)
    return(count, count2, cdf)



# calculating theta bar
CSN = []
nSM = []
cTB = []

for i in range(len(csv_files)):
    #print(csv_files[i])
    #data001_next = pd.read_csv(csv_files[i]) 
    kmers = 20
    CommonSyncmerNumber , numberSMunmut, CommonSyncmer = common(data, pd.read_csv(csv_files[i]))
    thetabar = 1 - (CommonSyncmerNumber/numberSMunmut)**(1/kmers)
    #print(CommonSyncmerNumber, numberSMunmut)
    print(thetabar)
    CSN.append(CommonSyncmerNumber)
    nSM.append(numberSMunmut)
    cTB.append(thetabar)
    
print(CSN)
print(nSM)
print(cTB)






# open the file in the write mode
outpath = 'C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Seed'
f = open(outpath +'/resultsThetabar3.csv', 'w')
writer = csv.writer(f)
writer.writerow(cTB)
f.close()



