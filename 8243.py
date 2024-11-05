n = int(input())
if n > 0:
    while n > 9:
        n = n // 10
    if n > 0:
        print(n)
else:
    n = n*-1
    while n > 9:
        n = n // 10
    if n > 0:
        print(n)