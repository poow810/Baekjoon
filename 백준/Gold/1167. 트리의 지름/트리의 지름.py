"""
백준 1167번
트리의 지름
임의의 두 점이 가장 멀면 됨.
"""
import sys
from collections import deque

def bfs(graph, start):
    queue = deque()
    visited = [-1] * (V+1)
    queue.append(start)
    max = [0, 0]

    visited[start] = 0
    while queue:
        current = queue.popleft()
        for child, length in graph[current]:
            if visited[child] == -1:
                visited[child] = visited[current] + length
                queue.append(child)

                if max[0] < visited[child]:
                    max = visited[child], child
    return max

if __name__ == '__main__':
    V = int(sys.stdin.readline())
    graph = [[] for _ in range(V+1)]

    for _ in range(V):
        c = list(map(int, sys.stdin.readline().split()))
        for i in range(1, len(c)-2, 2):
            idx = c[0]
            node = c[i]
            link = c[i+1]
            graph[idx].append((node, link))

    dis, node = bfs(graph, 1)
    print(bfs(graph, node)[0])

