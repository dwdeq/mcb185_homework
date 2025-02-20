import sys
import math

data = []
for arg in sys.argv[1:]:
    f = float(arg)
    data.append(float(arg))

def minmax(list):
    min = math.inf
    max = -math.inf
    for item in list:
        if min > item:
            min = item
        if max < item:
            max = item
    return [min,max]

def mean(list):
    sum = 0
    for item in list:
        sum += item
    return sum / len(list)

def sd(list):
    mn = mean(list)
    weird = 0
    for item in list:
        weird += (item - mn)**2
    return (weird / len(list))**0.5

def median(list):
    i = round(len(list)/2)
    list.sort()
    return list[i]

def n50(list):
    list.sort()
    sum = 0
    for item in list:
        sum += item
    n50sum = 0
    n50idx = 0
    while (n50sum <= sum / 2):
        n50idx -= 1
        n50sum += list[n50idx]
    return list[n50idx]

stats = []

stats.append(len(data))
stats.append(minmax(data)[0])
stats.append(minmax(data)[1])
stats.append(mean(data))
stats.append(sd(data))
stats.append(median(data))
stats.append(n50(data))

print(stats)




