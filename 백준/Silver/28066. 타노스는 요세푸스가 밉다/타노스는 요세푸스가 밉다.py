import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

lst = [x for x in range(N)]
queue = deque(lst)

while len(queue) > 1:
    queue.append(queue.popleft())
    if len(queue) < K:
        for _ in range(len(queue)-1):
            queue.popleft()
    else:
        for _ in range(K-1):
            queue.popleft()

print(queue.popleft() + 1)