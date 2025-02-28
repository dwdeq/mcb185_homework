import sys
import mcb185
import re

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    if re.search('DKTGT',seq): print(defline)

