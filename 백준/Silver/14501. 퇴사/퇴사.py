import sys

def dfs(start, count):
    
    if start == N:
        result.append(count)
        return
    
    if start + lst[start][0] <= N:
        dfs(start + lst[start][0], count+lst[start][1])
    dfs(start+1, count)

N = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = []

dfs(0, 0)


print(max(result))