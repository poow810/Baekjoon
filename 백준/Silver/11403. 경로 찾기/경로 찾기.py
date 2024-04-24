import sys

def solution(start):

    stack = []
    stack.append(start)
    visited = [0] * N

    while stack:
        node = stack.pop()
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = 1
                stack.append(i)
    return visited


N = int(sys.stdin.readline().strip())
graph = [[]*N for _ in range(N)]
for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    for j in range(len(lst)):
        if lst[j] == 1:
            graph[i].append(j)
ans = []
for i in range(N):
    v = solution(i)
    ans.append(v)
for z in ans:
    print(*z)