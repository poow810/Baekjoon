import sys
from collections import deque

def bfs(start):

    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        node = queue.popleft()

        for next in graph[node]:
            if not visited[next]:
                visited[next] = -visited[node]
                queue.append(next)
            
            elif visited[node] == visited[next]:
                return False
    
    return True


K = int(sys.stdin.readline().strip())

for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    answer = True
    visited = [0] * (V+1)
    for i in range(1, V+1):
        if not visited[i]:
            answer = bfs(i)

        if not answer:
            print("NO")
            break
    
    else:
        print("YES")