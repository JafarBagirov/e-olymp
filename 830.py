def sade(m,n):
    sade_tapilde = False
    for eded in range(m,n+1):
        if eded > 1:
            sadedir = True
            for i in range(2, int(eded**0.5)+1):
                if eded % i == 0:
                    sadedir = False
                    break
            if sadedir:
                print(eded)
                sade_tapilde = True
    if not sade_tapilde:
        print("Absent")
                
m,n = map(int, input().split())
sade(m, n)