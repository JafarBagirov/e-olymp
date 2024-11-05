 
n = int(input())
res = 0
for _ in range(n):
    num, price = input().split()
    num = int(num)
    price = float(price)
if price < 50.0:
    res += num
print(res)