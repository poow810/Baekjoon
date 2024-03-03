import sys
from collections import deque

def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < M

def bfs():
    global ans

    queue = deque()
    visited = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if mp[i][j] == 1:
                queue.append((i, j))
                visited[i][j] = 1
    while queue:
        x, y = queue.popleft()

        ans = max(ans, visited[x][y] - 1)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not is_valid(nx, ny):
                continue

            if visited[nx][ny] != 0:
                continue
            
            if mp[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                mp[nx][ny] = 2
                queue.append((nx, ny))


M, N = map(int, sys.stdin.readline().split())
mp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0 
bfs()
for i in range(N):
    for j in range(M):
        if mp[i][j] == 0:
            print(-1)
            exit()

print(ans)