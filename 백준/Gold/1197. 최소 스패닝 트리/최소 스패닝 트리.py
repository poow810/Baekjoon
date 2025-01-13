import sys
from heapq import heappop, heappush

def solution(node):

    visited = [0] * (V+1)
    hq = []
    heappush(hq, (0, node))
    total = 0

    while hq:
        weight, node = heappop(hq)

        if visited[node] == 1:
            continue

        visited[node] = 1
        total += weight

        for next_node, w in graph[node]:
            if visited[next_node] == 0:
                heappush(hq, (w, next_node))

    return total

V, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, w = map(int, sys.stdin.readline().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

answer = solution(1)

print(answer)