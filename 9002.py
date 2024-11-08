n, a, b = map(int, input().split())
ans = a * (n // 2) + b * (n // 2) + max(a, b) * (1 if n % 2 != 0 else 0)
print(ans)
