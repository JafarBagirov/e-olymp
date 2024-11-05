 
a, sign, b = input().split()
a = int(a)
b = int(b)
if sign == "+":
    s = a + b
if sign == "-":
    s = a - b
if sign == "*":
    s = a * b
if sign == "/":
    s = a // b
print(s)