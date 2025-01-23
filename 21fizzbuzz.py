for i in range(1, 100):
    if (i % 3 == 0):
        print("Fizz", end='')
        if (i % 5): print()
    if (i % 5 == 0):
        print("Buzz")
    if (i % 3 and i % 5):
        print(i)
