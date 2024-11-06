 
n = input()
say = n.count(" ")
if say != 0:
    s = n.index(" ")
    s1 = n.rindex(" ")
    print(s, s1)
else:
    print("-1")