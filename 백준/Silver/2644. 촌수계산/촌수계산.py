import sys


def dfs(start, end):

    stack = [start]
    visited[start] = 0

    while stack:
        cur = stack.pop()

        if cur == end:
            return visited[cur]

        for i in node[cur]:
            if visited[i] == 0:
                visited[i] = visited[cur] + 1
                stack.append(i)
    return -1


N = int(sys.stdin.readline())
start, end = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
visited = [0]*(N+1)
node = [[] for _ in range(N+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    node[a].append(b)
    node[b].append(a)

print(dfs(start, end))
