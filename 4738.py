 
n = int(input())
l = list(map(int, input().split()))
s = sorted(l, reverse=True)
print(*s)