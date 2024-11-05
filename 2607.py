 
n = int(input())
s = str(n)
tek = 0
cut = 0
for i in range (0, len(s), 2):
    tek = tek + int(s[i])
for i in range (1, len(s), 2):
    cut = cut + int(s[i])
print(cut*tek)