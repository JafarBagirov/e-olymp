n = int(input())
m = 0
t = 1
while n != 0:
    r  = n % 10
    if r % 2 == 0:
        r += 1
        m += r*t
        t *= 10
    else:
        r -= 1
        m += r*t
        t *= 10
    n //= 10
print(m)