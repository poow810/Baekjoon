import sys
from collections import deque


def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < M


def fire_bfs(fire):

    while fire:
        x, y = fire.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not is_valid(nx, ny):
                continue

            if mp[nx][ny] != '#' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                fire.append((nx, ny))


def bfs(x, y, count):

    queue = deque()
    queue.append((x, y, count))
    
    while queue:
        x, y, count = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not is_valid(nx, ny):
                return count
            
            if mp[nx][ny] != '#':
                if (count + 1) < visited[nx][ny] and visited[nx][ny] != -1 or visited[nx][ny] == 0:
                    visited[nx][ny] = -1
                    queue.append((nx, ny, count + 1))
    
    return 'IMPOSSIBLE'

T = int(sys.stdin.readline())
for _ in range(T):
    M, N = map(int, sys.stdin.readline().split())
    mp = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    fire = deque()    
    for i in range(N):
        for j in range(M):
            if mp[i][j] == '*':
                fire.append((i, j))
                visited[i][j] = 1
         
            elif mp[i][j] == '@':
                a, b = i, j
    
    fire_bfs(fire)
    print(bfs(a, b, 1))

    