#№ 8603
n=int(input())
if 99<n<1000:
    c=n%10
    b=n//10%10
    a=n//100
    print(a+b+c, a*b*c)