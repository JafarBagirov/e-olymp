 
import math
from functools import reduce
n = int(input())
l = list(map(int, input().split()))
gcd_result = reduce(math.gcd, l)
print(gcd_result)