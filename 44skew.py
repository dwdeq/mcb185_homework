import sequence

seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10
s = seq[0:w]
i = 0
while (len(seq) != w + i):
    cha = list(s)
    cha.append(seq[w+i])
    del cha[0]
    s = ''.join(cha)
    print(i, sequence.gc_comp(s), sequence.gc_skew(s))
    i += 1