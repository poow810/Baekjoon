from collections import deque

def is_valid(nx,ny):
    return 0 <= nx < N and 0 <= ny < N

def bfs(start_x, start_y):

    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 1

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if not is_valid(nx, ny):
                continue

            if mp[nx][ny] == 3:
                return 1
            
            if mp[nx][ny] == 0 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return 0

for t in range(10):
    N = 16
    T = int(input())
    mp = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * (N) for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(N):
        for j in range(N):
            if mp[i][j] == 2:
                x, y = i, j
    
    print(f"#{t+1}", bfs(x, y))