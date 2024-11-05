 
n = int (input())
if n % 7 == 0:
    print(n+7)
else:
    s = n % 7
    s1 = 7 - s
    s2 = n + s1
    print(s2)