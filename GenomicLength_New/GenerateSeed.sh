#!/bin/bash

nlp=/home/dasp5/packages/noverlap/bin
fn=1

for L in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100
    do

    dataL=/home/dasp5/dataset/Length100/"$fn".st_100_simulated/RGID_"$L".fasta
    echo $dataL
    Out=/home/dasp5/dataset/OpenSyncmer/1.Length_100/"$fn".st_100_simulated/seed_"$fn"/Results_RGID_"$L".txt
    echo $Out

    python3 $nlp/dna-seed-sim -m5 -M5 --syn-window=4 -s2 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m5 -M5 --syn-window=3 -s3 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m5 -M5 --syn-window=2 -s4 --syn-offset=1 $dataL >> $Out

    python3 $nlp/dna-seed-sim -m10 -M10 --syn-window=9 -s2 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m10 -M10 --syn-window=8 -s3 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m10 -M10 --syn-window=7 -s4 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m10 -M10 --syn-window=6 -s5 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m10 -M10 --syn-window=5 -s6 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m10 -M10 --syn-window=4 -s7 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m10 -M10 --syn-window=3 -s8 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m10 -M10 --syn-window=2 -s9 --syn-offset=1 $dataL >> $Out

    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=14 -s2 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=13 -s3 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=12 -s4 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=11 -s5 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=10 -s6 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=9 -s7 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=8 -s8 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=7 -s9 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=6 -s10 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=5 -s11 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=4 -s12 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=3 -s13 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m15 -M15 --syn-window=2 -s14 --syn-offset=1 $dataL >> $Out

    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=19 -s2 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=18 -s3 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=17 -s4 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=16 -s5 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=15 -s6 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=14 -s7 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=13 -s8 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=12 -s9 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=11 -s10 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=10 -s11 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=9 -s12 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=8 -s13 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=7 -s14 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=6 -s15 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=5 -s16 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=4 -s17 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=3 -s18 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m20 -M20 --syn-window=2 -s19 --syn-offset=1 $dataL >> $Out

    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=24 -s2 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=23 -s3 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=22 -s4 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=21 -s5 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=20 -s6 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=19 -s7 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=18 -s8 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=17 -s9 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=16 -s10 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=15 -s11 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=14 -s12 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=13 -s13 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=12 -s14 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=11 -s15 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=10 -s16 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=9 -s17 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=8 -s18 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=7 -s19 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=6 -s20 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=5 -s21 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=4 -s22 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=3 -s23 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m25 -M25 --syn-window=2 -s24 --syn-offset=1 $dataL >> $Out

    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=29 -s2 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=28 -s3 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=27 -s4 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=26 -s5 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=25 -s6 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=24 -s7 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=23 -s8 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=22 -s9 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=21 -s10 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=20 -s11 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=19 -s12 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=18 -s13 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=17 -s14 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=16 -s15 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=15 -s16 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=14 -s17 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=13 -s18 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=12 -s19 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=11 -s20 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=10 -s21 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=9 -s22 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=8 -s23 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=7 -s24 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=6 -s25 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=5 -s26 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=4 -s27 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=3 -s28 --syn-offset=1 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m30 -M30 --syn-window=2 -s29 --syn-offset=1 $dataL >> $Out

    echo "###########################"
    echo "Analysis completrd:"
    echo RGIDa_"$L".fasta
    echo "###########################"

done 

