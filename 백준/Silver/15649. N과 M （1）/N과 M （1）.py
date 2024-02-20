import sys

def dfs():

    if len(result) == M:
        print(" ".join(map(str, result)))

    for i in range(1, N+1):
        if visited[i] == 1:
            continue
        visited[i] = 1
        result.append(i)
        dfs()
        result.pop()
        visited[i] = 0

N, M = map(int, sys.stdin.readline().split())
lst = [x for x in range(1, N+1)]
visited = [0] * (N+1)
result = []
dfs()