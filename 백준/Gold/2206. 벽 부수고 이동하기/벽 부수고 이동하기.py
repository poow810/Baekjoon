import sys
from collections import deque

def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < M

def bfs(x, y):
    global ans

    queue = deque()
    queue.append((x, y, 1))
    visited[x][y][1] = 1
    while queue:
        x, y, dig = queue.popleft()
       
        if x == N - 1 and y == M - 1:
            return visited[x][y][dig]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not is_valid(nx, ny):
                continue

            if dig == 1 and mp[nx][ny] == 1:
                visited[nx][ny][0] = visited[x][y][1] + 1
                queue.append((nx, ny, 0))

            elif visited[nx][ny][dig] == 0 and mp[nx][ny] == 0:
                visited[nx][ny][dig] = visited[x][y][dig] + 1
                queue.append((nx, ny, dig))
    return -1


N, M = map(int, sys.stdin.readline().split())
mp = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
print(bfs(0, 0))
