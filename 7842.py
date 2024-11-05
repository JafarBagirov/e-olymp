 
n = int(input())
lst = list(map(int, input().split()))
for i in range(0, n, 2):
    print(lst[i], end = " ")