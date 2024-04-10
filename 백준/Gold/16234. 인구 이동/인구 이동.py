import sys
from collections import deque

def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N


def bfs(x, y):

    queue = deque()
    queue.append((x, y))
    lst = []
    lst.append((x, y))

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i] 
            ny = y + dy[i]

            if not is_valid(nx, ny) or visited[nx][ny]:
                continue
            
            if L <= abs(mp[nx][ny]-mp[x][y]) <= R:
                queue.append((nx, ny))
                lst.append((nx, ny))
                visited[nx][ny] = 1

    check.add(tuple(lst))    


N, L, R = map(int, sys.stdin.readline().split())
mp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0

while True:
    visited = [[0]*N for _ in range(N)]
    check = set()
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                bfs(i , j)

    for z in check:
        add = 0
        for a, b in z:
            add += mp[a][b]
        length = len(z)
        for x, y in z:
            mp[x][y] = add//length

    if len(check) == N**2:
        break
    count+= 1

print(count)