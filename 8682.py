 
n = input()
result = ''.join([digit for digit in n if int(digit) % 2 != 0])
if result:
    print(result)
else:
    print(0)