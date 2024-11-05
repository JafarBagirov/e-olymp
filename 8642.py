
a,b = map(int, input().split())
for i in range(a, b):
    s=str(i)
    if (int(s[0]) ** 4 + int(s[1]) ** 4 + int(s[2]) ** 4 + int(s[3]) ** 4) == i:
        print(i, end = " ")