a, b = map(int,input().split())

dp = [[float('inf')] * 2 for _ in range(b+1)]    
dp[a][0] = 0

for i in range(a, b + 1):
    dp[i][0] = min(dp[i-1][0]+1, dp[i][0])
    dp[i][1] = min(dp[i-1][1]+1, dp[i][1])
    if not i%10:
        dp[i][1] = min(dp[i//10][0] +1, dp[i][1])
    if not i%2:
        dp[i][0] = min(dp[i//2][0]+1, dp[i][0])
        dp[i][1] = min(dp[i//2][1]+1, dp[i][1])

print(min(dp[b][0],dp[b][1]))