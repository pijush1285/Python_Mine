#!/bin/bash

# Package Location
pkj=/home/dasp5/packages/noverlap/bin


kmer=10
smer=3
vt=5
int_vt=$((vt))
window=$((kmer - smer  + 1))
#echo $window

# Define the parent directory name
parent_dir="seedsk"$kmer"s"$smer""
mkdir $parent_dir

# Create the parent directory and any intermediate directories if necessary
mkdir $parent_dir/1_Raw_seed
mkdir $parent_dir/2_Mutated_0.05_seed
mkdir $parent_dir/3_Mutated_0.15_seed
mkdir $parent_dir/4_Mutated_0.25_seed

# Get the current location of the directory
current_dir=$(pwd)
echo "The current directory is: $current_dir"


comInputAdd=$current_dir
comOutputAdd=$current_dir/seedsk"$kmer"s"$smer"


for ((i=1;i<=1000;i++));
do
   input1=$comInputAdd/Raw_Fasta/RGID_"$i".fasta
   output1=$comOutputAdd/1_Raw_seed/RawSeed_"$i".csv
   python $pkj/dna-seed-sim -m"$kmer" -M"$kmer" --syn-window=$window -s"$smer" --syn-offset=$vt --seeds $input1 > $output1

   input2=$comInputAdd/Mutated_0.05/Mutated/Mutated_"$i".fasta
   output2=$comOutputAdd/2_Mutated_0.05_seed/Mut_0.05Seed_"$i".csv
   python $pkj/dna-seed-sim -m"$kmer" -M"$kmer" --syn-window=$window -s"$smer" --syn-offset=$vt --seeds $input2 > $output2

   input3=$comInputAdd/Mutated_0.15/Mutated/Mutated_"$i".fasta
   output3=$comOutputAdd/3_Mutated_0.15_seed/Mut_0.15Seed_"$i".csv
   python $pkj/dna-seed-sim -m"$kmer" -M"$kmer" --syn-window=$window -s"$smer" --syn-offset=$vt --seeds $input3 > $output3


   input4=$comInputAdd/Mutated_0.25/Mutated/Mutated_"$i".fasta
   output4=$comOutputAdd/4_Mutated_0.25_seed/Mut_0.25Seed_"$i".csv
   python $pkj/dna-seed-sim -m"$kmer" -M"$kmer" --syn-window=$window -s"$smer" --syn-offset=$vt  --seeds $input4 > $output4


   echo "###########Compleated#############"
   echo $i
done
