 
a, b = map(int, input().split())
s = 0
if b == 1:
    print(a * (a + 1) // 2)
else:
    for i in range(1, a + 1):
        c = i * (b ** i)
        s += c
    print(s)