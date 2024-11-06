 
n = input()
if len(n) == 4 and len(set(n)) == 2 and all(n.count(x) == 2 for x in set(n)):
    print("YES")
else:
    print("NO")