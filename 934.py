import math
a,b,c = map(int, input().split())
perimetr = (a+b+c) / 2
sahe = math.sqrt(perimetr*(perimetr-a)*(perimetr-b)*(perimetr-c))
ha = 2 / a * sahe
hb = 2 / b * sahe
hc = 2 / c * sahe
print(f"{ha:.2f} {hb:.2f} {hc:.2f}")