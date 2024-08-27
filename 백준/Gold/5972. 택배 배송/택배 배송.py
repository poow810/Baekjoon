import sys
from heapq import heappop, heappush


def solution(start):

    hq = []
    heappush(hq, [0, start])

    while hq:
        dist, node = heappop(hq)

        if visited[node] < dist:
            continue
        
        for w, c in graph[node]:
            new_dist = dist + w
            if new_dist < visited[c]:
                visited[c] = new_dist
                heappush(hq, [new_dist, c])


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [1e99] * (N+1)
for _ in range(M):
    a, b, w = map(int, sys.stdin.readline().split())
    graph[a].append([w, b])
    graph[b].append([w, a])

solution(1)
print(visited[N])