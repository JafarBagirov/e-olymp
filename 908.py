
n = int(input())
lst = list(map(int, input().split()))
s = 0
cem = 0
for i in range(n):
    if int(lst[i]) > 0:
        if int(lst[i]) % 6 == 0:
            s += 1
            cem += lst[i]
print(s, cem)