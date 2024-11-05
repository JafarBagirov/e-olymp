#№ 8607
n=int(input())
a=0
if 999<n<10000:
    s=str(n)
    for i in s:
        i=int(i)
        a=a+i**2
    print(a)