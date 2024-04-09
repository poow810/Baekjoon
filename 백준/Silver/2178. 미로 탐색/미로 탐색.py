import sys
from collections import deque


def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < M

def bfs(x, y):

    queue = deque()
    queue.append((x, y, 1))
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1

    while queue:
        x, y, count = queue.popleft()
        if (x, y) == (N-1, M-1):
            return count
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not is_valid(nx, ny) or visited[nx][ny] == 1 or mp[nx][ny] == '0':
                continue
            
            if mp[nx][ny] == '1':
                visited[nx][ny] = 1
                queue.append((nx, ny, count+1))


N, M = map(int, sys.stdin.readline().split())
mp = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
print(bfs(0, 0))