import sys


N, K = map(int, sys.stdin.readline().split())
lst = [[0, 0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0]*(K+1) for _ in range(N+1)]

for y in range(1, N+1):
    w, v = lst[y][0], lst[y][1]
    for x in range(1, K+1):
        if x < w:
            dp[y][x] = dp[y-1][x]
        else:
            dp[y][x] = max(dp[y-1][x], dp[y-1][x-w] + v)
print(dp[N][K])