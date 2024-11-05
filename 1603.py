 
n = int(input())
if n < 0:
    n = -n
    s = list(map(int, str(n)))
    print (sum(s))
else:
    s = list(map(int, str(n)))
    print (sum(s))