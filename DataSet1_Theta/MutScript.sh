
#!/bin/bash 

#Package Location

pkj=/home/dasp5/packages/mutation-rate-intervals

for ((i=1;i<=1000;i++));
do
   ionput=/home/dasp5/dataset/Table3/1_Dataset_0.1kby1k/Raw_Fasta/RGID_"$i".fasta
   outputM=/home/dasp5/dataset/Table3/1_Dataset_0.1kby1k/Mutated_0.05/Mutated/Mutated_"$i".fasta
   outputS=/home/dasp5/dataset/Table3/1_Dataset_0.1kby1k/Mutated_0.05/Status/MutStats_"$i".fasta
   cat $ionput | python $pkj/simulate_nucleotide_errors.py K=20 P=0.05 --stats=$outputS --mutated=$outputM
   
   
   outputM1=/home/dasp5/dataset/Table3/1_Dataset_0.1kby1k/Mutated_0.15/Mutated/Mutated_"$i".fasta
   outputS1=/home/dasp5/dataset/Table3/1_Dataset_0.1kby1k/Mutated_0.15/Status/MutStats_"$i".fasta
   cat $ionput | python $pkj/simulate_nucleotide_errors.py K=20 P=0.15 --stats=$outputS1 --mutated=$outputM1
   
   outputM2=/home/dasp5/dataset/Table3/1_Dataset_0.1kby1k/Mutated_0.25/Mutated/Mutated_"$i".fasta
   outputS2=/home/dasp5/dataset/Table3/1_Dataset_0.1kby1k/Mutated_0.25/Status/MutStats_"$i".fasta
   cat $ionput | python $pkj/simulate_nucleotide_errors.py K=20 P=0.25 --stats=$outputS2 --mutated=$outputM2
   
   
   echo $i
   echo "***********Completed*********"
done
