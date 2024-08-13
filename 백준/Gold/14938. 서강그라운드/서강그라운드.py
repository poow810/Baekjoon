import sys
from heapq import heappop, heappush

def solution(node):

    visited = [1e99] * (n+1)
    queue = []
    heappush(queue, (0, node))
    visited[node] = 0
    
    while queue:
        dist, node = heappop(queue)
        
        for next_dist, next_node in graph[node]:
            if next_dist + dist < visited[next_node]:
                visited[next_node] = next_dist + dist
                heappush(queue, (visited[next_node], next_node))

    return visited

n, m, r = map(int, sys.stdin.readline().split())
lst = [0] + list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, w = map(int, sys.stdin.readline().split())
    graph[a].append((w, b))
    graph[b].append((w, a))


max_count = 0

for i in range(1, len(graph)):
    count = 0
    result = solution(i)
    
    for j in range(1, n+1):
        if result[j] <= m:
            count += lst[j]
        
    max_count = max(max_count, count)
print(max_count)