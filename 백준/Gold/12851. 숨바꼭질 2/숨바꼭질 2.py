import sys
from collections import deque

def bfs(start):
    global count, max_time

    queue = deque()
    queue.append((start, 0))
    visited[start] = 0

    while queue:
        current, time = queue.popleft()

        if time > max_time:
            continue

        if current == K:
            if max_time > time:
                max_time = time
                count = 1

            elif max_time == time:
                count += 1
            continue

        for next_pos in (current+1, current-1, current*2):
            if 0 <= next_pos <= 100000 and visited[next_pos] >= time + 1:
                visited[next_pos] = time + 1
                queue.append((next_pos, time + 1))

N, K = map(int, sys.stdin.readline().split())
max_time = 1e99
count = 0
visited = [1e99] * 100001
bfs(N)

print(max_time)
print(count)