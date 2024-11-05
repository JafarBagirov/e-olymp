 
n = int(input())
s1 = []
s = str(n)
for i in range (len(s)-1, -1, -1):
    s1.append(s[i])
print("".join(map(str, s1)))