import sys
from collections import deque

def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < M

def bfs(mp):

    queue = deque()
    count = 0

    for i in range(N):
        for j in range(M):
            if mp[i][j] == 1:
                queue.append((i, j))
                mp[i][j] = 0
                visited[i][j] = 1
                
                while queue:
                    x, y = queue.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if not is_valid(nx, ny):
                            continue

                        if mp[nx][ny] == 1 and visited[nx][ny] == 0:
                            mp[nx][ny] = 0
                            queue.append((nx, ny))
                            visited[nx][ny] = 1
                else:
                    count += 1
    return count

T = int(sys.stdin.readline())
for t in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    mp = [[0] * (M) for _ in range(N)]
    visited = [[0] * (M) for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(K):
        x, y = map(int, sys.stdin.readline().split())
        mp[y][x] = 1

    print(bfs(mp))
