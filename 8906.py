n = int(input())
if n % 11 == 0:
    print(n-11)
else:
    s = n % 11
    print(n-s)