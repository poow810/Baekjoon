import sys

def dfs(lv):

    if lv == M:
        print(" ".join(map(str, check)))
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            check.append(lst[i])
            dfs(lv + 1)
            check.pop()
            visited[i] = 0

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
check = []
visited = [0]*(N)
dfs(0)