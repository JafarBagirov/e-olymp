 
n = int(input())
lst = list(map(float, input().split()))
a = -1
for i in range(n):
    if lst[i] <= 2.5:
        a = i
        break
if a != -1:
    print(f"{a+1} {lst[a]:.2f}")
else:
    print("Not Found")