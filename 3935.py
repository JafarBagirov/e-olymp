 
n = int(input())
s = []
for i in range(n):
    b = int(input())
    s.append(b)
print(*s[::-1])