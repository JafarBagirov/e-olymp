 
n = int(input())
s = []
s1 = str(n)
s2 = len(s1)
for i in range(0, s2, 1):
    if int(s1[i]) % 2 != 0:
        s.append(s1[i])
print(len(s))