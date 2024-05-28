import sys

def is_valid(nx, ny):
    return 0 <= nx < R and 0 <= ny < C

def dfs(x, y, lv):
    global max_lv

    max_lv = max(lv, max_lv)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not is_valid(nx, ny) or mp[nx][ny] in path:
            continue

        path.add(mp[nx][ny])
        dfs(nx, ny, lv + 1)
        path.remove(mp[nx][ny])


R, C = map(int, sys.stdin.readline().split())
mp = [list(sys.stdin.readline().strip()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0]*C for _ in range(R)]
path = set()
max_lv = 0

path.add(mp[0][0])

dfs(0, 0, 1)
print(max_lv)
