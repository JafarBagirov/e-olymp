n = int(input()) 
k = n - 1

for i in range(n):
    for j in range(n):
        if j < k:
            print(2, end='')
        else:
            print(0 if j == k else 1, end='')
    print()
    k -= 1