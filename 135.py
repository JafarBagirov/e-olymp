import sys
from math import gcd

n = int(input())
setir = input().strip()
massiv = list(map(int, setir.split()))

ekob = massiv[0]

for i in range(1, n):
    ekob = ekob * massiv[i] // gcd(ekob, massiv[i])
print(ekob)
