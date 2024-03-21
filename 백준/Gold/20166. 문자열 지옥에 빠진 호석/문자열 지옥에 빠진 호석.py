import sys
from collections import deque

def is_valid(nx, ny):
    if nx < 0:
        nx = N - 1
    elif nx >= N:
        nx = 0
    
    if ny < 0:
        ny = M - 1
    elif ny >= M:
        ny = 0
    
    if nx < 0 and ny < 0:
        nx, ny = N - 1, M - 1
    elif nx >= M and ny >= M:
        nx, ny = 0, 0
    return nx, ny

def bfs(x, y):

    queue = deque()
    queue.append((x, y, mp[x][y]))

    while queue:
        x, y, string = queue.popleft()

        if len(string) > 5:
            continue

        if string in dic:
            dic[string] += 1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            nx, ny = is_valid(nx, ny)
            queue.append((nx, ny, string + mp[nx][ny]))


N, M, K = map(int, sys.stdin.readline().split())
mp = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
dic = {}
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
for _ in range(K):
    a = sys.stdin.readline().strip()
    dic.setdefault(a, 0)

for i in range(N):
    for j in range(M):
        bfs(i, j)

for j in dic:
    print(dic[j])