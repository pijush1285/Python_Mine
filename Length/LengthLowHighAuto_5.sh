#!/bin/bash

nlp=/home/dasp5/packages/noverlap


for L in 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100
    do

    dataL=/home/dasp5/dataset/RandomSimulated/5.th_100_simulated/RGID_"$L".fasta
    echo $dataL
    Out=/home/dasp5/dataset/RandomSimulated/5.th_100_simulated/LengthAuto_5/Results_RGID_"$L".txt
    echo $Out

    python3 $nlp/dna-seed-sim -m5 -M5 --syn-window=4 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m5 -M5 --syn-window=3 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m5 -M5 --syn-window=2 -s4 $dataL >> $Out

    python3 $nlp/dna-seed-sim -m10 -M10 --syn-window=9 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m10 -M10 --syn-window=8 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m10 -M10 --syn-window=7 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m10 -M10 --syn-window=6 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m10 -M10 --syn-window=5 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m10 -M10 --syn-window=4 -s7 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m10 -M10 --syn-window=3 -s8 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m10 -M10 --syn-window=2 -s9 $dataL >> $Out

    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=14 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=13 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=12 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=11 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=10 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=9 -s7 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=8 -s8 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=7 -s9 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=6 -s10 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=5 -s11 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=4 -s12 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=3 -s13 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=2 -s14 $dataL >> $Out

    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=19 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=18 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=17 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=16 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=15 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=14 -s7 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=13 -s8 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=12 -s9 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=11 -s10 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=10 -s11 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=9 -s12 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=8 -s13 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=7 -s14 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=6 -s15 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=5 -s16 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=4 -s17 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=3 -s18 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=2 -s19 $dataL >> $Out

    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=24 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=23 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=22 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=21 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=20 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=19 -s7 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=18 -s8 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=17 -s9 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=16 -s10 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=15 -s11 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=14 -s12 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=13 -s13 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=12 -s14 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=11 -s15 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=10 -s16 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=9 -s17 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=8 -s18 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=7 -s19 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=6 -s20 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=5 -s21 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=4 -s22 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=3 -s23 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=2 -s24 $dataL >> $Out

    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=29 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=28 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=27 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=26 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=25 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=24 -s7 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=23 -s8 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=22 -s9 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=21 -s10 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=20 -s11 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=19 -s12 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=18 -s13 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=17 -s14 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=16 -s15 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=15 -s16 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=14 -s17 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=13 -s18 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=12 -s19 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=11 -s20 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=10 -s21 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=9 -s22 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=8 -s23 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=7 -s24 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=6 -s25 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=5 -s26 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=4 -s27 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=3 -s28 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=2 -s29 $dataL >> $Out

    echo "###########################"
    echo "Analysis completrd:"
    echo RGIDa_"$L".fasta
    echo "###########################"

done 

