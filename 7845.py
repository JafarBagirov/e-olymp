 
n = int(input())
m = [int(i) for i in input().split()]
s = 0
for i in range(1, n-1):
    if m[i-1] < m[i] and m[i] > m[i+1]:
        s += 1
print(s)