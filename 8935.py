 
a,b = map(int, input().split())
if a % 2 != 0:
    for i in range (a, b+1, 2):
        print(i, end = " ")
else:
    for i in range (a+1, b+1, 2):
        print(i, end = " ")