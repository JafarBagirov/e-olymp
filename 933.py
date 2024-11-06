 
n = int(input())
if n < 0:
    n = -n
cem = 0
while n > 0:
    cem += n % 10
    n //= 10
print(cem)