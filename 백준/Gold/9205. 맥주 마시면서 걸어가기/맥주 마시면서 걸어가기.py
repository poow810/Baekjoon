import sys
from collections import deque


def bfs(lst):

    queue = deque()
    queue.append((start_x, start_y))

    while queue:
        x, y = queue.popleft()

        if abs(x - end_x) + abs(y - end_y) <= 1000:
            return "happy"

        for i in range(n):
            if visited[i] == 1:
                continue
            next_x, next_y = lst[i]

            if abs(x - next_x) + abs(y - next_y) <= 1000:
                queue.append((next_x, next_y))
                visited[i] = 1

    return "sad"

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())

    start_x, start_y = map(int, sys.stdin.readline().split())
    lst = []
    for i in range(n):
        x, y = map(int, sys.stdin.readline().split())
        lst.append((x, y))

    end_x, end_y = map(int, sys.stdin.readline().split())
    visited = [0] * (n+1)
    print(bfs(lst))

