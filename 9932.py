
n = int(input())
if n % 1024 == 0:
    print(n // 1024)
else:
    print(n // 1024 + 1)