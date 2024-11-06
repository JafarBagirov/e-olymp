import sys
for i in sys.stdin:
    a = list(map(int, i.split()))
    for n in a:
        print(n*4, n**2)