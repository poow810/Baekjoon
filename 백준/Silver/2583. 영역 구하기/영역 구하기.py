import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().split())

# 유기농 배추처럼 사각형 좌표들 visited = 1 처리해놓고,
# 전체 배열 순회하면서, 0인곳만 count하면 될듯?

def is_valid(nx, ny):
    return 0 <= nx < M and 0 <= ny < N

def bfs(x, y):
    
    queue = deque()
    queue.append((x, y))

    mp[x][y] = 1
    count = 1

    while queue:
        cur = queue.popleft()

        for i in range(4):
            nx = dx[i] + cur[0]
            ny = dy[i] + cur[1]

            if not is_valid(nx, ny):
                continue
            if mp[nx][ny] == 1:
                continue

            mp[nx][ny] = 1
            queue.append((nx, ny))
            count += 1
    ans.append(count)

mp = [[0]*N for _ in range(M)]
count = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = []

for i in range(K):
    a, b, c, d = map(int, sys.stdin.readline().split())
    for j in range(a, c): # x좌표는 a부터 c까지 -> 0부터 4
        for k in range(M-b-1, M-d-1, -1): # y좌표는 b부터 d까지 -> 2부터 4
            mp[k][j] = 1
    

for z in range(M):
    for s in range(N):
        if mp[z][s] == 0:
            bfs(z, s)


print(len(ans))
ans.sort()
for i in ans:
    print(i, end=" ")

