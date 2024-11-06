 
n = int(input())
lst = list(map(float, input().split()))
say = 0
cem = 0
for i in range(n):
    if lst[i] < 0:
        say += 1
        cem += lst[i]
print(say, end = " ")
print(f"{cem:.2f}")