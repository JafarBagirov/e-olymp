 
n = int(input())
if (9 < n < 100) or (-100 < n < -9):
    if  n % 3 == 0 and n % 2 == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")