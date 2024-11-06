def solve():
    n = int(input())
    dp = [0] * (n + 105)
    dp[0] = 0
    dp[1] = 4

    for i in range(2, n + 101): 
        dp[i] = dp[i - 1] + 4
        if i >= 10:
            dp[i] = min(dp[i], dp[i - 10] + 30) 
        if i >= 50:
            dp[i] = min(dp[i], dp[i - 50] + 125) 
        if i >= 100:
            dp[i] = min(dp[i], dp[i - 100] + 200)  

    ans = float('inf')
    for i in range(n, n + 101):
        ans = min(ans, dp[i]) 
    print(ans)
solve()