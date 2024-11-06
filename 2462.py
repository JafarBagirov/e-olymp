 
n = input()
n = n.replace(" ", "")
if n[0::] == n[::-1]:
    print("YES")
else:
    print("NO")