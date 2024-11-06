 
n = int(input())
s = str(n)
s2 = s.count("2")
s5 = s.count("5")
if s2 > s5:
    print("2")
elif s2 < s5:
    print("5")
else:
    print("=")