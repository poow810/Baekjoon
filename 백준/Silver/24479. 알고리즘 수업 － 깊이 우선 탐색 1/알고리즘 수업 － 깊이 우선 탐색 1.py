import sys
sys.setrecursionlimit(10 ** 6)

def dfs(start, visited):
    global count
    visited[start] = count
    
    for i in graph[start]:
        if visited[i] == 0:
            count += 1
            dfs(i, visited)


N, M, R = map(int, sys.stdin.readline().split())
visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]
count = 1
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for j in graph:
    j.sort()

dfs(R, visited)

for i in range(1, N+1):
    print(visited[i])


