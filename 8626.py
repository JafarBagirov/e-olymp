#№ 8626
n=int(input())
a=n//100
b=n//10%100
c=n%100
if a==37 or b==37 or c==37:
    print("YES")
else:
    print("NO")