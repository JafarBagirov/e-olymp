 
n = int(input())
a = []
lst = list(map(float, input().split()))
for i in range(n):
    if lst[i] > 0:
        a.append(lst[i])
if a:
    s = sum(a) / len(a)
    print(f"{s:.2f}")
else:
    print("Not Found")