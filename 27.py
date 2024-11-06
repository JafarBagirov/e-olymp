 
max_num = int(input())
eded = bin(max_num)[2:]
dovr = len(eded)
for i in range(1, dovr):
    eded = eded[1:] + eded[0]
    cari = int(eded, 2)
    if cari > max_num:
        max_num = cari
print(max_num)