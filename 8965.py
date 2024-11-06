 
n = int(input())
lst = list(map(int, input().split()))
minu = -(min(lst) // 2)
for i in range(n):
    lst[i] = lst[i] + minu
print(*lst)