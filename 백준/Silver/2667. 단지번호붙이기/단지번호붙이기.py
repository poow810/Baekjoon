import sys
from collections import deque

def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

def bfs(x, y):

    queue = deque()
    queue.append((x, y))
    mp[x][y] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        
        if visited[x][y] == 1:
            continue
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if is_valid(nx, ny) and visited[nx][ny] == 0 and mp[nx][ny] == 1:
                mp[nx][ny] = 0
                count += 1
                queue.append((nx, ny))

    return count


N = int(sys.stdin.readline())
mp = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[0] * (N) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
lst = []
for i in range(N):
    for j in range(N):
        if mp[i][j] == 1:
            lst.append(bfs(i, j))
lst.sort()
print(len(lst))
for i in lst:
    print(i)