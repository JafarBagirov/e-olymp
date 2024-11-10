n = int(input())
say = 0
for _ in range(n):
    b = int(input())
    if b == 1:
        say += 1
if say > n / 2:
    print(n-say)
else:
    print(say)
