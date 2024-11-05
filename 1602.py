 
import math
a,b = map(int, input().split())
s = math.gcd(a, b)
s1 = (a * b) // s
print(s1)