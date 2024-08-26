import sys


def solution(start, count):

    visited[start] = 1

    for i in graph[start]:
        if visited[i] == 0:
            count = solution(i, count + 1)
    
    return count

    
T = int(sys.stdin.readline().strip())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [0] * (N+1)
    
    ans = solution(1, 0)
    
    print(ans)
