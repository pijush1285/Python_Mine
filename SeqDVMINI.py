# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 16:59:13 2022

@author: PIJHUSH
"""

import pandas as pd

# Reading the minimizer (k-mers = 20, window=25) from raw sequence.
data = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/RawSequence/RawMinimizerSeed.csv")  


# Reading the minimizer (k-mers = 20, window=25) from p=0.01 mutated sequence.
path='C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/MininizerSeed/csv'
data001_1 = pd.read_csv(path+'/'+'MMseed0.01_1.csv')
data001_2 = pd.read_csv(path+'/'+'MMseed0.01_2.csv')
data001_3 = pd.read_csv(path+'/'+'MMseed0.01_3.csv')
data001_4 = pd.read_csv(path+'/'+'MMseed0.01_4.csv')
data001_5 = pd.read_csv(path+'/'+'MMseed0.01_5.csv')
data001_6 = pd.read_csv(path+'/'+'MMseed0.01_6.csv')
data001_7 = pd.read_csv(path+'/'+'MMseed0.01_7.csv')
data001_8 = pd.read_csv(path+'/'+'MMseed0.01_8.csv')
data001_9 = pd.read_csv(path+'/'+'MMseed0.01_9.csv')
data001_10 = pd.read_csv(path+'/'+'MMseed0.01_10.csv')
data001_11 = pd.read_csv(path+'/'+'MMseed0.01_11.csv')
data001_12 = pd.read_csv(path+'/'+'MMseed0.01_12.csv')
data001_13 = pd.read_csv(path+'/'+'MMseed0.01_13.csv')
data001_14 = pd.read_csv(path+'/'+'MMseed0.01_14.csv')
data001_15 = pd.read_csv(path+'/'+'MMseed0.01_15.csv')
data001_16 = pd.read_csv(path+'/'+'MMseed0.01_16.csv')
data001_17 = pd.read_csv(path+'/'+'MMseed0.01_17.csv')
data001_18 = pd.read_csv(path+'/'+'MMseed0.01_18.csv')
data001_19 = pd.read_csv(path+'/'+'MMseed0.01_19.csv')
data001_20 = pd.read_csv(path+'/'+'MMseed0.01_20.csv')


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
    count2 = len(mutClosedSyncmerSeq)
    return(count, count2, cdf)


        
# Getting the return values in to variables.
CommonSyncmerNumber1 , numberSMunmut1, CommonSyncmer1 = common(data, data001_1)
CommonSyncmerNumber2 , numberSMunmut2, CommonSyncmer2 = common(data, data001_2)
CommonSyncmerNumber3 , numberSMunmut3, CommonSyncmer3 = common(data, data001_3)
CommonSyncmerNumber4 , numberSMunmut4, CommonSyncmer4 = common(data, data001_4)
CommonSyncmerNumber5 , numberSMunmut5, CommonSyncmer5 = common(data, data001_5)
CommonSyncmerNumber6 , numberSMunmut6, CommonSyncmer6 = common(data, data001_6)
CommonSyncmerNumber7 , numberSMunmut7, CommonSyncmer7 = common(data, data001_7)
CommonSyncmerNumber8 , numberSMunmut8, CommonSyncmer8 = common(data, data001_8)
CommonSyncmerNumber9 , numberSMunmut9, CommonSyncmer9 = common(data, data001_9)
CommonSyncmerNumber10 , numberSMunmut10, CommonSyncmer10 = common(data, data001_10)
CommonSyncmerNumber11 , numberSMunmut11, CommonSyncmer11 = common(data, data001_11)
CommonSyncmerNumber12 , numberSMunmut12, CommonSyncmer12 = common(data, data001_12)
CommonSyncmerNumber13 , numberSMunmut13, CommonSyncmer13 = common(data, data001_13)
CommonSyncmerNumber14 , numberSMunmut14, CommonSyncmer14 = common(data, data001_14)
CommonSyncmerNumber15 , numberSMunmut15, CommonSyncmer15 = common(data, data001_15)
CommonSyncmerNumber16 , numberSMunmut16, CommonSyncmer16 = common(data, data001_16)
CommonSyncmerNumber17 , numberSMunmut17, CommonSyncmer17 = common(data, data001_17)
CommonSyncmerNumber18 , numberSMunmut18, CommonSyncmer18 = common(data, data001_18)
CommonSyncmerNumber19 , numberSMunmut19, CommonSyncmer19 = common(data, data001_19)
CommonSyncmerNumber20 , numberSMunmut20, CommonSyncmer20 = common(data, data001_20)





