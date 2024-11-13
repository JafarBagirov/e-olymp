def solve():
    n, p, q, k = map(int, input().split())
    kve = n // (p * q)
    ans = 1
    while k > kve * q:
        k -= kve * q
        ans += 1
    print(ans, end=" ")

    ans = 1
    while k > kve:
        k -= kve
        ans += 1
    print(ans)

solve()
