import sys

N = int(sys.stdin.readline().strip())

dp = [0]*(N+1)
path = ["" for _ in range(N+1)]
path[1] = "1"

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    pre = i-1

    if i % 3 == 0 and dp[i//3] + 1 < dp[i]:
        dp[i] = dp[i//3]+1
        pre = i // 3
    if i % 2 == 0 and dp[i//2] + 1 < dp[i]:
        dp[i] = dp[i//2]+1
        pre = i // 2

    path[i] = str(i) + " " + path[pre]

print(dp[N])
print(path[N])

        