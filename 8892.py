 
n = int(input())
if n % 2 != 0 or (n % 2 == 0 and 99 < n < 1000):
    print("YES")
else:
    print("NO")