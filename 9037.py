 
n = int(input())
max_eded = int(max(str(n)))
t = 0
while n > 0:
    n -= max_eded
    t += 1
    max_eded = int(max(str(n)))
print(t)