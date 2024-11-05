#№ 943
n=int(input())
if 99<n<1000:
    a=n//100
    b=n//10%10
    c=n%10
    print(c*100+b*10+a)