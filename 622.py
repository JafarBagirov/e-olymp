 
n = int(input())
s = 0
i = 0
while i < n:
    if n % 2 != 0:
        s = s + 1
        n = n // 2
    else:
        n = n // 2
print(s)