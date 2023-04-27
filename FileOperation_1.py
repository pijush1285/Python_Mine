# -*- coding: utf-8 -*-
"""
Created on Thu May 19 15:34:46 2022

@author: PIJHUSH
"""

x = []
with open("C:/Users/PIJHUSH/Desktop/sheared/Simulated300/RandomeSimulated/Results_RGID_1.txt") as file:
    for l in file:
        x.append(l.strip())
        
        
# Using readlines()
filename="C:/Users/PIJHUSH/Desktop/sheared/Simulated300/RandomeSimulated/Results_RGID_1.txt"
file1 = open(filename, 'r')
Lines = file1.readlines()
  
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
    



p = Lines[0]
Lines[1]
Lines[2]
 

p[0]
p[1]
p[2]


per_word = p.split()

per_word[0]
per_word[1]   # Use ful for checking
per_word[2]
per_word[3]
per_word[4]
per_word[5]
per_word[6]

q = Lines[1]
per_word = q.split()


per_word[0]
per_word[1]
per_word[2]
per_word[3]
per_word[4]
per_word[5]

s = Lines[2]
per_word = s.split()

per_word[0]    # Use ful for checking
per_word[1]
per_word[2]    # Use ful for checking
per_word[3]
per_word[4]

rows, cols = (5, 5)
arr = [[0]*cols]*rows
print(arr)


for row in arr:
    print(row)
    
    
    
# One dimentional array    
n = int(input()) 
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])
    
n = 4
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            a[i][j] = 0
        elif i > j:
            a[i][j] = 2
        else:
            a[i][j] = 1
for row in a:
    print(' '.join([str(elem) for elem in row]))
    

import numpy

a = numpy.zeros(shape=(5,10))
a


my_rows, my_cols = (3, 4)
my_array = [[0]*my_cols]*my_rows
print(my_array)



##################################################################
import pandas as pd
import numpy as np

column_names = ['a', 'b', 'c']
row_names    = ['1', '2', '3']
#row_names    = []

matrix = np.reshape((1, 2, 3, 4, 5, 6, 7, 8, 9), (3, 3))
df = pd.DataFrame(matrix, columns=column_names, index=row_names)
#df = pd.DataFrame(matrix, columns=column_names)
df

##################################################################
column_names = ['m','M', 'syn-window', 's-mer', 'seeds']
row_names    = []
matrix = np.zeros( (1, 2, 3, 4, 5, 6, 7, 8, 9,10), (2, 5))
df = pd.DataFrame(matrix, columns=column_names)
df

df[1][1] = 2
df[1][2] = 3
df[1][3] = 4
df[1][4] = 5
df[1][5] = 7


matrix = np.zeros(shape=(2, 5), dtype=int)
matrix[1, 1] = 2

df = pd.DataFrame(matrix, columns=column_names)
df
y = np.empty((4, 2))


# Closing files
file1.close()

###################################################################

import numpy as np
x = np.zeros((7, 5))
x
x[1,2] = 2
x
x[1,2] = '-5m'

import pandas as pd
import numpy as np
technologies= ({
         'Fee' :['22000.30','25000.40','23000.20','24000.50','26000.10'],
         'Discount':['1000.10',np.nan,'1000.5',np.nan,'2500.20']
             })
df = pd.DataFrame(technologies)

df.append({'Fee' :['22000.30'],'Discount':['1000.10'] })

print(df.dtypes)
###################################################################
import pandas as pd

df = pd.DataFrame({'Courses': ["Spark","PySpark","Python","pandas"],
                    'Fee' : [20000,25000,22000,24000]})

df1 = pd.DataFrame({'Courses': ["Pandas","Hadoop","Hyperion","Java"],
                    'Fee': [25000,25200,24500,24900],
                    'Duration': ['30days','35days','40days','45days']})

# Using append() method
df2 = df.append(df1)
print(df2)

df2 = df.append(df1, ignore_index=True)
print(df2)
