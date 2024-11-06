a, b = map(int, input().split())
if a % 2 == 0:
    a += 1
if b % 2 == 0:
    b -= 1
if a > b:
    s = 0
else:
    d = 2
    n = (b - a) // 2 + 1
    s = (2 * a + d * (n - 1)) * n // 2
print(s)