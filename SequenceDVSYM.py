# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 07:19:50 2022

@author: PIJHUSH
"""


import pandas as pd

# Reading the syncmer (k-mers = 20, s=6) from raw sequence.
data = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/RawSequence/RawCSseed.csv")                

# Reading the syncmer (k-mers = 20, s=6) from p=0.01 mutated sequence.
data001_1 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Seed/csv/Mseed0.01_1.csv")
data001_2 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Seed/csv/Mseed0.01_2.csv")
data001_3 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Seed/csv/Mseed0.01_3.csv")
data001_4 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Seed/csv/Mseed0.01_4.csv")
data001_5 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Seed/csv/Mseed0.01_5.csv")
data001_6 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Seed/csv/Mseed0.01_6.csv")
data001_7 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Seed/csv/Mseed0.01_7.csv")
data001_8 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Seed/csv/Mseed0.01_8.csv")
data001_9 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Seed/csv/Mseed0.01_9.csv")
data001_10 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Seed/csv/Mseed0.01_10.csv")
data001_11 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Seed/csv/Mseed0.01_11.csv")
data001_12 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Seed/csv/Mseed0.01_12.csv")
data001_13 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Seed/csv/Mseed0.01_13.csv")
data001_14 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Seed/csv/Mseed0.01_14.csv")
data001_15 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Seed/csv/Mseed0.01_15.csv")
data001_16 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Seed/csv/Mseed0.01_16.csv")
data001_17 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Seed/csv/Mseed0.01_17.csv")
data001_18 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Seed/csv/Mseed0.01_18.csv")
data001_19 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Seed/csv/Mseed0.01_19.csv")
data001_20 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.01/Seed/csv/Mseed0.01_20.csv")




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




# Sequence divergence estimation
kmers = 20
thetabar1 = 1 - (CommonSyncmerNumber1/numberSMunmut1)**(1/kmers)
thetabar2 = 1 - (CommonSyncmerNumber2/numberSMunmut2)**(1/kmers)
thetabar3 = 1 - (CommonSyncmerNumber3/numberSMunmut3)**(1/kmers)
thetabar4 = 1 - (CommonSyncmerNumber4/numberSMunmut4)**(1/kmers)
thetabar5 = 1 - (CommonSyncmerNumber5/numberSMunmut5)**(1/kmers)
thetabar6 = 1 - (CommonSyncmerNumber6/numberSMunmut6)**(1/kmers)
thetabar7 = 1 - (CommonSyncmerNumber7/numberSMunmut7)**(1/kmers)
thetabar8 = 1 - (CommonSyncmerNumber8/numberSMunmut8)**(1/kmers)
thetabar9 = 1 - (CommonSyncmerNumber9/numberSMunmut9)**(1/kmers)
thetabar10 = 1 - (CommonSyncmerNumber10/numberSMunmut10)**(1/kmers)
thetabar11 = 1 - (CommonSyncmerNumber11/numberSMunmut11)**(1/kmers)
thetabar12 = 1 - (CommonSyncmerNumber12/numberSMunmut12)**(1/kmers)
thetabar13 = 1 - (CommonSyncmerNumber13/numberSMunmut13)**(1/kmers)
thetabar14 = 1 - (CommonSyncmerNumber14/numberSMunmut14)**(1/kmers)
thetabar15 = 1 - (CommonSyncmerNumber15/numberSMunmut15)**(1/kmers)
thetabar16 = 1 - (CommonSyncmerNumber16/numberSMunmut16)**(1/kmers)
thetabar17 = 1 - (CommonSyncmerNumber17/numberSMunmut17)**(1/kmers)
thetabar18 = 1 - (CommonSyncmerNumber18/numberSMunmut18)**(1/kmers)
thetabar19 = 1 - (CommonSyncmerNumber19/numberSMunmut19)**(1/kmers)
thetabar20 = 1 - (CommonSyncmerNumber20/numberSMunmut20)**(1/kmers)


thetabar0_01 = pd.DataFrame({'ThetaBar0_01': [thetabar1, thetabar2, thetabar3, thetabar4,
                                              thetabar5, thetabar6, thetabar7, thetabar8,
                                              thetabar9, thetabar10, thetabar11, thetabar12,
                                              thetabar13, thetabar14, thetabar15, thetabar16,
                                              thetabar17, thetabar18, thetabar19, thetabar20]})

###############################################################################
# Now working with syncmer where p=0.1

data01_1 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.1/CSMSeed/csv/Mseed0.1_1.csv")
data01_2 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.1/CSMSeed/csv/Mseed0.1_2.csv")
data01_3 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.1/CSMSeed/csv/Mseed0.1_3.csv")
data01_4 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.1/CSMSeed/csv/Mseed0.1_4.csv")
data01_5 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.1/CSMSeed/csv/Mseed0.1_5.csv")
data01_6 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.1/CSMSeed/csv/Mseed0.1_6.csv")
data01_7 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.1/CSMSeed/csv/Mseed0.1_7.csv")
data01_8 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.1/CSMSeed/csv/Mseed0.1_8.csv")
data01_9 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.1/CSMSeed/csv/Mseed0.1_9.csv")
data01_10 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.1/CSMSeed/csv/Mseed0.1_10.csv")
data01_11 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.1/CSMSeed/csv/Mseed0.1_11.csv")
data01_12 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.1/CSMSeed/csv/Mseed0.1_12.csv")
data01_13 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.1/CSMSeed/csv/Mseed0.1_13.csv")
data01_14 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.1/CSMSeed/csv/Mseed0.1_14.csv")
data01_15 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.1/CSMSeed/csv/Mseed0.1_15.csv")
data01_16 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.1/CSMSeed/csv/Mseed0.1_16.csv")
data01_17 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.1/CSMSeed/csv/Mseed0.1_17.csv")
data01_18 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.1/CSMSeed/csv/Mseed0.1_18.csv")
data01_19 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.1/CSMSeed/csv/Mseed0.1_19.csv")
data01_20 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.1/CSMSeed/csv/Mseed0.1_20.csv")

 

# Getting the return values in to variables.
CommonSyncmerNumber1a , numberSMunmut1a, CommonSyncmer1a = common(data, data01_1)
CommonSyncmerNumber2a , numberSMunmut2a, CommonSyncmer2a = common(data, data01_2)
CommonSyncmerNumber3a , numberSMunmut3a, CommonSyncmer3a = common(data, data01_3)
CommonSyncmerNumber4a , numberSMunmut4a, CommonSyncmer4a = common(data, data01_4)
CommonSyncmerNumber5a , numberSMunmut5a, CommonSyncmer5a = common(data, data01_5)
CommonSyncmerNumber6a , numberSMunmut6a, CommonSyncmer6a = common(data, data01_6)
CommonSyncmerNumber7a , numberSMunmut7a, CommonSyncmer7a = common(data, data01_7)
CommonSyncmerNumber8a , numberSMunmut8a, CommonSyncmer8a = common(data, data01_8)
CommonSyncmerNumber9a , numberSMunmut9a, CommonSyncmer9a = common(data, data01_9)
CommonSyncmerNumber10a , numberSMunmut10a, CommonSyncmer10a = common(data, data01_10)
CommonSyncmerNumber11a , numberSMunmut11a, CommonSyncmer11a = common(data, data01_11)
CommonSyncmerNumber12a , numberSMunmut12a, CommonSyncmer12a = common(data, data01_12)
CommonSyncmerNumber13a , numberSMunmut13a, CommonSyncmer13a = common(data, data01_13)
CommonSyncmerNumber14a , numberSMunmut14a, CommonSyncmer14a = common(data, data01_14)
CommonSyncmerNumber15a , numberSMunmut15a, CommonSyncmer15a = common(data, data01_15)
CommonSyncmerNumber16a , numberSMunmut16a, CommonSyncmer16a = common(data, data01_16)
CommonSyncmerNumber17a , numberSMunmut17a, CommonSyncmer17a = common(data, data01_17)
CommonSyncmerNumber18a , numberSMunmut18a, CommonSyncmer18a = common(data, data01_18)
CommonSyncmerNumber19a , numberSMunmut19a, CommonSyncmer19a = common(data, data01_19)
CommonSyncmerNumber20a , numberSMunmut20a, CommonSyncmer20a = common(data, data01_20)


# Sequence divergence estimation
kmers = 20
thetabar1a = 1 - (CommonSyncmerNumber1a/numberSMunmut1a)**(1/kmers)
thetabar2a = 1 - (CommonSyncmerNumber2a/numberSMunmut2a)**(1/kmers)
thetabar3a = 1 - (CommonSyncmerNumber3a/numberSMunmut3a)**(1/kmers)
thetabar4a = 1 - (CommonSyncmerNumber4a/numberSMunmut4a)**(1/kmers)
thetabar5a = 1 - (CommonSyncmerNumber5a/numberSMunmut5a)**(1/kmers)
thetabar6a = 1 - (CommonSyncmerNumber6a/numberSMunmut6a)**(1/kmers)
thetabar7a = 1 - (CommonSyncmerNumber7a/numberSMunmut7a)**(1/kmers)
thetabar8a = 1 - (CommonSyncmerNumber8a/numberSMunmut8a)**(1/kmers)
thetabar9a = 1 - (CommonSyncmerNumber9a/numberSMunmut9a)**(1/kmers)
thetabar10a = 1 - (CommonSyncmerNumber10a/numberSMunmut10a)**(1/kmers)
thetabar11a = 1 - (CommonSyncmerNumber11a/numberSMunmut11a)**(1/kmers)
thetabar12a = 1 - (CommonSyncmerNumber12a/numberSMunmut12a)**(1/kmers)
thetabar13a = 1 - (CommonSyncmerNumber13a/numberSMunmut13a)**(1/kmers)
thetabar14a = 1 - (CommonSyncmerNumber14a/numberSMunmut14a)**(1/kmers)
thetabar15a = 1 - (CommonSyncmerNumber15a/numberSMunmut15a)**(1/kmers)
thetabar16a = 1 - (CommonSyncmerNumber16a/numberSMunmut16a)**(1/kmers)
thetabar17a = 1 - (CommonSyncmerNumber17a/numberSMunmut17a)**(1/kmers)
thetabar18a = 1 - (CommonSyncmerNumber18a/numberSMunmut18a)**(1/kmers)
thetabar19a = 1 - (CommonSyncmerNumber19a/numberSMunmut19a)**(1/kmers)
thetabar20a = 1 - (CommonSyncmerNumber20a/numberSMunmut20)**(1/kmers)

thetabar0_1 = pd.DataFrame({'ThetaBar0_1': [thetabar1a, thetabar2a, thetabar3a, thetabar4a,
                                              thetabar5a, thetabar6a, thetabar7a, thetabar8a,
                                              thetabar9a, thetabar10a, thetabar11a, thetabar12a,
                                              thetabar13a, thetabar14a, thetabar15a, thetabar16a,
                                              thetabar17a, thetabar18a, thetabar19a, thetabar20a]})


thetabar0_1a = [thetabar1a, thetabar2a, thetabar3a, thetabar4a,
                thetabar5a, thetabar6a, thetabar7a, thetabar8a,
                thetabar9a, thetabar10a, thetabar11a, thetabar12a,
                thetabar13a, thetabar14a, thetabar15a, thetabar16a,
                thetabar17a, thetabar18a, thetabar19a, thetabar20a] 


###############################################################################
# Now working with syncmer where p=0.2



data02_1 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.2/CSMSeed/csv/Mseed0.2_1.csv")
data02_2 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.2/CSMSeed/csv/Mseed0.2_2.csv")
data02_3 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.2/CSMSeed/csv/Mseed0.2_3.csv")
data02_4 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.2/CSMSeed/csv/Mseed0.2_4.csv")
data02_5 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.2/CSMSeed/csv/Mseed0.2_5.csv")
data02_6 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.2/CSMSeed/csv/Mseed0.2_6.csv")
data02_7 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.2/CSMSeed/csv/Mseed0.2_7.csv")
data02_8 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.2/CSMSeed/csv/Mseed0.2_8.csv")
data02_9 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.2/CSMSeed/csv/Mseed0.2_9.csv")
data02_10 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.2/CSMSeed/csv/Mseed0.2_10.csv")
data02_11 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.2/CSMSeed/csv/Mseed0.2_11.csv")
data02_12 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.2/CSMSeed/csv/Mseed0.2_12.csv")
data02_13 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.2/CSMSeed/csv/Mseed0.2_13.csv")
data02_14 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.2/CSMSeed/csv/Mseed0.2_14.csv")
data02_15 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.2/CSMSeed/csv/Mseed0.2_15.csv")
data02_16 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.2/CSMSeed/csv/Mseed0.2_16.csv")
data02_17 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.2/CSMSeed/csv/Mseed0.2_17.csv")
data02_18 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.2/CSMSeed/csv/Mseed0.2_18.csv")
data02_19 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.2/CSMSeed/csv/Mseed0.2_19.csv")
data02_20 = pd.read_csv("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/SimulatedP0.2/CSMSeed/csv/Mseed0.2_20.csv")

 

# Getting the return values in to variables.
CommonSyncmerNumber1b , numberSMunmut1b, CommonSyncmer1b = common(data, data02_1)
CommonSyncmerNumber2b , numberSMunmut2b, CommonSyncmer2b = common(data, data02_2)
CommonSyncmerNumber3b , numberSMunmut3b, CommonSyncmer3b = common(data, data02_3)
CommonSyncmerNumber4b , numberSMunmut4b, CommonSyncmer4b = common(data, data02_4)
CommonSyncmerNumber5b , numberSMunmut5b, CommonSyncmer5b = common(data, data02_5)
CommonSyncmerNumber6b , numberSMunmut6b, CommonSyncmer6b = common(data, data02_6)
CommonSyncmerNumber7b , numberSMunmut7b, CommonSyncmer7b = common(data, data02_7)
CommonSyncmerNumber8b , numberSMunmut8b, CommonSyncmer8b = common(data, data02_8)
CommonSyncmerNumber9b , numberSMunmut9b, CommonSyncmer9b = common(data, data02_9)
CommonSyncmerNumber10b , numberSMunmut10b, CommonSyncmer10b = common(data, data02_10)
CommonSyncmerNumber11b , numberSMunmut11b, CommonSyncmer11b = common(data, data02_11)
CommonSyncmerNumber12b , numberSMunmut12b, CommonSyncmer12b = common(data, data02_12)
CommonSyncmerNumber13b , numberSMunmut13b, CommonSyncmer13b = common(data, data02_13)
CommonSyncmerNumber14b , numberSMunmut14b, CommonSyncmer14b = common(data, data02_14)
CommonSyncmerNumber15b , numberSMunmut15b, CommonSyncmer15b = common(data, data02_15)
CommonSyncmerNumber16b , numberSMunmut16b, CommonSyncmer16b = common(data, data02_16)
CommonSyncmerNumber17b , numberSMunmut17b, CommonSyncmer17b = common(data, data02_17)
CommonSyncmerNumber18b , numberSMunmut18b, CommonSyncmer18b = common(data, data02_18)
CommonSyncmerNumber19b , numberSMunmut19b, CommonSyncmer19b = common(data, data02_19)
CommonSyncmerNumber20b , numberSMunmut20b, CommonSyncmer20b = common(data, data02_20)


# Sequence divergence estimation
kmers = 20
thetabar1b = 1 - (CommonSyncmerNumber1b/numberSMunmut1b)**(1/kmers)
thetabar2b = 1 - (CommonSyncmerNumber2b/numberSMunmut2b)**(1/kmers)
thetabar3b = 1 - (CommonSyncmerNumber3b/numberSMunmut3b)**(1/kmers)
thetabar4b = 1 - (CommonSyncmerNumber4b/numberSMunmut4b)**(1/kmers)
thetabar5b = 1 - (CommonSyncmerNumber5b/numberSMunmut5b)**(1/kmers)
thetabar6b = 1 - (CommonSyncmerNumber6b/numberSMunmut6b)**(1/kmers)
thetabar7b = 1 - (CommonSyncmerNumber7b/numberSMunmut7b)**(1/kmers)
thetabar8b = 1 - (CommonSyncmerNumber8b/numberSMunmut8b)**(1/kmers)
thetabar9b = 1 - (CommonSyncmerNumber9b/numberSMunmut9b)**(1/kmers)
thetabar10b = 1 - (CommonSyncmerNumber10b/numberSMunmut10b)**(1/kmers)
thetabar11b = 1 - (CommonSyncmerNumber11b/numberSMunmut11b)**(1/kmers)
thetabar12b = 1 - (CommonSyncmerNumber12b/numberSMunmut12b)**(1/kmers)
thetabar13b = 1 - (CommonSyncmerNumber13b/numberSMunmut13b)**(1/kmers)
thetabar14b = 1 - (CommonSyncmerNumber14b/numberSMunmut14b)**(1/kmers)
thetabar15b = 1 - (CommonSyncmerNumber15b/numberSMunmut15b)**(1/kmers)
thetabar16b = 1 - (CommonSyncmerNumber16b/numberSMunmut16b)**(1/kmers)
thetabar17b = 1 - (CommonSyncmerNumber17b/numberSMunmut17b)**(1/kmers)
thetabar18b = 1 - (CommonSyncmerNumber18b/numberSMunmut18b)**(1/kmers)
thetabar19b = 1 - (CommonSyncmerNumber19b/numberSMunmut19b)**(1/kmers)
thetabar20b = 1 - (CommonSyncmerNumber20b/numberSMunmut20b)**(1/kmers)


thetabar0_2 = pd.DataFrame({'ThetaBar0_2': [thetabar1b, thetabar2b, thetabar3b, thetabar4b,
                                              thetabar5b, thetabar6b, thetabar7b, thetabar8b,
                                              thetabar9b, thetabar10b, thetabar11b, thetabar12b,
                                              thetabar13b, thetabar14b, thetabar15b, thetabar16b,
                                              thetabar17b, thetabar18b, thetabar19b, thetabar20b]})



thetabar0_2b = [thetabar1b, thetabar2b, thetabar3b, thetabar4b,
                thetabar5b, thetabar6b, thetabar7b, thetabar8b,
                thetabar9b, thetabar10b, thetabar11b, thetabar12b,
                thetabar13b, thetabar14b, thetabar15b, thetabar16b,
                thetabar17b, thetabar18b, thetabar19b, thetabar20b]

import matplotlib.pyplot as plt
import numpy as np

# Creating dataset
np.random.seed(10)
data = np.random.normal(100, 20, 200)
data = [thetabar0_1, thetabar0_2]


fig = plt.figure(figsize =(10, 7))
 
# Creating plot
plt.boxplot(data)
 
# show plot
plt.show()



thetabar0_1.to_numpy()

data = [thetabar0_1a, thetabar0_2b]


data_1 = np.random.normal(100, 10, 10)
data_2 = np.random.normal(90, 20, 10)

data = [data_1 , data_2]




import csv

# open the file in the write mode
f = open('C:/Users/PIJHUSH/Desktop/sheared/Simulated300/resultsThetabar.csv', 'w')

# create the csv writer
writer = csv.writer(f)

# write a row to the csv file
writer.writerow(data)

# close the file
f.close()
