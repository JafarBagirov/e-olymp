 
n = int(input())
if n % 10 == 0:
    print(n + 10)
else:
    s = 10 - (n % 10)
    print(n + s)