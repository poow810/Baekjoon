import sys
from heapq import heappop, heappush


def solution(start, end):

    hq = []
    heappush(hq, (0, start))
    distance[start] = 0

    while hq:
        dist, cur = heappop(hq)

        if cur == end:
            return dist

        if distance[cur] < dist:
            continue
        

        for i in node[cur]:
            next_dist = i[0]
            next_node = i[1]

            new_dist = dist + next_dist

            if new_dist >= distance[next_node]:
                continue

            distance[next_node] = new_dist
            heappush(hq, (new_dist, next_node))

    return "INF"

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
node = [[] for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    node[u].append((w, v))

ans = []
distance = [int(1e99)] * (V+1)
solution(K, 0)
for j in range(1, V+1):
    if int(distance[j]) == int(1e99):
        print("INF")
    else:
        print(distance[j])