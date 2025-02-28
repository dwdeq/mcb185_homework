import sys
import gzip
import mcb185 # type: ignore

fastas_file = sys.argv[1]
window = int(sys.argv[2])
fastas = []

with gzip.open(fastas_file, 'rt') as fp:
    for line in fp:
        words = line.split()
        fastas.append(words[0])

n = 0
i = 0
while (i < len(fastas)):
    if fastas[i][0] == '>':
        n = i + 1
        i += 2
    else:
        temp = []
        temp.append(fastas[n])
        temp.append(fastas[i])
        fastas[n] = ''.join(temp)
        del fastas[i]

for fasta in fastas:
    frame = False
    j = 0
    if fasta[0] == '>': 
        print(fasta)
        continue

    i = 0
    while i < len(fasta) - 2:
        if not frame:
            if fasta[i:i+3] == 'ATG':
                frame = True
            else:
                i += 1
        if frame:
            codon = fasta[i:i+3]
            aa = mcb185.translate(codon)

            if (j < window):
                print(aa, end='')
                j += 1
            
            elif (j == window):
                print('...', end = '')
                j += 1

            if aa == '*':
                print()
                frame = False
                j = 0
            
            i += 3

    print()