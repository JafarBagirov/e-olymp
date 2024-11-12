def solve():
    n = int(input())
    ans = 1

    for i in range(1, n + 1):
        if i == n and i != 1:
            k = 5
        elif i == n and i == 1:
            k = 4
        elif i == 1:
            k = 4
        else:
            k = 5
        ans *= k

    print(ans)

solve()
