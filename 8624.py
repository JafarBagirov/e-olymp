 
n = int(input())
s = len(set(str(n)))
if s == 4 or s == 3 or s == 2 or s == 1:
    print("YES")
else:
    print("NO")