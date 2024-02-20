import sys
sys.setrecursionlimit(10000)

def dfs():

    if len(result) == M:
        print(" ".join(map(str, result)))
        return 
    
    for i in range(1, N+1):
        result.append(i)
        dfs()
        result.pop()

N, M = map(int, sys.stdin.readline().split())
result = []
dfs()