import sys
import gzip
import math

fastas = sys.argv[1]
window = int(sys.argv[2])
max_entropy = float(sys.argv[3])
fasta = []

wrap = 60

with gzip.open(fastas, 'rt') as fp:
    for line in fp:
        words = line.split()
        fasta.append(words[0])

n = 0                                       # initialize counting variable

def entropy(seq):
    nts = 'ACGT'
    counts = [0] * len(nts)
    entropies = [0] * len(nts)
    h = 0
    for nt in seq:
        idx = nts.find(nt)
        counts[idx] += 1
    for i in range(len(counts)):
        if counts[i] == 0: entropies[i] = 0
        else: entropies[i] = -(counts[i]/window * math.log(counts[i]/window))
    for hs in entropies:
        h += hs
    return h

move = False

for row in fasta:                           # start looking through each row
    if row[0] == '>':                       # for rows starting with '>'...
        print(row)                          # output the full row, and
        n = 0                               # reset the counting variable
        move = False
    elif move == True:
        continue
    else:                                   # otherwise...
        for i in range(len(row)):           # for each character in the row
            s = row[i:i+window]
            if (n < wrap):                # if n is less than the window
                if entropy(s) > max_entropy:
                    print('N', end = '')
                    n += 1
                else:
                    print(row[i], end = '')     # print the character
                    n += 1                      # add 1 to the counting variable
            if n % 20 == 0 and n != 0:
                if (n == wrap):
                    print('...\n')
                    move = True
                    break
                print()