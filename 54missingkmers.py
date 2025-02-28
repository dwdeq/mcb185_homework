import sys
import mcb185 # type: ignore
import itertools

k = 0
found = False
missing = []
while not found:
    k += 1
    kcount = {}
    for defline, seq in mcb185.read_fasta(sys.argv[1]):
        for i in range(len(seq) - k + 1):
            kmer = seq[i:i+k]
            if kmer not in kcount: kcount[kmer] = 0
            kcount[kmer] += 1
        rseq = mcb185.anti_seq(seq)
        for i in range(len(rseq) - k + 1):
            kmer = rseq[i:i+k]
            if kmer not in kcount: kcount[kmer] = 0
            kcount[kmer] += 1

    for nts in itertools.product('ACGT', repeat=k):
        kmer = ''.join(nts)
        if kmer not in kcount: 
            found = True
            missing.append(kmer)

    print('kmers of size',k,'found')

for kmer in missing:
    print(kmer)
    