 
n = int(input())
arr = list(map(int, input().split()))
unique_arr = []
for number in arr:
    if number not in unique_arr:
        unique_arr.append(number)
print(*unique_arr)