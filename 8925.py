 
n = int(input())
n = str(n)
s = 1
for i in range(len(n)):
    if int(n[i]) % 2 != 0:
        s *= int(n[i])
if s != 1:
    print(s)
else:
    print("-1")