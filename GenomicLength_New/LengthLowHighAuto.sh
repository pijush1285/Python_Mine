#!/bin/bash

nlp=/home/dasp5/packages/noverlap/bin


for L in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100
    do

    dataL=/home/dasp5/datasets/Length/1.st_100_simulated/RGID_"$L".fasta
    echo $dataL
    Out=/home/dasp5/datasets/Length/1.st_100_simulated/LengthAuto_1/Results_RGID_"$L".txt
    echo $Out

    python3 $nlp/dna-seed-sim -m5 -M5 --syn-window=4 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m5 -M5 --syn-window=3 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m5 -M5 --syn-window=2 -s4 $dataL >> $Out

    python3 $nlp/dna-seed-sim -m6 -M6 --syn-window=5 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m6 -M6 --syn-window=4 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m6 -M6 --syn-window=3 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m6 -M6 --syn-window=2 -s5 $dataL >> $Out

    python3 $nlp/dna-seed-sim -m7 -M7 --syn-window=6 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m7 -M7 --syn-window=5 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m7 -M7 --syn-window=4 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m7 -M7 --syn-window=3 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m7 -M7 --syn-window=2 -s6 $dataL >> $Out

    python3 $nlp/dna-seed-sim -m8 -M8 --syn-window=7 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m8 -M8 --syn-window=6 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m8 -M8 --syn-window=5 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m8 -M8 --syn-window=4 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m8 -M8 --syn-window=3 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m8 -M8 --syn-window=2 -s7 $dataL >> $Out

    python3 $nlp/dna-seed-sim -m9 -M9 --syn-window=8 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m9 -M9 --syn-window=7 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m9 -M9 --syn-window=6 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m9 -M9 --syn-window=5 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m9 -M9 --syn-window=4 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m9 -M9 --syn-window=3 -s7 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m9 -M9 --syn-window=2 -s8 $dataL >> $Out
 
    python3 $nlp/dna-seed-sim -m10 -M10 --syn-window=9 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m10 -M10 --syn-window=8 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m10 -M10 --syn-window=7 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m10 -M10 --syn-window=6 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m10 -M10 --syn-window=5 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m10 -M10 --syn-window=4 -s7 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m10 -M10 --syn-window=3 -s8 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m10 -M10 --syn-window=2 -s9 $dataL >> $Out

    python3 $nlp/dna-seed-sim -m11 -M11 --syn-window=10 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m11 -M11 --syn-window=9 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m11 -M11 --syn-window=8 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m11 -M11 --syn-window=7 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m11 -M11 --syn-window=6 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m11 -M11 --syn-window=5 -s7 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m11 -M11 --syn-window=4 -s8 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m11 -M11 --syn-window=3 -s9 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m11 -M11 --syn-window=2 -s10 $dataL >> $Out

    python3 $nlp/dna-seed-sim -m12 -M12 --syn-window=11 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m12 -M12 --syn-window=10 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m12 -M12 --syn-window=9 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m12 -M12 --syn-window=8 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m12 -M12 --syn-window=7 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m12 -M12 --syn-window=6 -s7 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m12 -M12 --syn-window=5 -s8 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m12 -M12 --syn-window=4 -s9 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m12 -M12 --syn-window=3 -s10 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m12 -M12 --syn-window=2 -s11 $dataL >> $Out

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

    python3 $nlp/dna-seed-sim -m14 -M14 --syn-window=13 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m14 -M14 --syn-window=12 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m14 -M14 --syn-window=11 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m14 -M14 --syn-window=10 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m14 -M14 --syn-window=9 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m14 -M14 --syn-window=8 -s7 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m14 -M14 --syn-window=7 -s8 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m14 -M14 --syn-window=6 -s9 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m14 -M14 --syn-window=5 -s10 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m14 -M14 --syn-window=4 -s11 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m14 -M14 --syn-window=3 -s12 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m14 -M14 --syn-window=2 -s13 $dataL >> $Out

 
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


    python3 $nlp/dna-seed-sim -m16 -M16 --syn-window=15 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m16 -M16 --syn-window=14 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m16 -M16 --syn-window=13 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m16 -M16 --syn-window=12 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m16 -M16 --syn-window=11 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m16 -M16 --syn-window=10 -s7 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m16 -M16 --syn-window=9 -s8 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m16 -M16 --syn-window=8 -s9 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m16 -M16 --syn-window=7 -s10 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m16 -M16 --syn-window=6 -s11 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m16 -M16 --syn-window=5 -s12 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m16 -M16 --syn-window=4 -s13 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m16 -M16 --syn-window=3 -s14 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m16 -M16 --syn-window=2 -s15 $dataL >> $Out

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

    python3 $nlp/dna-seed-sim -m18 -M18 --syn-window=17 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m18 -M18 --syn-window=16 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m18 -M18 --syn-window=15 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m18 -M18 --syn-window=14 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m18 -M18 --syn-window=13 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m18 -M18 --syn-window=12 -s7 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m18 -M18 --syn-window=11 -s8 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m18 -M18 --syn-window=10 -s9 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m18 -M18 --syn-window=9 -s10 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m18 -M18 --syn-window=8 -s11 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m18 -M18 --syn-window=7 -s12 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m18 -M18 --syn-window=6 -s13 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m18 -M18 --syn-window=5 -s14 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m18 -M18 --syn-window=4 -s15 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m18 -M18 --syn-window=3 -s16 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m18 -M18 --syn-window=2 -s17 $dataL >> $Out

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

    python3 $nlp/dna-seed-sim -m22 -M22 --syn-window=21 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m22 -M22 --syn-window=20 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m22 -M22 --syn-window=19 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m22 -M22 --syn-window=18 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m22 -M22 --syn-window=17 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m22 -M22 --syn-window=16 -s7 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m22 -M22 --syn-window=15 -s8 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m22 -M22 --syn-window=14 -s9 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m22 -M22 --syn-window=13 -s10 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m22 -M22 --syn-window=12 -s11 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m22 -M22 --syn-window=11 -s12 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m22 -M22 --syn-window=10 -s13 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m22 -M22 --syn-window=9 -s14 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m22 -M22 --syn-window=8 -s15 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m22 -M22 --syn-window=7 -s16 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m22 -M22 --syn-window=6 -s17 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m22 -M22 --syn-window=5 -s18 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m22 -M22 --syn-window=4 -s19 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m22 -M22 --syn-window=3 -s20 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m22 -M22 --syn-window=2 -s21 $dataL >> $Out

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

    python3 $nlp/dna-seed-sim -m24 -M24 --syn-window=23 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m24 -M24 --syn-window=22 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m24 -M24 --syn-window=21 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m24 -M24 --syn-window=20 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m24 -M24 --syn-window=19 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m24 -M24 --syn-window=18 -s7 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m24 -M24 --syn-window=17 -s8 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m24 -M24 --syn-window=16 -s9 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m24 -M24 --syn-window=15 -s10 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m24 -M24 --syn-window=14 -s11 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m24 -M24 --syn-window=13 -s12 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m24 -M24 --syn-window=12 -s13 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m24 -M24 --syn-window=11 -s14 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m24 -M24 --syn-window=10 -s15 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m24 -M24 --syn-window=9 -s16 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m24 -M24 --syn-window=8 -s17 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m24 -M24 --syn-window=7 -s18 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m24 -M24 --syn-window=6 -s19 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m24 -M24 --syn-window=5 -s20 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m24 -M24 --syn-window=4 -s21 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m24 -M24 --syn-window=3 -s22 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m24 -M24 --syn-window=2 -s23 $dataL >> $Out


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

    python3 $nlp/dna-seed-sim -m26 -M26 --syn-window=25 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m26 -M26 --syn-window=24 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m26 -M26 --syn-window=23 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m26 -M26 --syn-window=22 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m26 -M26 --syn-window=21 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m26 -M26 --syn-window=20 -s7 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m26 -M26 --syn-window=19 -s8 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m26 -M26 --syn-window=18 -s9 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m26 -M26 --syn-window=17 -s10 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m26 -M26 --syn-window=16 -s11 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m26 -M26 --syn-window=15 -s12 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m26 -M26 --syn-window=14 -s13 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m26 -M26 --syn-window=13 -s14 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m26 -M26 --syn-window=12 -s15 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m26 -M26 --syn-window=11 -s16 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m26 -M26 --syn-window=10 -s17 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m26 -M26 --syn-window=9 -s18 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m26 -M26 --syn-window=8 -s19 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m26 -M26 --syn-window=7 -s20 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m26 -M26 --syn-window=6 -s21 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m26 -M26 --syn-window=5 -s22 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m26 -M26 --syn-window=4 -s23 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m26 -M26 --syn-window=3 -s24 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m26 -M26 --syn-window=2 -s25 $dataL >> $Out

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
    
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=27 -s2 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=26 -s3 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=25 -s4 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=24 -s5 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=23 -s6 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=22 -s7 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=21 -s8 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=20 -s9 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=19 -s10 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=18 -s11 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=17 -s12 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=16 -s13 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=15 -s14 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=14 -s15 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=13 -s16 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=12 -s17 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=11 -s18 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=10 -s19 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=9 -s20 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=8 -s21 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=7 -s22 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=6 -s23 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=5 -s24 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=4 -s25 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=3 -s26 $dataL >> $Out
    python3 $nlp/dna-seed-sim -m28 -M28 --syn-window=2 -s27 $dataL >> $Out

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

