import sys
from collections import deque


def bfs(start):
    global min_num

    queue = deque()
    queue.append(start)
    visited = [0] * (N+1)
    visited[start] = 1

    while queue:
        node = queue.popleft()
        for i in lst[node]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[node] + 1
    
    ans.append((start, max(visited)-1))

N = int(sys.stdin.readline())
lst = [[] for _ in range(N+1)]
while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1:
        break
    lst[a].append(b)
    lst[b].append(a)

ans = []
for i in range(1, N+1):
    min_num = 1e99
    bfs(i)

result = []
c = 1e99
for k in ans:
    if k[1] < c:
        c = k[1]

count = 0
for j in ans:
    if j[1] == c:
        result.append((j[0], j[1]))
        count += 1

print(c, count)
for z in result:
    print(z[0], end = " ")