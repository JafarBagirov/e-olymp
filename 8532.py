 
a,b = map(int, input().split())
for i in range (a, b+1, 1):
    print(i*i, end = " ")
print()
for i in range (b, a-1, -1):
    print(i**3, end = " ")