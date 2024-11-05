 
m = int(input())
level = 0
while str(m) != str(m)[::-1]:
    reversed_m = int(str(m)[::-1])
    m += reversed_m
    level += 1
print(level)