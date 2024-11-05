pi,itd,pd = map(int, input().split())
pid = (pi + itd + pd) / 2
p = pid - itd
i = pid - pd
d = pid - pi
print(p, i, d)