import sys
for line in sys.stdin:
    a, b, c = map(int, line.split())
    siyahi = sorted([a, b, c])
    if sum(siyahi) != 0:
        if siyahi[0]**2 + siyahi[1]**2 == siyahi[2]**2:
            print("right")
        else:
            print("wrong")
    else:
        break