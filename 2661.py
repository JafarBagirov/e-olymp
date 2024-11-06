n = int(input())
s = set()
lst1 = list(map(int,input().split()))
for x in lst1:
  s.add(x)
m = int(input())
lst2 = list(map(int,input().split()))
for x in lst2:
  s.add(x)
for x in sorted(s):
  print(x, end=' ')