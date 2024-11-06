a, b = map(int, input().split())

if a > b:
    a, b = b, a

kol = b - a - 1
if kol % 2 == 0:
    ans = kol // 2
else:
    ans = kol // 2 + (1 if (b - 1) % 2 == 0 else 0)

print(ans)