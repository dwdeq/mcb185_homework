import gzip
import sys

with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if line[:2] == 'DE':
            continue
        if line[:2].isdigit():
            continue