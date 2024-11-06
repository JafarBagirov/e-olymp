 
x, y, z = map(float, input().split())
res = min(min(max(x, y), max(y, z)), x + y + z)
print(res)