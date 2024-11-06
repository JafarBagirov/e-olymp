n = int(input())
if n < 0:
    n *= -1
s = str(n)
succes = False
product = 1
for c in s:
    if '0' <= c <= '9':
        digit = int(c)
        if digit % 2 == 0:
            product *= digit
            succes = True

print(product if succes else -1)