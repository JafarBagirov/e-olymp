
n = int(input())
l = list(map(int, input().split()))
a = []
maks = max(l)
mini = min(l)
for i in range(n):
    s = l[i] + mini - maks
    a.append(s)
print(*a)