import sys
sys.setrecursionlimit(10**6)

def dfs(current):
    global lv
    
    visited[current] = lv
    for i in graph[current]:
        if visited[i] == 0:
            lv += 1
            dfs(i)

N, M, R = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort(reverse=True)

visited = [0] * (N+1)
lv = 1

dfs(R)
for i in visited[1:]:
    print(i)