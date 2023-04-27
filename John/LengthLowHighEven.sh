#!/bin/bash

nlp=/home/dasp5/packages/noverlap/bin


for L in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100
    do

    dataL=/home/dasp5/dataset/Length/1.st_100_simulated/RGID_"$L".fasta
    echo $dataL
    Out=/home/dasp5/dataset/Length/1.st_100_simulated/LengthAuto_1/LengthEven_1/Results_RGID_"$L".txt
    echo $Out

    python3 $nlp/dna-seed-sim -m7 -M7 --syn-window=6 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m7 -M7 --syn-window=5 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m7 -M7 --syn-window=4 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m7 -M7 --syn-window=3 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m7 -M7 --syn-window=2 -s6 $dataL >> $Out

    python3 $nlp/dna-seed-sim -m9 -M9 --syn-window=8 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m9 -M9 --syn-window=7 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m9 -M9 --syn-window=6 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m9 -M9 --syn-window=5 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m9 -M9 --syn-window=4 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m9 -M9 --syn-window=3 -s7 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m9 -M9 --syn-window=2 -s8 $dataL >> $Out

    python3 $nlp/dna-seed-sim -m11 -M11 --syn-window=10 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m11 -M11 --syn-window=9 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m11 -M11 --syn-window=8 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m11 -M11 --syn-window=7 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m11 -M11 --syn-window=6 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m11 -M11 --syn-window=5 -s7 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m11 -M11 --syn-window=4 -s8 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m11 -M11 --syn-window=3 -s9 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m11 -M11 --syn-window=2 -s10 $dataL >> $Out

    python3 $nlp/dna-seed-sim -m13 -M13 --syn-window=12 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m13 -M13 --syn-window=11 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m13 -M13 --syn-window=10 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m13 -M13 --syn-window=9 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m13 -M13 --syn-window=8 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m13 -M13 --syn-window=7 -s7 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m13 -M13 --syn-window=6 -s8 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m13 -M13 --syn-window=5 -s9 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m13 -M13 --syn-window=4 -s10 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m13 -M13 --syn-window=3 -s11 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m13 -M13 --syn-window=2 -s12 $dataL >> $Out

    python3 $nlp/dna-seed-sim -m17 -M17 --syn-window=16 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m17 -M17 --syn-window=15 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m17 -M17 --syn-window=14 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m17 -M17 --syn-window=13 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m17 -M17 --syn-window=12 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m17 -M17 --syn-window=11 -s7 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m17 -M17 --syn-window=10 -s8 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m17 -M17 --syn-window=9 -s9 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m17 -M17 --syn-window=8 -s10 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m17 -M17 --syn-window=7 -s11 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m17 -M17 --syn-window=6 -s12 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m17 -M17 --syn-window=5 -s13 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m17 -M17 --syn-window=4 -s14 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m17 -M17 --syn-window=3 -s15 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m17 -M17 --syn-window=2 -s16 $dataL >> $Out

    python3 $nlp/dna-seed-sim -m19 -M19 --syn-window=18 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m19 -M19 --syn-window=17 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m19 -M19 --syn-window=16 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m19 -M19 --syn-window=15 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m19 -M19 --syn-window=14 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m19 -M19 --syn-window=13 -s7 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m19 -M19 --syn-window=12 -s8 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m19 -M19 --syn-window=11 -s9 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m19 -M19 --syn-window=10 -s10 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m19 -M19 --syn-window=9 -s11 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m19 -M19 --syn-window=8 -s12 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m19 -M19 --syn-window=7 -s13 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m19 -M19 --syn-window=6 -s14 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m19 -M19 --syn-window=5 -s15 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m19 -M19 --syn-window=4 -s16 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m19 -M19 --syn-window=3 -s17 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m19 -M19 --syn-window=2 -s18 $dataL >> $Out

    python3 $nlp/dna-seed-sim -m21 -M21 --syn-window=20 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m21 -M21 --syn-window=19 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m21 -M21 --syn-window=18 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m21 -M21 --syn-window=17 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m21 -M21 --syn-window=16 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m21 -M21 --syn-window=15 -s7 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m21 -M21 --syn-window=14 -s8 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m21 -M21 --syn-window=13 -s9 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m21 -M21 --syn-window=12 -s10 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m21 -M21 --syn-window=11 -s11 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m21 -M21 --syn-window=10 -s12 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m21 -M21 --syn-window=9 -s13 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m21 -M21 --syn-window=8 -s14 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m21 -M21 --syn-window=7 -s15 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m21 -M21 --syn-window=6 -s16 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m21 -M21 --syn-window=5 -s17 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m21 -M21 --syn-window=4 -s18 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m21 -M21 --syn-window=3 -s19 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m21 -M21 --syn-window=2 -s20 $dataL >> $Out

    python3 $nlp/dna-seed-sim -m23 -M23 --syn-window=22 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m23 -M23 --syn-window=21 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m23 -M23 --syn-window=20 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m23 -M23 --syn-window=19 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m23 -M23 --syn-window=18 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m23 -M23 --syn-window=17 -s7 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m23 -M23 --syn-window=16 -s8 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m23 -M23 --syn-window=15 -s9 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m23 -M23 --syn-window=14 -s10 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m23 -M23 --syn-window=13 -s11 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m23 -M23 --syn-window=12 -s12 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m23 -M23 --syn-window=11 -s13 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m23 -M23 --syn-window=10 -s14 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m23 -M23 --syn-window=9 -s15 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m23 -M23 --syn-window=8 -s16 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m23 -M23 --syn-window=7 -s17 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m23 -M23 --syn-window=6 -s18 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m23 -M23 --syn-window=5 -s19 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m23 -M23 --syn-window=4 -s20 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m23 -M23 --syn-window=3 -s21 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m23 -M23 --syn-window=2 -s22 $dataL >> $Out

    python3 $nlp/dna-seed-sim -m27 -M27 --syn-window=26 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m27 -M27 --syn-window=25 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m27 -M27 --syn-window=24 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m27 -M27 --syn-window=23 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m27 -M27 --syn-window=22 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m27 -M27 --syn-window=21 -s7 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m27 -M27 --syn-window=20 -s8 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m27 -M27 --syn-window=19 -s9 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m27 -M27 --syn-window=18 -s10 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m27 -M27 --syn-window=17 -s11 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m27 -M27 --syn-window=16 -s12 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m27 -M27 --syn-window=15 -s13 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m27 -M27 --syn-window=14 -s14 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m27 -M27 --syn-window=13 -s15 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m27 -M27 --syn-window=12 -s16 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m27 -M27 --syn-window=11 -s17 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m27 -M27 --syn-window=10 -s18 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m27 -M27 --syn-window=9 -s19 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m27 -M27 --syn-window=8 -s20 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m27 -M27 --syn-window=7 -s21 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m27 -M27 --syn-window=6 -s22 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m27 -M27 --syn-window=5 -s23 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m27 -M27 --syn-window=4 -s24 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m27 -M27 --syn-window=3 -s25 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m27 -M27 --syn-window=2 -s26 $dataL >> $Out
    
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=28 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=27 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=26 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=25 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=24 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=23 -s7 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=22 -s8 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=21 -s9 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=20 -s10 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=19 -s11 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=18 -s12 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=17 -s13 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=16 -s14 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=15 -s15 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=14 -s16 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=13 -s17 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=12 -s18 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=11 -s19 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=10 -s20 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=9 -s21 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=8 -s22 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=7 -s23 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=6 -s24 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=5 -s25 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=4 -s26 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=3 -s27 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m29 -M29 --syn-window=2 -s28 $dataL >> $Out

    echo "###########################"
    echo "Analysis completrd:"
    echo RGIDa_"$L".fasta
    echo "###########################"

done 


