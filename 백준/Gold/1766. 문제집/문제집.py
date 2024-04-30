import sys
from heapq import heappop, heappush

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
indegree = [0] *(N+1)
queue = []

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1, N+1):
    if indegree[i] == 0:
        heappush(queue, i)

while queue:
    node = heappop(queue)
    print(node, end=" ")

    for i in graph[node]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heappush(queue, i)


