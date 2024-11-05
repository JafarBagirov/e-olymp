 
import math
n = int(input())
s = math.log10(n)
if 10 ** int(s) == n:
    print(int(s))
else:
    print("No")