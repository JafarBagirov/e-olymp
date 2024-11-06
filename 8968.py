n = int(input())
arr = list(map(int, input().split()))

a, b = arr[0], arr[0]
for i in range(1, n):
    a = max(a, arr[i]) 
    b = min(b, arr[i])  
a //= 2 
b //= 2 

for i in range(n):
    if arr[i] > 0:
        arr[i] -= a
    elif arr[i] < 0:
        arr[i] -= b 
    print(arr[i], end=" ")