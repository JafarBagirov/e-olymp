#№ 6266
W,H,w,h=map(int, input().split())
s1=W//w//2+W//w%2
s2=H//h//2+H//h%2
print(s1*s2)