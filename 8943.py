 
n = int(input())
print('*' * 3)
for _ in range(n - 2):
    print('*' + ' ' * 1 + '*')
if n > 1:
    print('*' * 3)