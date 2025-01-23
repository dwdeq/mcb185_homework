def pythag(x,y):
    return (x**2 + y**2) ** 0.5

triples = ((0,0,0),)

for i in range(1,99):
    for j in range(i,99):
        if (pythag(i,j) % 1 == 0):
            triples += ((i,j,round(pythag(i,j))),)

for thing in triples:
    print(thing)