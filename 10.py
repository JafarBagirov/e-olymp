 
v = 0
m = 0
n = int(input())
i = n
while(v <= 0.5):
    v = v + 1/i
    i = i - 1
    m += 1
print(n - m + 1)