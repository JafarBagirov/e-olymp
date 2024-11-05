 
a,b = map(int, input().split())
if b != 0:
    if a % b == 0:
        print(a // b)
    else:
        print("ERROR")
else:
    print("ERROR")