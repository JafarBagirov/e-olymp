#№ 947
n=int(input())
if 99<n<1000:
    a=n//100
    b=n//10%10
    c=n%10
    print(str(c)+str(b)+str(a))