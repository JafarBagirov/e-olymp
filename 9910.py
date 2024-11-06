 
a,b = map(int, input().split())
if a > b:
    a,b = b,a
if b % 2 == 0:
    print((b-a)//2)
else:
    print((b-a-1)//2)