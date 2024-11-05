n = int(input())
s = str(n)
s1 = 0
h = False

for i in range(len(s)):
    if int(s[i]) % 2 == 0:
        s1 += int(s[i])
        h = True
if h:
    print(s1)
else:
    print("-1")