 
n = int(input())
s = 0
a = []
lst = list(map(int, input().split()))
for i in range (n):
    if lst[i] % 2 == 0:
        s = s + 1
        a.append(lst[i])
if a:
    print(s)
    print(*a[::-1])
else:
    print("NO")