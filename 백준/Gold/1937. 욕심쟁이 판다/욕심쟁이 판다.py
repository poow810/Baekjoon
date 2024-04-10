import sys
import copy
from collections import deque


def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N


def dfs(x, y):
    
    if dp[x][y] != 0:
        return dp[x][y]
    
    dp[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not is_valid(nx, ny):
            continue

        if mp[nx][ny] > mp[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    return dp[x][y]

N = int(sys.stdin.readline())
mp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dp = [[0] * N for _ in range(N)]


max_day = 0
for i in range(N):
    for j in range(N):
        max_day = max(max_day, dfs(i, j))

print(max_day)


