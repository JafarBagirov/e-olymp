# I method
m,n,k = map(int, input().split())
print(m // n, end='')
if k > 0:
    print(".", end='')
curk = 0
curm = (m % n) * 10
while curk < k:
    if curm == 0:
        print("0", end='')
        curk += 1
    elif curm < n:
        print("0", end='')
        curm *= 10
        curk += 1
    else:
        print(curm // n, end='')
        curm = (curm % n) * 10
        curk += 1

# II method

m,n,k=map(int,input().split())
print(str(m//n)+".",end="")
m=m%n
for i in range(1,k+1):
    m=m*10
    print(m//n,end="")
    m=m%n