n = abs(int(input()))
mexrec = 1
suret = 0
for i in range(2, n*2+1, 2):
    mexrec *= i
for j in range(2, n*2+1, 2):
    suret += (mexrec / j) * (j-1)
cem = suret/mexrec
print(f"{cem:.3f}")