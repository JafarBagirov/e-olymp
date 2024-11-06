n = int(input())

qiymet = (n // 100) * 100
if n % 100 > 65:
    qiymet += 100
else:
    qiymet += (n % 100 // 20) * 30
    if n % 20 > 15:
        qiymet += 30
    else:
        qiymet += (n % 20) * 2
print(qiymet)