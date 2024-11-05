 
a,b = map(int, input().split())
s = 0
for i in range(a, b+1, 1):
    s = s + i*i
print(s)