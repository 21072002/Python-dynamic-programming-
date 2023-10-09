def fibonachi(n,dp):
    if n==0 or n==1:
        return n
    if dp[n] != -1:
        return dp[n]
    else:
        dp[n] = fibonachi(n-1,dp) + fibonachi(n-2,dp)
        return dp[n]

dp = [-1]*100
print(fibonachi(10,dp))
print(dp)