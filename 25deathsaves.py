import random

save = 0
fail = 0

def d20():
    return random.randint(1,20)

while(save < 3 and fail < 3):
    roll = d20()

    if (roll >= 10):
        if (roll == 20):
            save = 3
            print("Nat 20!")
        save += 1
    else:
        if (roll == 1):
            fail = 2
            print("Nat 1!")
        fail += 1

if (save == 3):
    print('Stabilized')
elif (save == 4):
    print('Revived')
else:
    print('Died')