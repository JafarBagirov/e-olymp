import math

n = int(input())

# Sadə ədəd olub-olmama yoxlaması
is_prime = True
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print("Yes")
else:
    print("No")