#№ 8522
a,b=map(int, input().split())
if a % b > 0:
    s1=a//b
    s2=a%b
    print(s1, s2)
else:
    print("Divisible")