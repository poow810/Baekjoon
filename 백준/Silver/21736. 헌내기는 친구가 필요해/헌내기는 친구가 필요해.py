import sys
from collections import deque


def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < M

def bfs(x, y):

    queue = deque()
    queue.append((x, y))
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1
    count = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not is_valid(nx, ny) or visited[nx][ny] == 1:
                continue

            if mp[nx][ny] == 'O':
                visited[nx][ny] = 1
                queue.append((nx, ny))
            
            if mp[nx][ny] == 'P':
                visited[nx][ny] = 1
                count += 1
                queue.append((nx, ny))
        
    return count


N, M = map(int, sys.stdin.readline().split())
mp = [list(sys.stdin.readline().strip()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if mp[i][j] == 'I':
            x, y = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = bfs(x, y)
if ans == 0:
    print('TT')
else:
    print(ans)