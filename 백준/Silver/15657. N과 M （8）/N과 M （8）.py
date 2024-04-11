import sys

def dfs(lv, start):

    if lv == M:
        print(" ".join(map(str, check)))
        return

    for i in range(start, N):
            check.append(lst[i])
            dfs(lv + 1, i)
            check.pop()

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
check = []
visited = [0]*(N)
dfs(0, 0)