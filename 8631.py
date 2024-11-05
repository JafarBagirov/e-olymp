 
n = int(input())
s = str(n)
s1 = 0
maks = max(s)
for i in range (0, len(s)):
    if s[i] == maks:
        s1 = s1 + 1
print(s1)