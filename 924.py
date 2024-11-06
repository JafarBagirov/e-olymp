import math

setir = input()
massiv = setir.split(' ')

s = float(massiv[0])
r1 = float(massiv[1])
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862
r2 = math.sqrt(r1 * r1 - s / pi)

print(f"{r2:.2f}")