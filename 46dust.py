import sys
import math
import mcb185 # type: ignore

window = int(sys.argv[2])
max_entropy = float(sys.argv[3])
fasta = []
wrap = 60

def entropy(seq):
    a = seq.count('A') / len(seq)
    c = seq.count('C') / len(seq)
    g = seq.count('G') / len(seq)
    t = seq.count('T') / len(seq)
    probs = [a,c,g,t]
    h = 0
    for n in probs:
        if n != 0: 
            h += n*math.log2(n)
    return -h

for defline, seq in mcb185.read_fasta(sys.argv[1]):
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
        