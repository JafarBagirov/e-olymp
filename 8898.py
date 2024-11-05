 
import math
n = int(input())
s = math.sqrt(n)
if int(s) == s:
    result = (int(s) + 1) ** 2
else:
    s1 = math.ceil(s)
    result = s1 ** 2
print(result)