#!/bin/bash


# Package Location
pkj=/home/dasp5/packages/noverlap/bin


kmer=10
smer=3
window=8



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

for ((i=1;i<=10;i++));
do
   input1=$comInputAdd/Raw_Fasta/RGID_"$i".fasta
   output1=$comOutputAdd/1_Raw_seed/RawSeed_"$i".csv
   python $pkj/dna-seed-sim -m"$kmer" -M"$kmer" --syn-window=$window -s"$smer" --syn-offset=5 --seeds $input1 > $output1

   input2=$comInputAdd/Mutated_0.05/Mutated/Mutated_"$i".fasta
   output2=$comOutputAdd/2_Mutated_0.05_seed/Mut_0.05Seed_"$i".csv
   python $pkj/dna-seed-sim -m"$kmer" -M"$kmer" --syn-window=$window -s"$smer" --syn-offset=5 --seeds $input2 > $output2

   input3=$comInputAdd/Mutated_0.15/Mutated/Mutated_"$i".fasta
   output3=$comOutputAdd/3_Mutated_0.15_seed/Mut_0.15Seed_"$i".csv
   python $pkj/dna-seed-sim -m"$kmer" -M"$kmer" --syn-window=$window -s"$smer" --syn-offset=5 --seeds $input3 > $output3


   input4=$comInputAdd/Mutated_0.25/Mutated/Mutated_"$i".fasta
   output4=$comOutputAdd/4_Mutated_0.25_seed/Mut_0.25Seed_"$i".csv
   python $pkj/dna-seed-sim -m"$kmer" -M"$kmer" --syn-window=$window -s"$smer" --syn-offset=5 --seeds $input4 > $output4


   echo "###########Compleated#############"
   echo $i
done


echo "############################################"
echo "Now the Theta calculation began"
echo "############################################"


# Define the parent directory name
parent_dir1="Thetak"$kmer"s"$smer""
mkdir $parent_dir1



# Define the file paths
file1=$current_dir/seedsk"$kmer"s"$smer"
file2=$current_dir/$parent_dir1

# Define the two variable values
var1=$kmer
var2=$smer


echo $file1
echo $file2
echo "##########################################"


# Run the Python script with the file paths, variable values, and output file name as arguments
python Theta.py $file1 $file2 $var1 $var2







