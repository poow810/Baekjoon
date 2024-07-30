import sys
from collections import deque

def is_valid(nx, ny):
    return 0 <= nx < n and 0 <= ny < m

def bfs(x, y):
    global max_count
    
    queue = deque()
    queue.append((x, y))
    count = 1
    mp[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not is_valid(nx, ny):
                continue
            
            if mp[nx][ny] == 1:
                count += 1
                mp[nx][ny] = 0
                queue.append((nx, ny))
    return count

n, m = map(int, sys.stdin.readline().split())
mp = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_count = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
c = 0
for i in range(n):
    for j in range(m):
        if mp[i][j] == 1:
            max_count = max(max_count, bfs(i, j))
            c += 1
print(c)
print(max_count)