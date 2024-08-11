import sys
from heapq import heappush, heappop

def solution(start):
    
    queue = []
    heappush(queue, (0, start))
    visited[start] = 0
    
    while queue:
        count, node = heappop(queue)
        
        if count > visited[node]:
            continue
        
        for i in graph[node]:
            next_count = count + 1
            if next_count < visited[i]:
                visited[i] = next_count
                heappush(queue, (next_count, i))
                

N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [int(1e99)] * (N+1)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)

solution(X)
ans = []
for i in range(1, len(visited)):
    if visited[i] == K:
        ans.append(i)

if ans:
    for i in ans:
        print(i)

else:
    print(-1)