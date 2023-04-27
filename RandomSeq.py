
# For run the code 
# $ python RandomSeq.py -h
# $ python RandomSeq.py -n 10 -l 2000000


from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from random import choice
import random
from argparse import ArgumentParser, RawTextHelpFormatter


def main(): 
    parser = getArguments()
    argument = parser.parse_args()
    check( argument ) 
    number_of_sequence = argument.seq_number
    sequence_length = argument.seq_length
    RandomSequenceGenerator(number_of_sequence, sequence_length)
    
    
def getsequences(length):
    bases=["A","G","C","T"]
    sequence=""
    for count in range(length):
        sequence+=choice(bases)
    return sequence

# Now the function is define below. We need to pass the number of file and the 
# Length of the genome sequence.
def RandomSequenceGenerator(number, length):
    random.seed(31415)
    count = 1
    for x in range(number):
            len1 = length
            sequence = getsequences(len1)  
            name = "RGID_"+str(count)
            new_id = str(name)
            new_rec = SeqRecord(Seq(sequence),id=new_id, description="Random_SeqLength_0:"+str(length)+".")
            FastaFileName = str(name)+".fasta"
            SeqIO.write(new_rec, FastaFileName,"fasta")
            print("Fasta file generate completed number:", count)
            count = count + 1
            

# Check and fixes arguments if possible.    
def check( argument ):
    if argument.seq_number <= 0:
        raise Exception( f'Error: seq_number = {argument.seq_number} <= 0.' )
    if argument.seq_length <= 0:
        raise Exception( f'Error: seq_length = {argument.seq_length} <= 0.' )
        
        
        
def getArguments():
    parser = ArgumentParser(description='The fasta files will be generated at random using this script.\n',
                            formatter_class=RawTextHelpFormatter)
    parser.add_argument("-n", "--seq_number", dest="seq_number", type=int, required=True, 
                        help="SEQ_NUMBER is the number of sequence you want to produce.", metavar="SEQ_NUMBER")
    parser.add_argument("-l", "--seq_length", dest="seq_length", type=int, required=True,
                        help="SEQ_LENGTH is the length of the sequence you want to produce.", metavar="SEQ_LENGTH") 
    return parser      
        
        
if __name__ == "__main__":
    main()
