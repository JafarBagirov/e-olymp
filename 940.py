n = int(input())
m = list(map(int, input().split()))

maj = 0
cnt = 0

for num in m:
    if cnt == 0:
        maj = num
        cnt += 1
    elif num == maj:
        cnt += 1
    else:
        cnt -= 1

cnt = 0
for num in m:
    if num == maj: cnt += 1

if 2 * cnt > n: res = maj
else: res = -1

print(res)