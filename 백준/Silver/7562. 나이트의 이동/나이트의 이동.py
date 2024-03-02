import sys
from collections import deque

def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N


def bfs(x, y):

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        
        if (x, y) == (end_x, end_y):
            return mp[x][y]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not is_valid(nx, ny):
                continue

            if mp[nx][ny] != 0:
                continue

            mp[nx][ny] = mp[x][y] + 1
            queue.append((nx, ny))


T = int(input())
for _ in range(T):
    N = int(input())
    start_x, start_y = map(int, sys.stdin.readline().split())
    end_x, end_y = map(int, sys.stdin.readline().split())
    mp = [[0] * N for _ in range(N)]
    dx = [-2, -2, 2, 2, -1, -1, 1, 1]
    dy = [-1, 1, -1, 1, -2, 2, -2, 2]

    print(bfs(start_x, start_y))