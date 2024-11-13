def f(n, l):
    s = 0
    for i in range(n - 1):
        x1, y1 = l[i]
        x2, y2 = l[i + 1]
        s += (x1 * y2 - x2 * y1)
    
    x1, y1 = l[n - 1]
    x2, y2 = l[0]
    s += (x1 * y2 - x2 * y1)
    
    s = abs(s) / 2
    return round(s, 3)

n = int(input())

l = []
for _ in range(n):
    x, y = map(int, input().split())
    l.append((x, y))

s = f(n, l)

print(s)
