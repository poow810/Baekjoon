import sys
import copy
from collections import deque


def is_valid(nx, ny):
    return 0 <= nx < R and 0 <= ny < C


def up_air():

    d = 0
    before = 0
    x, y = air[0][0], air[0][1]+1
    while True:
        nx = x + dx[d]
        ny = y + dy[d]

        if nx == R or ny == C or nx == -1 or ny == -1:
            d = (d-1)%4
            continue

        if x == air[0][0] and y == air[0][1]:
            break

        np[x][y] , before = before, np[x][y]
        x, y = nx, ny


def down_air():

    d = 0 
    before = 0
    x, y = air[1][0], air[1][1]+1

    while True:
        nx = x + dx[d]
        ny = y + dy[d]

        if nx == R or ny == C or nx == -1 or ny == -1:
            d = (d+1)%4
            continue

        if x == air[1][0] and y == air[1][1]:
            break

        np[x][y], before = before, np[x][y]
        x, y = nx, ny


R, C, T = map(int, sys.stdin.readline().split())
mp = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
dx = [0, 1, 0, -1] # 동남서북
dy = [1, 0, -1, 0]
air = []
for _ in range(T):
    np = copy.deepcopy(mp)
    for i in range(R):
        for j in range(C):
            if mp[i][j] == -1:
                air.append((i, j))

            if mp[i][j] != 0 and mp[i][j] != -1:
                spread = mp[i][j]//5
                count = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    
                    if not is_valid(nx, ny) or mp[nx][ny] == -1:
                        count += 1
                        continue
                    
                    np[nx][ny] += spread
                np[i][j] -= spread*(4-count)
    
    up_air()
    down_air()
    mp = np

res = 0
for i in range(R):
    for j in range(C):
        if mp[i][j] != 0 and mp[i][j] != -1:
            res += mp[i][j]
        
print(res)
