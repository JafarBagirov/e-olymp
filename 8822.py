def solve():
    n = int(input())
    ans = 1
    for i in range(1, n + 1):
        if i == n and i != 1:
            k = 9
        elif i == n and i == 1:
            k = 8
        elif i == 1:
            k = 8
        else:
            k = 9
        ans *= k
    print(ans)
solve()
