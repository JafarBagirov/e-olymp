n = int(input())
for i in range(n):
    row = ""
    for j in range(n):
        if (i + j) % 2 == 0:
            row += '*'
        else:
            row += ' '
    print(row)