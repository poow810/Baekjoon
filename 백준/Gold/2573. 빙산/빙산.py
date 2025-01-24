import sys
from collections import deque


def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < M

def melt(x,y):

    for t in range(4):
        nx = x + dx[t]
        ny = y + dy[t]
        
        if not is_valid(nx, ny):
            continue

        if mp[nx][ny]==0:
            sea[x][y]+=1


def bfs(x, y):
    global temp

    queue = deque()
    queue.append((x, y))
    temp += 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not is_valid(nx, ny):
                continue
            
            if mp[nx][ny] != 0 and visited[nx][ny]==0:
                queue.append((nx, ny))
                visited[nx][ny] = temp


N, M = map(int, sys.stdin.readline().split())
mp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

sea = [[0 for _ in range(M)] for _ in range(N)]
year = 0

while True:
    temp = 0
    count = 0
    year += 1
    visited = [[0 for _ in range(M)] for i in range(N)]
    
    for i in range(N): 
        for j in range(M):
            if mp[i][j] > 0:
                count += 1 
                melt(i, j)
    
    if count == 0: 
        print(0)
        break
    
    for i in range(N): 
        for j in range(M):
            if mp[i][j] > sea[i][j]:
                mp[i][j] -= sea[i][j]
                sea[i][j] = 0
            else:
                mp[i][j] = 0
                sea[i][j] = 0 


    for i in range(N): 
        for j in range(M):
            if mp[i][j] > 0 and visited[i][j] == 0: 
                bfs(i, j) 
    if temp >= 2:
        print(year)
        break