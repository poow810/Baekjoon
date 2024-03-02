from collections import deque

def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N


def bfs(x, y):
    global max_house

    queue = deque()
    queue.append((x, y))
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    house = 0
    k = 0

    if mp[x][y] == 1:
        house += 1

    while queue:
        x, y = queue.popleft()
        if visited[x][y] == k + 1:
            k = visited[x][y]
            cost = k * k + (k-1) * (k-1)
            if cost <= M * house:
                if max_house < house:
                    max_house = house

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not is_valid(nx, ny):
                continue

            if visited[nx][ny] != 0:
                continue

            visited[nx][ny] = visited[x][y] + 1

            if mp[nx][ny] == 1:
                house += 1
            queue.append((nx, ny))

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    mp = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    max_house = 0

    for i in range(N):
        for j in range(N):
            bfs(i, j)

    print(f"#{t+1}", max_house)