import sys
from heapq import heappush, heappop


def solution(start):

    hq = []
    heappush(hq, (0, start))
    visited[start] = 0

    while hq:
        price, cur = heappop(hq)

        if visited[cur] < price:
            continue

        for i in graph[cur]:
            next_price = i[0]
            next_node = i[1]

            new_price = price + next_price
            if new_price >= visited[next_node]:
                continue
            
            visited[next_node] = new_price
            heappush(hq, (new_price, next_node))


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
visited = [int(1e99)] * (N+1)
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([c, b])


s, e = map(int, sys.stdin.readline().split())
solution(s)
print(visited[e])