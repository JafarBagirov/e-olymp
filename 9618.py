 
n = int(input())
s = 0
lst = list(map(int, input().split()))
for i in range(n):
    if lst[i] < 0:
        s += lst[i]
if s:
    print(s)
else:
    print("0")