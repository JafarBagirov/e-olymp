 
n = int(input())
lst = list(map(int, input().split()))
s = 0
for i in range(n):
    if lst[i] > 0:
        s += 1
print(s)