import sys
from collections import deque

def is_valid(nx, ny):
    return 0<= nx < R and 0 <= ny < C

def dfs(x, y, count):
    global ans
    
    if count == K and x == 0 and y == C-1:
        ans += 1
        return 
    
    visited[x][y] = 1
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if is_valid(nx, ny) and mp[nx][ny] == '.' and not visited[nx][ny]:
            visited[nx][ny] = 1 
            dfs(nx, ny, count+1)
            visited[nx][ny] = 0
    


R, C, K = map(int, sys.stdin.readline().split())
mp = [list(sys.stdin.readline().strip()) for _ in range(R)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
x, y = R-1, 0
ans = 0
visited = [[0]*C for _ in range(R)]
dfs(x, y, 1)
print(ans)