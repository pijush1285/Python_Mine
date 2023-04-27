#!/bin/bash 

#Package Location

pkj=/home/dasp5/packages/mutation-rate-intervals

for ((i=1;i<=1000;i++));
do
   ionput=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k/Rawfasta_100kL/RGID_"$i".fasta
   outputM=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k/Mutated_0.001/Mutated/Mutated_"$i".fasta
   outputS=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k/Mutated_0.001/Status/MutStats_"$i".fasta
   cat $ionput | python $pkj/simulate_nucleotide_errors.py K=20 P=0.001 --stats=$outputS --mutated=$outputM
   
   
   outputM1=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k/Mutated_0.01/Mutated/Mutated_"$i".fasta
   outputS1=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k/Mutated_0.01/Status/MutStats_"$i".fasta
   cat $ionput | python $pkj/simulate_nucleotide_errors.py K=20 P=0.01 --stats=$outputS1 --mutated=$outputM1
   
   outputM2=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k/Mutated_0.1/Mutated/Mutated_"$i".fasta
   outputS2=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k/Mutated_0.1/Status/MutStats_"$i".fasta
   cat $ionput | python $pkj/simulate_nucleotide_errors.py K=20 P=0.1 --stats=$outputS2 --mutated=$outputM2
   
   outputM3=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k/Mutated_0.2/Mutated/Mutated_"$i".fasta
   outputS3=/home/dasp5/dataset/Table2Analysis/Dataset_100kby_1k/Mutated_0.2/Status/MutStats_"$i".fasta
   cat $ionput | python $pkj/simulate_nucleotide_errors.py K=20 P=0.2 --stats=$outputS3 --mutated=$outputM3
   
   echo $i
   echo "***********Completed*********"
done

