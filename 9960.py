n = int(input())
l = list(map(int, input().split()))

s = [x for x in l if x % 2 == 0]
if s:
    s = min(s)
    ind = l.index(s)
    print(ind, s)
else:
    print("NO")