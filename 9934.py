#№ 9934
n=int(input())
a=n//3600
b=(n-a*3600)//60
c=n-a*3600-b*60
print(a, b, c)