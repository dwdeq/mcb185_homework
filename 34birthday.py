import random
import sys

trials = int(sys.argv[1])
people = int(sys.argv[2])

results = []

for i in range(trials):
    calendar = []
    for i in range(365):
        calendar.append(0)
    result = False
    for j in range(people):
        day = random.randint(0,364)
        calendar[day] += 1
        if calendar[day] == 2:
            result = True
    results.append(result)


avg = 0
for result in results:
    if result == True:
        avg += 1
print(avg/len(results))

