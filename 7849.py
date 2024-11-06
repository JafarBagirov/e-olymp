 
n = int(input())
arr = list(map(int, input().split()))
max_value = max(arr)
min_value = min(arr)
for i in range(n):
    if arr[i] == max_value:
        arr[i] = min_value
    elif arr[i] == min_value:
        arr[i] = max_value
print(*arr)