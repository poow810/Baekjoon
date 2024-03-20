from collections import deque


def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N


def bfs(start, end):

    queue = deque()
    a, b = start
    visited = [[10000]*N for _ in range(N)]
    queue.append((a, b))
    visited[a][b] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not is_valid(nx, ny):
                continue

            if visited[x][y] + mp[nx][ny] < visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + mp[nx][ny] 
                queue.append((nx, ny))
    
    return visited[N-1][N-1]


T = int(input())
for t in range(T):
    N = int(input())
    mp = [list(map(int, input().strip())) for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    print(f"#{t+1}", bfs((0, 0), (N-1, N-1)))
    