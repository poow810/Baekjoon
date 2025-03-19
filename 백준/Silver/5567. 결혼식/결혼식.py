import sys
from collections import deque

def bfs():

    visited = [0] * (n+1)
    queue = deque()
    queue.append(1)
    visited[1] = 1

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = visited[node] + 1
    
    return visited


n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = bfs()
answer = 0
for i in visited:
    if i == 2 or i == 3:
        answer += 1

print(answer)