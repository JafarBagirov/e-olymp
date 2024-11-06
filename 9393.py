 
n = input()
yeni_n = ''
for i in n:
    if i.isdigit():
        if int(i) % 2 == 0:
            yeni_n += i
    else:
        yeni_n += i
print(yeni_n)