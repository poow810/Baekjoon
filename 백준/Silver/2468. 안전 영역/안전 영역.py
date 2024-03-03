import sys
from collections import deque

def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

def bfs(x, y, height):
    global count

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
                
            if visited[nx][ny] != 0:
                continue

            if mp[nx][ny] <= height:
                continue
            
            visited[nx][ny] = 1
            queue.append((nx, ny))
    count += 1


N = int(sys.stdin.readline())
mp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_num = 0
for i in range(N):
    for j in range(N):
        if mp[i][j] > max_num:
            max_num = mp[i][j]

max_count = 0
for j in range(max_num):
    visited = [[0] * N for _ in range(N)]
    count = 0
    for k in range(N):
        for z in range(N):
            if mp[k][z] > j and visited[k][z] == 0:
                bfs(k, z, j)
    
    if max_count < count:
        max_count = count

print(max_count)