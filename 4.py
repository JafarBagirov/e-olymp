import math
setir = input()
massiv = list(map(float, setir.split()))

x1, y1, r1, x2, y2, r2 = massiv

mesafe = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
cr = r1 + r2
fr = abs(r1 - r2)

if mesafe == cr:
    print("1")
elif mesafe > cr:
    print("0")
elif mesafe == 0:
    print("-1" if abs(r1 - r2) < 1e-9 else "0")
elif 0 < mesafe < cr:
    if fr < mesafe:
        print("2")
    elif fr == mesafe:
        print("1")
    elif fr > mesafe:
        print("0")
