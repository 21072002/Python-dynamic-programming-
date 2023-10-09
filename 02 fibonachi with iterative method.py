dp = [0]*101
dp[0] = 0
dp[1] = 1
for i in range(2,101):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[10])
print(dp[99])





