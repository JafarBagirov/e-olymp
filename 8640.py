 
a, b = map(int, input().split())
for i in range(a, b + 1):
    x = i // 1000
    y = (i // 100) % 10
    z = (i // 10) % 10
    u = i % 10
    if x % 2 == 1 and y % 2 == 1 and z % 2 == 1 and u % 2 == 1:
        print(i, end=' ')