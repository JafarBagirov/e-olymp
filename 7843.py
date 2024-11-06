 
n = int(input())
lst = list(map(int, input().split()))
for i in range(1, n):
    if lst[i] > lst[i-1]:
        print(lst[i], end = " ")