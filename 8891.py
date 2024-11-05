 
n = int(input())
s = 0
if n % 2 == 0:
    s += 1
if n < 0 and n % 3 == 0:
    s += 1
if s == 1:
    print("YES")
else:
    print("NO")