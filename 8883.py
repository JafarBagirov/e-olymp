 
a,b,c,d  = map(int, input().split())
s = sorted([a, b, c ,d])
if s[0] == s[1] and s[2] == s[3]:
    print(sum(s))
else:
    print("No")