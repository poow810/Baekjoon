from collections import deque

def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < M

def bfs(x, y):

    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    count = 1

    while queue:
        
        x, y = queue.popleft()
        if visited[x][y] == hour:
            return count
        
        for i in range(4):
            if pipe[mp[x][y]][i]:
                nx = x + dx[i]
                ny = y + dy[i]

                if not is_valid(nx, ny):
                    continue

                if mp[nx][ny] == 0:
                    continue 

                if visited[nx][ny] == 1:
                    continue
                
                c = 0
                for j in range(4):
                    if pipe[mp[nx][ny]][j] == 1:
                        check_x = nx + dx[j]
                        check_y = ny + dy[j]
                        if (check_x, check_y) == (x, y):
                            c += 1
                if c > 0:
                    if visited[nx][ny] == 0 and visited[nx][ny] < hour:
                        visited[nx][ny] = visited[x][y] + 1
                        count += 1
                        queue.append((nx, ny))
    return count

T = int(input())
for t in range(T):
    N, M, x, y, hour = map(int, input().split())
    mp = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    pipe = [[0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], 
            [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0]]
    print(f"#{t+1}", bfs(x, y))