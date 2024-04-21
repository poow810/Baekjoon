import sys

N = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))

dp = [1]*(N)
dp[0] = 1

for i in range(1, N):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))