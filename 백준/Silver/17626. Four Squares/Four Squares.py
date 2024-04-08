import sys


N = int(sys.stdin.readline())
dp = [0] * (N + 1)

k = 1
while k**2 <= N:
    dp[k**2] = 1
    k += 1

for i in range(1, N+1):
    if dp[i] != 0:
        continue
    check = 0
    while check**2 <= i:
        if dp[i] == 0:
            dp[i] = dp[check**2] + dp[i-check**2]
        else:
            dp[i] = min(dp[i], dp[check**2] + dp[i-check**2])
        check +=1

print(dp[N])
    