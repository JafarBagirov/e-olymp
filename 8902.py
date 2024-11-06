n = int(input())

if n % 2 != 0:
    n += 1
    while n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        n = n + 1
    print(n)
else:
    while n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        n = n + 1
    print(n)