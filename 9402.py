 
a,b = map(int, input().split())
print("*" * b)
for i in range(a-2):
    print("*" + " " * (b-2) + "*")
print("*" * b)