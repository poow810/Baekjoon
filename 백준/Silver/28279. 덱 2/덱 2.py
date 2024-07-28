import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
for _ in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    if lst[0] == 1:
        queue.appendleft(lst[1])
    elif lst[0] == 2:
        queue.append(lst[1])
    elif lst[0] == 3:
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif lst[0] == 4:
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif lst[0] == 5:
        print(len(queue))
    elif lst[0] == 6:
        if queue:
            print(0)
        else:
            print(1)
    elif lst[0] == 7:
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif lst[0] == 8:
        if queue:
            print(queue[-1])
        else:
            print(-1)