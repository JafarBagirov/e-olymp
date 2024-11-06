 
n = int(input())
maks = 0
lst = list(map(float, input().split()))
for i in range(n):
    if abs(lst[i]) > maks:
        maks = abs(lst[i])
print(f"{maks:.2f}")