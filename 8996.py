 
n = input()
yeni_n = ""
for i in range(len(n)):
    if n[i] not in yeni_n:
        yeni_n += n[i]
print(yeni_n)