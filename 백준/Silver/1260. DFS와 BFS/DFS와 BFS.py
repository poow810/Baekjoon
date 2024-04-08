import sys
from collections import deque


def dfs(start):
    
    visited1[start] = 1
    print(start, end = " ")

    for i in graph[start]:
        if visited1[i] == 0:
            dfs(i)


def bfs(start):

    queue = deque()
    queue.append(start)
    visited2[start] = 1

    while queue:
        node = queue.popleft()
        print(node, end = " ")
        for i in graph[node]:
            if visited2[i] == 0:
                visited2[i] = 1
                queue.append(i)


N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited1 = [0] * (N+1)
dfs(V)
print()

visited2 = [0] * (N+1)
bfs(V)