# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 02:08:26 2022

@author: PIJHUSH
"""


###############################################################################
#Seed 11

#!/bin/bash

# Package Location
pkj=/home/dasp5/packages/noverlap/bin

comInputAdd=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k
comOutputAdd=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k/seeds/seed_11

for ((i=1;i<=1000;i++)); 
do 
   input1=$comInputAdd/Rawfasta_100kL/RGID_"$i".fasta
   output1=$comOutputAdd/Raw_seed/RawSeed_"$i".csv
   python $pkj/dna-seed-sim -m11 -M11 --syn-window=9 -s3 --seeds $input1 > $output1
   
   input2=$comInputAdd/Mutated_0.001/Mutated/Mutated_"$i".fasta
   output2=$comOutputAdd/Mut_0.001_seed/Mut_0.001Seed_"$i".csv
   python $pkj/dna-seed-sim -m11 -M11 --syn-window=9 -s3 --seeds $input2 > $output2
   
   input3=$comInputAdd/Mutated_0.01/Mutated/Mutated_"$i".fasta
   output3=$comOutputAdd/Mut_0.01_seed/Mut_0.01Seed_"$i".csv
   python $pkj/dna-seed-sim -m11 -M11 --syn-window=9 -s3 --seeds $input3 > $output3
   
   
   input4=$comInputAdd/Mutated_0.1/Mutated/Mutated_"$i".fasta
   output4=$comOutputAdd/Mut_0.1_seed/Mut_0.1Seed_"$i".csv
   python $pkj/dna-seed-sim -m11 -M11 --syn-window=9 -s3 --seeds $input4 > $output4


   input5=$comInputAdd/Mutated_0.2/Mutated/Mutated_"$i".fasta
   output5=$comOutputAdd/Mut_0.2_seed/Mut_0.2Seed_"$i".csv
   python $pkj/dna-seed-sim -m11 -M11 --syn-window=9 -s3 --seeds $input5 > $output5
   
   
   echo "###########Compleated#############"
   echo $i
done

###############################################################################
#Seed 21

#!/bin/bash

# Package Location
pkj=/home/dasp5/packages/noverlap/bin

comInputAdd=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k
comOutputAdd=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k/seeds/seed_21

for ((i=1;i<=1000;i++)); 
do 
   input1=$comInputAdd/Rawfasta_100kL/RGID_"$i".fasta
   output1=$comOutputAdd/Raw_seed/RawSeed_"$i".csv
   python $pkj/dna-seed-sim -m21 -M21 --syn-window=16 -s6 --seeds $input1 > $output1
   
   input2=$comInputAdd/Mutated_0.001/Mutated/Mutated_"$i".fasta
   output2=$comOutputAdd/Mut_0.001_seed/Mut_0.001Seed_"$i".csv
   python $pkj/dna-seed-sim -m21 -M21 --syn-window=16 -s6 --seeds $input2 > $output2
   
   input3=$comInputAdd/Mutated_0.01/Mutated/Mutated_"$i".fasta
   output3=$comOutputAdd/Mut_0.01_seed/Mut_0.01Seed_"$i".csv
   python $pkj/dna-seed-sim -m21 -M21 --syn-window=16 -s6 --seeds $input3 > $output3
   
   
   input4=$comInputAdd/Mutated_0.1/Mutated/Mutated_"$i".fasta
   output4=$comOutputAdd/Mut_0.1_seed/Mut_0.1Seed_"$i".csv
   python $pkj/dna-seed-sim -m21 -M21 --syn-window=16 -s6 --seeds $input4 > $output4


   input5=$comInputAdd/Mutated_0.2/Mutated/Mutated_"$i".fasta
   output5=$comOutputAdd/Mut_0.2_seed/Mut_0.2Seed_"$i".csv
   python $pkj/dna-seed-sim -m21 -M21 --syn-window=16 -s6 --seeds $input5 > $output5
   
   
   echo "###########Compleated#############"
   echo $i
done

################################################################################
#Seed 31

#!/bin/bash

# Package Location
pkj=/home/dasp5/packages/noverlap/bin

comInputAdd=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k
comOutputAdd=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k/seeds/seed_31

for ((i=1;i<=1000;i++)); 
do 
   input1=$comInputAdd/Rawfasta_100kL/RGID_"$i".fasta
   output1=$comOutputAdd/Raw_seed/RawSeed_"$i".csv
   python $pkj/dna-seed-sim -m31 -M31 --syn-window=22 -s10 --seeds $input1 > $output1
   
   input2=$comInputAdd/Mutated_0.001/Mutated/Mutated_"$i".fasta
   output2=$comOutputAdd/Mut_0.001_seed/Mut_0.001Seed_"$i".csv
   python $pkj/dna-seed-sim -m31 -M31 --syn-window=22 -s10 --seeds $input2 > $output2
   
   input3=$comInputAdd/Mutated_0.01/Mutated/Mutated_"$i".fasta
   output3=$comOutputAdd/Mut_0.01_seed/Mut_0.01Seed_"$i".csv
   python $pkj/dna-seed-sim -m31 -M31 --syn-window=22 -s10 --seeds $input3 > $output3
   
   
   input4=$comInputAdd/Mutated_0.1/Mutated/Mutated_"$i".fasta
   output4=$comOutputAdd/Mut_0.1_seed/Mut_0.1Seed_"$i".csv
   python $pkj/dna-seed-sim -m31 -M31 --syn-window=22 -s10 --seeds $input4 > $output4


   input5=$comInputAdd/Mutated_0.2/Mutated/Mutated_"$i".fasta
   output5=$comOutputAdd/Mut_0.2_seed/Mut_0.2Seed_"$i".csv
   python $pkj/dna-seed-sim -m31 -M31 --syn-window=22 -s10 --seeds $input5 > $output5
   
   
   echo "###########Compleated#############"
   echo $i
done

################################################################################
#Seed 41


#!/bin/bash

# Package Location
pkj=/home/dasp5/packages/noverlap/bin

comInputAdd=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k
comOutputAdd=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k/seeds/seed_41

for ((i=1;i<=1000;i++)); 
do 
   input1=$comInputAdd/Rawfasta_100kL/RGID_"$i".fasta
   output1=$comOutputAdd/Raw_seed/RawSeed_"$i".csv
   python $pkj/dna-seed-sim -m41 -M41 --syn-window=30 -s12 --seeds $input1 > $output1
   
   input2=$comInputAdd/Mutated_0.001/Mutated/Mutated_"$i".fasta
   output2=$comOutputAdd/Mut_0.001_seed/Mut_0.001Seed_"$i".csv
   python $pkj/dna-seed-sim -m41 -M41 --syn-window=30 -s12 --seeds $input2 > $output2
   
   input3=$comInputAdd/Mutated_0.01/Mutated/Mutated_"$i".fasta
   output3=$comOutputAdd/Mut_0.01_seed/Mut_0.01Seed_"$i".csv
   python $pkj/dna-seed-sim -m41 -M41 --syn-window=30 -s12 --seeds $input3 > $output3
   
   
   input4=$comInputAdd/Mutated_0.1/Mutated/Mutated_"$i".fasta
   output4=$comOutputAdd/Mut_0.1_seed/Mut_0.1Seed_"$i".csv
   python $pkj/dna-seed-sim -m41 -M41 --syn-window=30 -s12 --seeds $input4 > $output4


   input5=$comInputAdd/Mutated_0.2/Mutated/Mutated_"$i".fasta
   output5=$comOutputAdd/Mut_0.2_seed/Mut_0.2Seed_"$i".csv
   python $pkj/dna-seed-sim -m41 -M41 --syn-window=30 -s12 --seeds $input5 > $output5
   
   
   echo "###########Compleated#############"
   echo $i
done
