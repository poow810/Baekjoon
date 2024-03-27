import sys, copy

def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < M


def check(np, dir, x, y):

    for i in dir:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]

            if not is_valid(nx, ny):
                break

            if np[nx][ny] == 6:
                break

            elif np[nx][ny] == 0:
                np[nx][ny] = '#'


def dfs(lv, mp):
    global min_count

    if lv == len(cctv_lst):
        count = 0
        for i in range(N):
            count += mp[i].count(0)
        min_count = min(min_count, count)
        return
    
    np = copy.deepcopy(mp)
    x, y, c = cctv_lst[lv]
    for i in cctv[c]:
        check(np, i, x, y)
        dfs(lv + 1, np)
        np = copy.deepcopy(mp)


N, M = map(int, sys.stdin.readline().split())
mp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cctv = [[0], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 3], [1, 3], [1, 2], [0, 2]],
         [[0, 2, 3], [0, 1, 3], [1, 2, 3], [0, 1, 2]], [[0, 1, 2, 3]]]
cctv_lst = []
for i in range(N):
    for j in range(M):
        if 1 <= mp[i][j] <= 5:
            cctv_lst.append((i, j, mp[i][j]))


min_count = 1e99
dfs(0, mp)
print(min_count)