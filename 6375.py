 
n = int(input())
b = []
for i in range (n):
    for a in range(1):
        m = [int(i) for i in input().split()]
        c = max(m)
        b.append(c)
for j in range(1, n+1):
    print(f"Case #{j}: {b[j-1]}" )