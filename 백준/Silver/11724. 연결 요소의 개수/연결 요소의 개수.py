import sys

def dfs(node):

    stack = []
    stack.append(node)
    visited[node] = 1

    while stack:
        node = stack.pop()
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = 1
                stack.append(i)


N, M = map(int, sys.stdin.readline().split())
graph = [[]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(N+1)
count = 0 
for i in range(1, N+1):
    if visited[i] == 0:
        dfs(i)
        count += 1

print(count)