 
n = input()
s = 0
vowels = "AYOUIE"
for i in n:
    if i in vowels:
        s += 1
print(s)