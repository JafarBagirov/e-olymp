 
a,b = map(int, input().split())
for i in range (a, b+1, 1):
    s = str(i)
    if len(set(s)) == len(s):
        print(i, end = " ")