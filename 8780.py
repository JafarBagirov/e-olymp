#№ 8780
n = int(input())
m = float('inf')
for _ in range(n):
    w, h = map(int, input().split())
    ma = max(w, h)
    mi = min(w, h)
    if ma <= m:
        m = ma
    elif mi <= m:
        m = mi
    else:
        print("NO")
        break
else:
    print("YES")