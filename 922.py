
n = int(input())
lst = list(map(int, input().split()))
s = lst[-1:] + lst[:-1]
for i in s:
    print(i, end = " ")