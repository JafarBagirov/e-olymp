 
a,b = map(int, input().split())
print("*" * b)
for _ in range(a-2):
    print("*" + " " * (b-2) + "*") if b > 1 else print("*")
if a > 1:
    print("*" * b)