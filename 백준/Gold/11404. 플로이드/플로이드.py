import sys
from heapq import heappop, heappush


def solution(start):

    hq = []
    heappush(hq, (0, start))
    dist[start] = 0

    while hq:
        cost, node = heappop(hq)

        if dist[node] < cost:
            continue

        for i in graph[node]:
            next_dist = i[1]
            next_node = i[0]

            new_dist = next_dist + cost

            if new_dist >= dist[next_node]:
                continue

            dist[next_node] = new_dist
            heappush(hq, (new_dist, next_node))



N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

for i in range(1, N+1):
    dist = [int(1e99) for _ in range(N+1)]
    solution(i)
    for i in range(len(dist)):
        if dist[i] == int(1e99):
            dist[i] = 0
    print(" ".join(map(str, dist[1:])))