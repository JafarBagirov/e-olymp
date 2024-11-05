 
n = int(input())
s = []
for i in range (1, n+1, 1):
    if n % i == 0:
        s.append(i)
print(sum(s))