import sys
from heapq import heappop, heappush


def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N


def solution(x, y):

    hq = []
    heappush(hq, (mp[0][0], x, y))
    visited[x][y] = mp[x][y]

    while hq:
        rupy, x, y = heappop(hq)

        if visited[x][y] < rupy:
            continue 
        
        visited[x][y] = rupy
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not is_valid(nx, ny):
                continue

            new_rupy = rupy + mp[nx][ny]
            if new_rupy >= visited[nx][ny]:
                continue
            visited[nx][ny] = new_rupy
            heappush(hq, (new_rupy, nx, ny))

count = 0
while True:
    count += 1
    N = int(sys.stdin.readline())
    if N == 0:
        exit()
    mp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    visited = [[int(1e99)]*N for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    solution(0, 0)
    print(f"Problem {count}: {visited[N-1][N-1]}")