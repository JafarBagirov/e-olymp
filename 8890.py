n = int(input())
d=str(n)
a=0
l=[]
for _ in range(5):
    if int(d[a]) % 2 == 0:
        c=int(d[a])+1
        l.append(c)
        a=a+1
    else:
        l.append(int(d[a]))
        a=a+1
print("".join(map(str, l)))