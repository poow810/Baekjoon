import sys, copy
from collections import deque


def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < M


def dfs(lv):
    global count

    if lv == 3:
        np = bfs()
        c = 0
        for z in range(N):
            for k in range(M):
                if np[z][k] == 0:
                    c += 1
        count = max(count, c)
        return 

    for i in range(N):
        for j in range(M):
            if mp[i][j] == 0:
                mp[i][j] = 1
                dfs(lv + 1)
                mp[i][j] = 0


def bfs():

    np = copy.deepcopy(mp)
    queue = deque()
    for i in range(N):
        for j in range(M):
            if np[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if not is_valid(nx, ny):
                continue

            if np[nx][ny] == 0:
                np[nx][ny] = 2
                queue.append((nx, ny))
    
    return np


N, M = map(int, sys.stdin.readline().split())
mp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0
dfs(0)
print(count)