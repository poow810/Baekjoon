import sys
from collections import deque


def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < M


def bfs(x, y):
    global answer

    visited[x][y] = 1
    queue = deque()
    queue.append((x, y))
    
    flag = True
    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if not is_valid(nx, ny):
                continue

            if mp[nx][ny] > mp[x][y]:
                flag = False

            if visited[nx][ny] == 1:
                continue


            if mp[nx][ny] == mp[x][y]:
                visited[nx][ny] = 1
                queue.append((nx, ny))
    
    if flag:
        answer += 1
    return


N, M = map(int, sys.stdin.readline().split())

mp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]
answer = 0

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:

            bfs(i, j)

print(answer)
