 
import sys
input = sys.stdin.read
data = input().splitlines()
for line in data:
    n, m = map(int, line.split())
    perimeter = 2 * (n + m)
    area = n * m
print(perimeter, area)