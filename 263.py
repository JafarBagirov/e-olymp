 
n = int(input())
dp = [0] * (n + 4)
dp[1], dp[2], dp[3] = 2, 4, 7
for i in range(4, n + 1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 12345
print(dp[n])