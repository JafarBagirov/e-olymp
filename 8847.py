 
n = int(input())
s = n // 1000
a = n % 1000 // 100
b = n // 10 % 10
c = n % 10
print(s*1000+c*100+b*10+a)