def yoxla(a, b, c, d):
    if (a == b and c == d) or (a == c and b == d) or (a == d and b == c):
        return "YES"
    return "NO"
setir = input()
massiv = setir.split(' ')

a = float(massiv[0])
b = float(massiv[1])
c = float(massiv[2])
d = float(massiv[3])

print(yoxla(a, b, c, d))