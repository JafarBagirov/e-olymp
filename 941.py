 
n = int(input())
if n < 0: n = -n
a = n // 100
b = (n // 10) % 10
c = n % 10
res = a * b * c - (a + b + c)
print(res)