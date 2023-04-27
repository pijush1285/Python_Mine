# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 02:47:00 2022

@author: dasp5
"""

# Copy a file into multiple folder
path1="/home/dasp5/dataset/Length100/1.st_100_simulated/"
path2="/home/dasp5/dataset/Length100/2.st_100_simulated/"
path3="/home/dasp5/dataset/Length100/3.st_100_simulated/"
path4="/home/dasp5/dataset/Length100/4.st_100_simulated/"
path5="/home/dasp5/dataset/Length100/5.st_100_simulated/"
path6="/home/dasp5/dataset/Length100/6.st_100_simulated/"
path7="/home/dasp5/dataset/Length100/7.st_100_simulated/"
path8="/home/dasp5/dataset/Length100/8.st_100_simulated/"
path9="/home/dasp5/dataset/Length100/9.st_100_simulated/"
path10="/home/dasp5/dataset/Length100/10.st_100_simulated/"
echo "/$path1/ /$path2/ /$path3/ /$path4/ /$path5/ /$path6/ /$path7/ /$path8/ /$path9/ /$path10/" | xargs -n 1 cp -v RandomSeq.py

#Generate the raw sequence
python RandomSeq.py -n 100 -l 100


# Copy a file into multiple folder
path1="/home/dasp5/dataset/Length100/1.st_100_simulated/"
path2="/home/dasp5/dataset/Length100/2.st_100_simulated/"
path3="/home/dasp5/dataset/Length100/3.st_100_simulated/"
path4="/home/dasp5/dataset/Length100/4.st_100_simulated/"
path5="/home/dasp5/dataset/Length100/5.st_100_simulated/"
path6="/home/dasp5/dataset/Length100/6.st_100_simulated/"
path7="/home/dasp5/dataset/Length100/7.st_100_simulated/"
path8="/home/dasp5/dataset/Length100/8.st_100_simulated/"
path9="/home/dasp5/dataset/Length100/9.st_100_simulated/"
path10="/home/dasp5/dataset/Length100/10.st_100_simulated/"
echo "/$path1/ /$path2/ /$path3/ /$path4/ /$path5/ /$path6/ /$path7/ /$path8/ /$path9/ /$path10/" | xargs -n 1 cp -v Seed.sh


# Capture folder number from strinng
pwd



# makes directory
path1="/home/dasp5/dataset/Length100/1.st_100_simulated/seed_1/Final/"
path2="/home/dasp5/dataset/Length100/2.st_100_simulated/seed_2/Final/"
path3="/home/dasp5/dataset/Length100/3.st_100_simulated/seed_3/Final/"
path4="/home/dasp5/dataset/Length100/4.st_100_simulated/seed_4/Final/"
path5="/home/dasp5/dataset/Length100/5.st_100_simulated/seed_5/Final/"
path6="/home/dasp5/dataset/Length100/6.st_100_simulated/seed_6/Final/"
path7="/home/dasp5/dataset/Length100/7.st_100_simulated/seed_7/Final/"
path8="/home/dasp5/dataset/Length100/8.st_100_simulated/seed_8/Final/"
path9="/home/dasp5/dataset/Length100/9.st_100_simulated/seed_9/Final/"
path10="/home/dasp5/dataset/Length100/10.st_100_simulated/seed_10/Final/"
echo "/$path1/ /$path2/ /$path3/ /$path4/ /$path5/ /$path6/ /$path7/ /$path8/ /$path9/ /$path10/" | xargs -n 1 cp -v Script.py

