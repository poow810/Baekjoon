import sys
sys.setrecursionlimit(150000)

def dfs1(start):
 
    for i in mp[start]:
        if visited[i] == -1:
            visited[i] = visited[start] + 1
            dfs1(i)


N, M, R = map(int, sys.stdin.readline().split())
mp = [[] for _ in range(N+1)]
visited =[-1] * (N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    mp[a].append(b)
    mp[b].append(a)

for j in mp:
    j.sort(reverse=True)

visited[R] = 0
dfs1(R)
for i in visited[1:]:
    print(i)