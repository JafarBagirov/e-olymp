n = int(input())
m = abs(n)
if m % 2 == 0: 
    s = (1+m) * m // 2
else: 
    s = (m+1) // 2 * m
if n > 0: 
    print(s)
else: 
    print(1-s)

