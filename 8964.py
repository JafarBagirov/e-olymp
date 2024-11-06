 
n = int(input())
lst = list(map(int, input().split()))
s = max(lst)
for i in range(n - 1, -1, -1):
    if lst[i] == s:
        lst.pop(i)
        lst.append(s)
print(*lst)