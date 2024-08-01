import sys
from collections import deque


def bfs(node):
    
    queue = deque()
    queue.append((node, 0))
    visited = [-1]*(N+1)
    
    while queue:
        node, count = queue.popleft()
        visited[node] = count
        
        for i in mp[node]:
            if visited[i] == -1:
                visited[i] = count + 1
                queue.append((i, count + 1))
    
    return visited
    

N, M = map(int, sys.stdin.readline().split())
mp = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    mp[A].append(B)
    mp[B].append(A)
    

v = bfs(1)
b = max(v)
for i in range(len(v)):
    if v[i] == b:
        a = i
        break
c = v.count(b)
print(a, b, c)
        