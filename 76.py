 
a,b,x,y,z = map(int, input().split())
if (a>x and b>y) or (a > y and b > x) or (a > y and b > z) or (a > z and b > y ) or (a > x and b > z) or (a > z and b > x):
    print("1")
else:
    print("0")