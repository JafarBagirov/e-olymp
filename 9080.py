 
import math
n,r = map(int, input().split())
n = n * 60 * 24
r = r * 1000
s = r / n
d = math.ceil(s)
print(d)