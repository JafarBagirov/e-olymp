 
import sys
sum = 0
for line in sys.stdin:
    for var in line.split():
        sum = sum + int(var)
print(sum)