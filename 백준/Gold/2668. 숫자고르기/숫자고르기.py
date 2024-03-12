import sys


def dfs(start):

    stack = []
    visited = [0] * (N+1)
    for i in range(len(graph[start])):
        stack.append(graph[start][i])

    while stack:
        node = stack.pop()
        if node == start:
            lst.append(start)
            return
        for j in graph[node]:
            if visited[j] == 0:
                visited[j] = 1
                stack.append(j)


N = int(sys.stdin.readline())
graph = [[] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    a = int(sys.stdin.readline())
    graph[a].append(i)

lst=[]
for j in range(1, N+1):
    dfs(j)
print(len(lst))
for k in lst:
    print(k)