
import math
n = int(input())
s = math.log2(n)
if 2 ** int(s) == n:
    print("YES")
else:
    print("NO")