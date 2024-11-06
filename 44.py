MAX = 5001
res = [0] * MAX

n = int(input())
res[1] = 1

for i in range(2, n + 1):
    res[i] = i
    for j in range(1, (i // 2) + 1):
        if res[j] + res[i - j] < res[i]:
            res[i] = res[j] + res[i - j]
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            if res[j] + res[i // j] < res[i]:
                res[i] = res[j] + res[i // j]

print(res[n])