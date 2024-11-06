n,m = map(int, input().split())
matris = []
for i in range(m):
    setir = [int(i) for i in input().split()]
    matris.append(setir)
ardicil = []
for j in range(m):
    a = matris[j].count(min(matris[j]))
    b = matris[j].count(max(matris[j]))

    s = ((sum(matris[j])) - a*min(matris[j]) - b*max(matris[j])) / (len(matris[j]) - a - b)

    ardicil.append(f"{s:.2f}")
print(" ".join(ardicil))