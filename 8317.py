 
n = int(input())
s = str(n)
s_1 = "".join(sorted(s))
s_2 = "".join(sorted(s, reverse = True))
s_3 = int(s_2) - int(s_1)
print(s_3**2)