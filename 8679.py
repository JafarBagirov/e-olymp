 
n = int(input())
s = []
lst = list(map(int, input().split()))
for i in range (n):
    if lst[i] % 3 == 0:
        a = lst[i] // 3
        s.append(a)
    else:
        s.append(lst[i])
        print(*s)