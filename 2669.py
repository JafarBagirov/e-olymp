def solve():
    n, m = map(int, input().split())
    v = [list(map(int, input().split())) for _ in range(n)]
    
    print(m, n) 
    for i in range(m):
        print(*[v[j][i] for j in range(n-1, -1, -1)])

solve()
