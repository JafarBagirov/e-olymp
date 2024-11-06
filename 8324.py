n = int(input())
s = set()
for i in range(n):
    x = int(input())
    if x in s:
        print("Yes", len(s))
    else:
        s.add(x)
        print("No", len(s))