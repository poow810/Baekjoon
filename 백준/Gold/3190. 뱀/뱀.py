import sys
from collections import deque

def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N


N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
mp = [[0] * N for _ in range(N)]
for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    mp[a-1][b-1] = 'a'
L = int(sys.stdin.readline())
dic = {}
for _ in range(L):
    a, b = map(str, sys.stdin.readline().split())
    dic[int(a)] = b

count = 0
dx = [0, 1, 0, -1] # 우 하 좌 상
dy = [1, 0, -1, 0]
direct = 0
x, y = 0, 0
queue = deque()
while True:
    if (x, y) == (0, 0) and (x, y) not in queue:
        queue.append((x, y))
    if count in dic:
        if dic[count] == 'D':
            direct = (direct + 1) % 4
        elif dic[count] == 'L':
            direct = (direct + 3) % 4
    nx = x + dx[direct]
    ny = y + dy[direct]
    count += 1    
    if not is_valid(nx, ny):
        break
    if (nx, ny) in queue:
        break
    if mp[nx][ny] == 'a':
        mp[nx][ny] = 0
        queue.append((nx, ny))
    elif mp[nx][ny] == 0:
        queue.popleft()
        queue.append((nx, ny))
    x, y = nx, ny

print(count)