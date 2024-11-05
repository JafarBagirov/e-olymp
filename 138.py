 
n = int(input())
s = 0
c = [500, 200, 100, 50, 20, 10]
for i in range(6):
    s = s + n // c[i]
    n = n % c[i]
if n > 0:
    print("-1")
else:
    
    print(s)