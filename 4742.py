import math

n = int(input())
res = 1

for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        c = 0
        while n % i == 0:
            n = n // i
            c = c + 1
        res = res * (c + 1)

if n > 1:
    res = res * 2

print(res - 2)