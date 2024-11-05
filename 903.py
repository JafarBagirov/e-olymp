#№ 903
n=int(input())
a=n//100
b=n%10
if a>b:
    print(a)
elif a<b:
    print(b)
else:
    print("=")