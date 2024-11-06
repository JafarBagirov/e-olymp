def solve():
    n = int(input())
    res = 0

    ans = list(map(int, input().split()))

    for i in range(1, n - 1):
        if ans[i - 1] % 2 == 0 and ans[i + 1] % 2 == 0:
            res += 1
    print(res)
solve()
