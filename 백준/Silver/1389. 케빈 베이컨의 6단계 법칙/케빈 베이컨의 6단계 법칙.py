import sys
from collections import deque

def solution(start):

    queue = deque()
    queue.append(start)
    visited = [0]*(N+1)
    visited[start] = 1

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = visited[node] + 1
                queue.append(i)
    
    count = 0
    for j in range(1, N+1):
        count = count + visited[j] - 1

    return count

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

lst = []
for i in range(1, N+1):
    lst.append(solution(i))

check = min(lst)
for i in range(N):
    if lst[i] == check:
        print(i+1)
        break
