import sys
from collections import deque

def bfs(start):
    
    queue = deque()
    visited = [0] * (N+1)
    queue.append(start)

    while queue:
        node = queue.popleft()
        visited[node] = 1
        print(node, end=" ")

        for i in graph[node]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)


def dfs(start):

    visited_dfs[start] = 1
    print(start, end=" ")

    for i in graph[start]:
        if visited_dfs[i] == 0:
            dfs(i)


N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited_dfs = [0] * (N+1)

for i in graph:
    i.sort()

dfs(V)
print()
bfs(V)