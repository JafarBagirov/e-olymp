n = int(input())
cur = list(map(int, input().split()))

mn = int(1e9)
ans = None

for i in range(n):
    res = 0
    temp = cur[i]

    while temp:
        res += temp % 10
        temp //= 10
    if res <= mn:
        mn = res
        ans = cur[i]

print(ans)