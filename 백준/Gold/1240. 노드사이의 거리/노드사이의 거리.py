import sys


def solution(start, end):

    stack = []
    visited = [0] * (N+1)
    stack.append((start, 0))

    while stack:
        current, distance = stack.pop()
        
        if current == end:
            return distance

        if visited[current] == 0:
            visited[current] = 1
            for next, weight in graph[current]:
                stack.append((next, weight + distance))


N, M = map(int, sys.stdin.readline().split())

graph = [[] * (N+1) for _ in range(N+1)]

for _ in range(N-1):
    a, b, w = map(int, sys.stdin.readline().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(solution(a, b))