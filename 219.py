def solve():
    a, b, c, d = map(int, input().split())
    res = a * b * c
    n = res // d
    i = n
    while True:
        if i * d >= res:
            print(i)
            return
        i += 1
solve()
