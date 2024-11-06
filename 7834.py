 
n = int(input())
lst = list(map(int, input().split()))
s = sorted(lst)
print(int(s[-1]) + int(s[-2]))

