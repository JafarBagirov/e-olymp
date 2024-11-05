 
n = int(input())
s = str(n)
if len(s) == len(set(s)):
    print("YES")
else:
    print("NO")