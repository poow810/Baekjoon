import sys

N, M = map(int, sys.stdin.readline().split())
lst = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0]*100001
for i in range(1, N+1):
    dp[i] = dp[i-1] + lst[i]

for j in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(dp[b]-dp[a-1])