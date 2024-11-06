 
n = int(input())
s = []
for i in range(n):
    a = int(input())
    s.append(a)
s = sorted(s, key=lambda x: (x % 10, x))
print(s)