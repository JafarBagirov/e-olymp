 
n = int(input())
i = 2
s = []
while i != n:
    if n % i == 0:
        s.append(i)
    i = i + 1
print(len(s)+2)