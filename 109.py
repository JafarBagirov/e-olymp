n = int(input())
sehife = 0
p = 9
i = 1

while True:
    if n <= i * p:
        if n % i != 0:
            print("0")
            break
        sehife += n // i
        print(sehife)
        break
    n -= p * i
    sehife += p
    p *= 10
    i += 1