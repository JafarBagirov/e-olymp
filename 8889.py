
n = int(input())
c = 0
for _ in range(5):
    d = n % 10
    if d % 2 != 0:
        c = c + 1
    n = n // 10
print(c)