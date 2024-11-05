#№ 9935
m = int(input())
gd = 1440
gn = m // gd + 1
qd = m % gd
s = qd // 60
d = qd % 60
print(gn, s, d)