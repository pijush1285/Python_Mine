# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 04:55:25 2021

@author: PIJHUSH

http://claresloggett.github.io/python_workshops/improved_kmers.html
"""

def count_kmers(read, k):
    """Count kmer occurrences in a given read.

    Parameters
    ----------
    read : string
        A single DNA sequence.
    k : int
        The value of k for which to count kmers.

    Returns
    -------
    counts : dictionary, {'string': int}
        A dictionary of counts keyed by their individual kmers (strings
        of length k).

    Examples
    --------
    >>> count_kmers("GATGAT", 3)
    {'ATG': 1, 'GAT': 2, 'TGA': 1}
    """
    # Start with an empty dictionary
    counts = {}
    # Calculate how many kmers of length k there are
    num_kmers = len(read) - k + 1
    # Loop over the kmer start positions
    for i in range(num_kmers):
        # Slice the string to get the kmer
        kmer = read[i:i+k]
        # Add the kmer to the dictionary if it's not there
        if kmer not in counts:
            counts[kmer] = 0
        # Increment the count for this kmer
        counts[kmer] += 1
    # Return the final counts
    return counts



count_kmers("GATGAT",3)
count_kmers("GATGAT",2)
count_kmers("GATGAT",5)
#There is an exercise to solve the following task bellow.
count_kmers(["GATGAT", "GATGAT", "CCGAT"],3)


###############################################################
# Reading and writing files
###############################################################


#Linux command can be used from here.
%ls
%cd Desktop
%ls
%cd John
%ls
notefile = open("TestFile.txt", "w")
notefile.write("Hello world!\nThis is a new line.\n")
notefile.close()




# Open the file for reading
# Use b for "binary" mode, which is sometimes necessary on Windows
fastq_filehandle = open("example_reads.fastq", "rb")

# Loop over each line in the file
for row in fastq_filehandle:
    # Use the built-in .strip() method to remove whitespace and newlines from the line
    row = row.strip()
    # Print it out
    print(row)

# Close the file
fastq_filehandle.close()
