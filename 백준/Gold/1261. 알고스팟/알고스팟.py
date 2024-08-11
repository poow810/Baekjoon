import sys
from heapq import heappush, heappop

def is_valid(nx, ny):
    return 0 <= nx < M and 0 <= ny < N


def bfs(x, y):
    global ans
    
    queue = []
    heappush(queue, (x, y, 0))
    visited[x][y] = 0
    
    while queue:
        x, y, count = heappop(queue)

        if count > visited[x][y]:
            continue
                
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not is_valid(nx, ny):
                continue
            
            if count + mp[nx][ny] < visited[nx][ny]:
                visited[nx][ny] = count + mp[nx][ny]
                heappush(queue, (nx, ny, visited[nx][ny]))
    
    
N, M = map(int, sys.stdin.readline().split())
mp = [list(map(int, sys.stdin.readline().strip())) for _ in range(M)]
visited = [[int(1e99)] * N for _ in range(M)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs(0, 0)
print(visited[M-1][N-1])