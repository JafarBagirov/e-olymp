 
n = int(input())
m = int(input())
if n < 0: n = -n
res = 0
while n > 0:
    if n % 10 == m:
        res += 1
    n = n // 10
print(res)