N = int(input())
answer = 0
M = 0

while M * M < N:
    M += 1
M -= 1
answer += M * (M + 1) * 2
answer += (N - M * M) * 2
answer += 1
if N - M * M > M:
    answer += 1

print(answer)