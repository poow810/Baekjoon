import sys


def dfs(start, n, m):
    if len(num) == m:
        print(' '.join(map(str, num)))
        return

    for j in range(start, n+1):
        num.append(j)
        dfs(j, n, m)
        num.pop()


N, M = list(map(int, sys.stdin.readline().split()))
num = []
dfs(1, N, M)
