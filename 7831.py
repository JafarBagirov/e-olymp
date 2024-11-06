 
n = int(input())
s = 0
lst = list(map(int, input().split()))
maks = max(lst)
for i in range (n):
    if lst[i] != maks:
        s += lst[i]
print(s)