 
n=1
s=[]
while n != 0:
    n = int(input())
    if n % 2 == 0:
        s.append(n)
print(sum(s))