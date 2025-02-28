import sys

data = []
for arg in sys.argv[1:]:
    f = float(arg)
    data.append(f)

def n50(n50list):
    n50list.sort()
    n50sum = 0
    for item in n50list:
        n50sum += item
    n50half = 0
    n50idx = -1
    while (n50half < n50sum / 2):
        n50idx += 1
        n50half += n50list[n50idx]
    return n50list[n50idx]

print(n50(data))