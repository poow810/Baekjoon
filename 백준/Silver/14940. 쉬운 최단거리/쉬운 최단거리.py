import sys
from collections import deque


def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < M


def bfs(x, y):

    queue = deque()
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 0
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not is_valid(nx, ny):
                continue
            
            if mp[nx][ny] == 0:
                continue

            if visited[nx][ny] == 0 and mp[nx][ny] != 2:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
            
    return visited

N, M = map(int, sys.stdin.readline().split())
mp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(N):
    for j in range(M):
        if mp[i][j] == 2:
            ans = bfs(i, j)

for z in range(N):
    for k in range(M):
        if mp[z][k] == 1 and ans[z][k] == 0:
            ans[z][k] = -1

for i in ans:
    print(" ".join(map(str, i)))