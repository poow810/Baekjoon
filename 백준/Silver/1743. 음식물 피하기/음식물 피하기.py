import sys
from collections import deque

def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < M


def bfs(x, y):

    visited[x][y] = 1
    queue = deque()
    queue.append((x, y))
    count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not is_valid(nx, ny):
                continue

            if visited[nx][ny] == 0 and mp[nx][ny] == '#':
                count += 1
                visited[nx][ny] = 1
                queue.append((nx, ny))
    
    return count



N, M, K = map(int, sys.stdin.readline().split())
mp = [['.' for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(K):
    a, b = map(int, sys.stdin.readline().split())
    mp[a-1][b-1] = '#'

visited = [[0] * M for _ in range(N)]

max_size = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and mp[i][j] == '#':
            max_size = max(max_size, bfs(i, j))

print(max_size)
