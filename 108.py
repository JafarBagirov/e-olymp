 
a, b, c = map(int, input().split())
res = a + b + c - min(a, b, c) - max(a, b, c)
print(res)