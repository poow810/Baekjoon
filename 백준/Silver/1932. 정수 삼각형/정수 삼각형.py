import sys

N = int(sys.stdin.readline().strip())
dp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for i in range(1, N):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = dp[i][j] + dp[i-1][j]
        elif j == len(dp[i])-1:
            dp[i][j] = dp[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j]

print(max(dp[N-1]))

