t = 1, 2  # this is a tuple
print(t)
print(type(t))

person = 'Steve', 21, 57891.50 # name, age, yearly income
print(person)

def midpoint(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y

print(midpoint(1, 2, 3, 4))     #1
m = midpoint(1, 2, 3, 4)        #2
mx, my = midpoint(1, 2, 3, 4)   #3
print(mx, my)                   #4

print(m)

print(m[0], m[1])

while True:
    print('hello')