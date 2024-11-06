 
n = int(input())
l = list(map(int, input().split()))
a = []
for i in range(1, n, 2):
    a.append(l[i])
    a.append(l[i-1])
if n % 2 != 0:
    a.append(l[-1])
print(*a)