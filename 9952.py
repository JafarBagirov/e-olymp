import math

a,b = map(int, input().split())
a = math.ceil(a**0.5)
b = int(b**0.5)
print(b-a+1)
