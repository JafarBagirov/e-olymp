import math

n = int(input())
list = []
for i in range(1, int(math.sqrt(n))):
    if n % i == 0:
        list.append(i)
        list.append(n//i)

i = int(math.sqrt(n));
if n % i == 0: list.append(i);

list.sort()
print(*list, sep=" ")