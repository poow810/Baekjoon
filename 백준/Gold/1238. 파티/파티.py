import sys
from heapq import heappop, heappush

def solution(start):

    distance = [1e99] * (N+1)
    hq = []
    heappush(hq, (0, start))
    distance[start] = 0

    while hq:
        dist, cur = heappop(hq)

        if distance[cur] < dist:
            continue

        for i in graph[cur]:
            next_dist = i[0]
            next_node = i[1]

            new_dist = next_dist + dist

            if new_dist >= distance[next_node]:
                continue

            distance[next_node] = new_dist
            heappush(hq, (new_dist, next_node))
    return distance


N, M, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([c, b])

path1 = solution(X)
path1[0] = 0
max_count = 0
for i in range(1, N+1):
    dis = solution(i)
    path1[i] += dis[X]

print(max(path1))