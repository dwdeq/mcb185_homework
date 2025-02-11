def prime(n):
    for i in range (2,n):
        if (n % i == 0):
            return False
    return True

for i in range(1,51):
    print(i, end='')
    if (prime(i)):
        print('*', end='')
    print()