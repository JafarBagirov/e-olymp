 
import math
n = int(input())
s = math.log2(n)
if int(s) == s:
    result = 2 ** (int(s) + 1)
else:
    s1 = math.ceil(s)
    result =  2 ** s1
print(result)