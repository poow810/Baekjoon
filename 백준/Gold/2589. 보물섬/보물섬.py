import sys
from collections import deque


def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < M


def bfs(x, y, min_num):

    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not is_valid(nx, ny):
                continue

            if mp[nx][ny] != 'L' or visited[nx][ny] != 0:
                continue

            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))
    return visited[x][y] - 1


N, M = map(int, sys.stdin.readline().split())
mp = [list(sys.stdin.readline()) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_num = 0
for i in range(N):
    for j in range(M):
        if mp[i][j] == 'L':
            visited = [[0] * M for _ in range(N)]
            check = bfs(i, j, 1e99)
            if max_num < check:
                max_num = check

print(max_num)