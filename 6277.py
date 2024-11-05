 
n = int(input())
c = 0
n *= 100
while n >= 120:
    c += n // 120  # satılan butulkalar
    n = n % 120 + (n // 120) * 20  # yenilenmiş mebleg
print(c)