 
n = int(input())
lst = list(map(int, input().split()))
lst = sorted(lst)
for i in range (n):
    print(lst[i], end = " ")