import sys

def dfs(start):
    global num
    if len(num) == M:
        print(' '.join(map(str, num)))
        return

    for j in range(start, N+1):
        if j not in num:
            num.append(j)
            dfs(j+1)
            num.pop()


N, M = list(map(int, sys.stdin.readline().split()))
num = []
dfs(1)
