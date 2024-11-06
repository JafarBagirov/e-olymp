 
n = int(input())
l = list(map(int, input().split()))
a = []
for i in range(n):
    s = l.count(l[i])
    if s == 1:
        a.append(l[i])
print(*a)