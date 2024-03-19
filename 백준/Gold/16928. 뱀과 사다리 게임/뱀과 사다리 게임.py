import sys
from collections import deque

def is_valid(npos):
    return npos <= 100


def bfs(start, end, ladder_snake):
    global min_dice

    queue = deque()
    count = 0
    queue.append((start, count))

    while True:
        if queue:
            pos, count = queue.popleft()

        if pos == end:
            min_dice = min(min_dice, count)
            return
        
        for i in range(1, 7):
            npos = pos + i
            
            if not is_valid(npos):
                continue
            
            for j in ladder_snake:
                    if npos == j[0]:
                        if visited[npos] == 0:
                            queue.append((j[1], count + 1))
                            visited[npos] = 1
                            break
            else:
                if visited[npos] == 0:
                    visited[npos] = 1
                    queue.append((npos, count + 1))


N, M = map(int, sys.stdin.readline().split())
ladder_snake = []

for _ in range(N+M):
    a, b = map(int, sys.stdin.readline().split())
    ladder_snake.append((a, b))

visited = [0] * 101


start = 1
end = 100
min_dice = 1e99
bfs(start, end, ladder_snake)
print(min_dice)