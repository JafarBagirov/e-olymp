n = int(input())

if n == 3:
    for i in range(n):
        print('*' * n)
else:
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1 or i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()