n,m = map(int, input().split())
count = 1
matrix = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(count)
        count += 1
    matrix.append(row)

for row in matrix:
    print(" ".join(map(str, row)))