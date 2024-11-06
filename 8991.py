 
s = input()
d = ""
for c in s:
    if c.isalpha():
        d += c * 2
else:
    d += c
print(d)