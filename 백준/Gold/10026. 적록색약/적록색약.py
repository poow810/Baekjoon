import sys
from collections import deque
import copy

def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

def bfs(mp, visited):

    queue = deque()
    count = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                queue.append((i, j))
                visited[i][j] = 1
                while queue:
                    x, y = queue.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if not is_valid(nx, ny):
                            continue

                        if mp[i][j] == mp[nx][ny] and visited[nx][ny] == 0:
                            queue.append((nx, ny))
                            visited[nx][ny] = 1
                else:
                    count += 1
    return count

N = int(sys.stdin.readline())
mp = [list(sys.stdin.readline().strip()) for _ in range(N)]
visit1 = [[0] * (N) for _ in range(N)]
visit2 = [[0] * (N) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ncolor = copy.deepcopy(mp)
for i in range(N):
    for j in range(N):
        if ncolor[i][j] == 'G':
            ncolor[i][j] = 'R'
print(bfs(mp, visit1), end = " ")
print(bfs(ncolor, visit2))