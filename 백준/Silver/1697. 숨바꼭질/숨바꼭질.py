import sys
from collections import deque

def bfs(cur):

    queue = deque()
    queue.append(cur)
    visited[cur] = 1

    while queue:
        cur = queue.popleft()

        if cur == K:
            return visited[cur] - 1

        for i in range(3):
            if i == 0:
                next = cur - 1
            elif i == 1:
                next = cur + 1
            else:
                next = cur * 2

            if 0 <= next <= 100000:
                if visited[next] == 0:
                    visited[next] = visited[cur] + 1
                    queue.append(next)

N, K = map(int, sys.stdin.readline().split())
visited = [0] * 100001
print(bfs(N))
