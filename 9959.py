n = int(input())
l = list(map(int, input().split()))
s = 0
a = []
for i in l:
    if i % 5 == 0:
        a.append(i)
        s += 1
a.reverse()
if s:
    print(s)
    print(*a)
else:
    print("NO")