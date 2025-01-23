import random

save = False
advantage = False
disadvantage = False
dc = 10

def d20():
    return random.randint(1,20)

roll = d20()
if (advantage):
    roll2 = d20()
    if (roll2 > roll):
        roll = roll2
elif (disadvantage):
    roll2 = d20()
    if (roll2 < roll):
        roll = roll2
if (roll >= dc):
    save = True

if (save):
    print('Successful Saving Throw')
else:
    print('Saving Throw Failed')