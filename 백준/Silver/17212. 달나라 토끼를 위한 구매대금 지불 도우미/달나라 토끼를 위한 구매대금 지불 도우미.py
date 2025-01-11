import sys

N = int(sys.stdin.readline().strip())

dp = [0] * 100001

dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[5] = 1
dp[4] = 2
dp[5] = 1
dp[6] = 2
dp[7] = 1

for i in range(7, N+1):
    dp[i] = min(dp[i-1], dp[i-2], dp[i-5], dp[i-7]) + 1

print(dp[N])
