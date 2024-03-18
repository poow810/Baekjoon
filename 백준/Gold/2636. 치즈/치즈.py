import sys
from collections import deque


def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < M

def bfs(x, y):

    queue = deque()
    queue.append((x, y))
    mp[x][y] = 9

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not is_valid(nx, ny):
                continue

            if mp[nx][ny] == 0:
                mp[nx][ny] = 9
                queue.append((nx, ny))


def bfs2():
    global second

    check = 0
    for g in range(N):
        for h in range(M):
            if mp[g][h] == 1:
                check+=1
    if check != 0:
        ans.append(check)
    if check == 0:
        return

    queue = deque()
    for i in range(N):
        for j in range(M):
            if mp[i][j] == 1:
                queue.append((i, j))

    pos = []
    while queue:
        x, y = queue.popleft()
        count = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if mp[nx][ny] == 9:
                count += 1
        if count >= 1:
            pos.append((x, y))

    for a, b in pos:
        mp[a][b] = 9
    
    check_bfs()
    second += 1
    bfs2()


def check_bfs():

    queue = deque()
    check = deque()
    for i in range(N):
        for j in range(M):
            if mp[i][j] == 0:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if mp[nx][ny] == 9:
                mp[x][y] = 9
                check.append((x, y))
    while check:
        x, y = check.popleft()

        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]

            if mp[nx][ny] == 0:
                mp[nx][ny] = 9
                check.append((nx, ny))


N, M = map(int, sys.stdin.readline().split())
mp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = []
second = 0
bfs(0, 0)

bfs2()
print(second)
print(ans[-1])

