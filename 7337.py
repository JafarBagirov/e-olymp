 
a,b,c = map(int, input().split())
s = [a, b, c]
s1 = sorted(s)
print(s1[2] + s1[0])