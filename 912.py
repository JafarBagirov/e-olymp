 
s = input()
c = 0
for i in range(len(s) - 1):
    if (s[i+1] in '.!?' and s[i] not in '.!?'):
        c += 1
print(c)