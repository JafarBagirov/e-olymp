 
n = int(input())
s = []
i1 = 2
i2 = 2
while i2 < n:
    s.append(i2)
    i2 = 2**i1
    i1 += 1
print(*s)