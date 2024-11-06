def guzgu(x):
    return int(str(x)[::-1])

def sade(x):
    if x == 0 or x == 1:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0:
        return False
    kok = int(x**0.5) + 1
    for i in range(3, kok, 2):
        if x % i == 0:
            return False
    return True

setir = input()
massiv = list(map(int, setir.split()))

a = massiv[0]
b = massiv[1]

if a > b:
    a, b = b, a

say = 0

for i in range(a, b + 1):
    if sade(i) and sade(guzgu(i)):
        say += 1
print(say)