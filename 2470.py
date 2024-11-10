def solve():
    n = int(input())
    m = []
    for i in range(n):
        row = list(map(int, input().split()))
        m.append(row)

    success = True
    for i in range(n):
        for j in range(i, n):
            if (i == j and m[i][j] != 0) or (j > i and m[j][i] != m[i][j]):
                success = False
                break
        if not success:
            break

    print("YES" if success else "NO")
solve()
