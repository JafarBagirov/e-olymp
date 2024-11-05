 
n = int(input())
a = []
s = str(n)
for i in range (len(s)):
    s1 = s[:i] + s[i+1:]
    a.append(int(s1))
    m = max(a)
print(m)