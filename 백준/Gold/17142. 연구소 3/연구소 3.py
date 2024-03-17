import sys, copy
from collections import deque
from itertools import combinations


def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N


def bfs(np, check, check_zero):
    
    max_count = 0
    queue = deque()
    for a, b in check:
        np[a][b] = 1
        queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        max_count = max(max_count, np[x][y])

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if not is_valid(nx, ny):
                continue

            if np[nx][ny] == 0:
                check_zero -= 1              
                np[nx][ny] = np[x][y] + 1
                queue.append((nx, ny))

            if np[nx][ny] == '*':
                if check_zero == 0:
                    break
                np[nx][ny] = np[x][y] + 1
                queue.append((nx, ny))


    for z in range(N):
        for g in range(N):
            if np[z][g] == 0:
                return -1
    
    return max_count-1
    


N, M = map(int, sys.stdin.readline().split())
mp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
virus = []
zero_count = 0
for i in range(N):
    for j in range(N):
        if mp[i][j] == 1:
            mp[i][j] = '-'
        elif mp[i][j] == 2:
            virus.append((i, j))
        else:
            zero_count += 1

virus_lst = list(combinations(virus, M))
ans = set()
for v in virus_lst:
    np = copy.deepcopy(mp)
    check = []
    for x, y in virus:
        np[x][y] = '*'
    for c_x, c_y in v:
        mp[c_x][c_y] = 0
        check.append((c_x, c_y))
    ans.add(bfs(np, check, zero_count))

if len(ans) == 1 and -1 in ans:
    print(-1)
else:
    if -1 in ans:
        ans.remove(-1)
    print(min(ans))
