import sys
from heapq import heappop, heappush

def solution(start, end):
    global min_num


    if start == end:
        return 0
    
    hq = []
    heappush(hq, (0, start))
    visited = [int(1e99)] * (N+1)

    while hq:
        w, node = heappop(hq)
        
        if node == end:
            return visited[node]

        if visited[node] < w:
            continue

        for i in graph[node]:
            next_w = i[0]
            next_node = i[1]

            new_w = w + next_w
            
            if new_w >= visited[next_node]:
                continue
            
            visited[next_node] = new_w
            heappush(hq, (new_w, next_node))
    
    print(-1)
    exit()


N, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
min_num = 1e99
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, sys.stdin.readline().split())
a = solution(1, v1) + solution(v1, v2) + solution(v2, N)
b = solution(1, v2) + solution(v2, v1) + solution(v1, N)
print(min(a, b))