 
x, n, m = map(int, input().split())
res = 1
for i in range(1, n + 1):
    res = (res * x) % m
print(res)