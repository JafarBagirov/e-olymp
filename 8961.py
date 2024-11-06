 
n = int(input())
arr = list(map(int, input().split()))
min_value = min(arr)
for i in range(n):
    if arr[i] == min_value:
        arr[i] = arr[0]
        arr[0] = min_value
        break
print(*arr)