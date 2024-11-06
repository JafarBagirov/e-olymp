n = int(input())
print('*' * n)
print('*' + ' ' * (n - 2) + '*') if n > 1 else print('*')
print('*' * n)