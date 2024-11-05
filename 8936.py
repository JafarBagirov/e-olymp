 
a,b = map(int, input().split())
if b % 2 == 0:
    for i in range (b, a-1, -2):
        print(i, end = " ")
else:
    for i in range (b-1, a-1, -2):
        print(i, end = " ")