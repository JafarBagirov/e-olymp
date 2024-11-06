 
a, b = input(), input()
if len(a) > len(b):
    print(">")
elif len(a) < len(b):
    print("<")
elif a == b:
    print("=")
elif a > b:
    print(">")
else:
    print("<")