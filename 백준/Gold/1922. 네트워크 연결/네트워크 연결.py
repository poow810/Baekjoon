import sys
from heapq import heappop, heappush

def prim(start):
    
    hq = []
    visited = [0] * N
    sum_weight = 0
    heappush(hq, (0, start))

    while hq:
        weight, node = heappop(hq)

        if visited[node] == 1:
            continue

        visited[node] = 1
        sum_weight += weight

        for i in range(N):
            if not visited[i] and graph[node][i] != 0:
                heappush(hq, (graph[node][i], i))

    return sum_weight 

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
graph = [[0] * N for _ in range(N)]

for _ in range(M):
    a, b, w = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = w
    graph[b-1][a-1] = w

print(prim(0))