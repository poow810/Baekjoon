import sys


def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < M


def dfs(x, y):
    global ans

    if dp[x][y] != -1:
        return dp[x][y]

    if (x, y) == (N-1, M-1):
        return 1
    
    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not is_valid(nx, ny):
            continue
        
        if mp[nx][ny] < mp[x][y]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

N, M = map(int, sys.stdin.readline().split())
mp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dfs(0, 0)
print(dp[0][0])