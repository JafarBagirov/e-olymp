 
n = int(input())
lst = list(map(int, input().split()))
maks = max(lst)
minu = min(lst)
s = 0
for i in range(n):
    if lst[i] != maks and lst[i] != minu:
        s += lst[i]
print(s)