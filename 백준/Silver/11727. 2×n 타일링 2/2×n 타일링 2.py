import sys

N = int(sys.stdin.readline().rstrip())
dp = [0]*1001
dp[0] = 0
dp[1] = 1
dp[2] = 3
dp[3] = 5
for i in range(4, 1001):
    dp[i] = dp[i-1] + 2*dp[i-2]
    
print(dp[N]%10007)