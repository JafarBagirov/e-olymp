
a, b = map(int, input().split())
for i in range(a, b+1):
    s = str(i)
    if len(s) == len(set(s)):
        print(i)