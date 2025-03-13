import argparse
import math
import mcb185 # type: ignore

def entropy(seq):
    a = seq.count('A') / len(seq)
    c = seq.count('C') / len(seq)
    g = seq.count('G') / len(seq)
    t = seq.count('T') / len(seq)
    probs = [a,c,g,t]
    h = 0
    for n in probs:
        if n != 0: 
            h -= n*math.log2(n)
    return h

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('--size', type=int, default=20,
    help='window size [%(default)i]')
parser.add_argument('--entropy', type=float, default=1.4,
    help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)

window = arg.size
max_entropy = arg.entropy
fasta = []
wrap = 60

for defline, seq in mcb185.read_fasta(arg.file):
    print('>',defline, sep = '')
    for i in range(len(seq) - window + 1):
        if i > wrap:
            print('...',end = '')
            break
        subseq = seq[i:i+window]
        if entropy(subseq) < max_entropy:
            print('N', end='')
            i += window
        else:
            print(seq[i],end='')
    print('\n')
        