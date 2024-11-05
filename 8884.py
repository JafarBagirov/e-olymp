a,b,c = map(int, input().split())
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("equilateral")
    elif a == b != c or a == c != b or b == c != a:
        print("isosceles")
    else:
        print("versatile")
else:
    print("invalid")