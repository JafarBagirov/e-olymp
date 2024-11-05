 
r, w, l = map(int, input().split())
d = w*w + l*l
if d > 4*r*r:
    print("NO")
else:
    print("YES")