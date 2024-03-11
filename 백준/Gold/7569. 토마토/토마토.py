import sys
from collections import deque


def is_valid(nz, nx, ny):
    return 0 <= nz < H and 0 <= nx < N and 0 <= ny < M 

def bfs():
    global ans

    queue = deque()
    visited = [[[0]*M for __ in range(N)] for _ in range(H)]

    for s in range(H):
        for i in range(N):
            for j in range(M):
                if mp[s][i][j] == 1:
                    queue.append((s, i, j))
                    visited[s][i][j] = 1
    
    while queue:
        z, x, y = queue.popleft()

        ans = max(ans, visited[z][x][y] - 1)
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if not is_valid(nz, nx, ny):
                continue

            if visited[nz][nx][ny] != 0:
                continue
            
            if mp[nz][nx][ny] == 0:
                visited[nz][nx][ny] = visited[z][x][y] + 1
                mp[nz][nx][ny] = 2
                queue.append((nz, nx, ny))


M, N, H = map(int, sys.stdin.readline().split())
mp = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for __ in range(H)]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
ans = 0 

bfs()
for z in range(H):
    for i in range(N):
        for j in range(M):
            if mp[z][i][j] == 0:
                print(-1)
                exit()

print(ans)