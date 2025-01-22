import sys
from collections import deque

def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N


def bfs(x, y):

    queue = deque([(x, y)])
    visited[x][y] = 1

    count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not is_valid(nx, ny):
                continue

            if mp[nx][ny] != '0' and visited[nx][ny] == 0:
                visited[nx][ny] = 1

                if mp[nx][ny] != '0':
                    count += 1
                queue.append((nx, ny))
    
    return count


N = int(sys.stdin.readline().strip())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0] * N for _ in range(N)]
mp = []
lst = []
for i in range(N):
    mp.append(list(map(str, sys.stdin.readline().strip())))

answer = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and mp[i][j] != '0':
            lst.append(bfs(i, j))
            answer += 1

print(answer)
lst.sort()
for i in lst:
    print(i)
