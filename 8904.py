 
n = int(input())
s = 0
t = 1
while n > s:
    t += 1
    s = 2**t
print(s - (2**(t-1)))