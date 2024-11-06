n = int(input())
t = 1
if n < 0:
    n *= -1
    t = -1
a = n//100
b = n//10%10
c = n%10
print(t*(a*110000+b*1100+c*11))