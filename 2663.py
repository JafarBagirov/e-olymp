def bubble_sort_with_swaps(arr):
    swaps = 0 
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return swaps


n = int(input())
arr = list(map(int, input().split()))
swap_count = bubble_sort_with_swaps(arr)
print(swap_count)