import sys

T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())

    dp = [1] * 10001

    for i in range(2, 10001):
        dp[i] += dp[i-2]

    for j in range(3, 10001):
        dp[j] += dp[j-3]

    print(dp[N])