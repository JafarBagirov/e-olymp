 
n = int(input())
l = list(map(int, input().split()))
m = max(l)
i = l.index(m)
print(m, i+1)