import sys

def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

def dfs(x, y, state):
    global count

    visited = [0, 0, 0]

    if x == N-1 and y == N-1:
        count += 1
        return    

    if not is_valid(x, y):
        return
    
    if state == 0:
        visited[1] = 1
    elif state == 1:
        visited[0] = 1

    for i in range(3):
        if visited[i] == 0:
            nx = x + dx[i]
            ny = y + dy[i]

            if not is_valid(nx, ny):
                continue
            
            if mp[nx][ny] == 1:
                continue

            if i == 2:
                if mp[nx-1][ny] == 1 or mp[nx][ny-1] == 1 or mp[nx][ny] == 1:
                    return
            
            if mp[nx][ny] == 0:
                dfs(nx, ny, i)

N = int(sys.stdin.readline())
mp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [0, 1, 1] # 가로, 세로, 대각
dy = [1, 0, 1]
visited = [0, 0, 0]
count = 0

if mp[N-1][N-1] == 1:
    print(0)
else:
    dfs(0, 1, 0)
    print(count)