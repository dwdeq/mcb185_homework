import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

results = []

for i in range(trials):
    birthdays = []
    match = False
    for j in range(people):
        birthdays.append(random.randint(1,days))
        for k in range(len(birthdays)-1):
            if (birthdays[j] == birthdays[k]):
                match = True
    results.append(match)

avg = 0
for result in results:
    if result == True:
        avg += 1
print(avg/len(results))