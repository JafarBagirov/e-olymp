n=int(input())
s=str(n)
d=0
s1=1
while len(s) > d:
    if int(s[d]) != 0:
        s1=int(s[d])*s1
    d=d+1
print(s1)