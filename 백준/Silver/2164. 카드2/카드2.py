import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
for i in range(1, N+1):
    queue.append(i)

while queue:
    if len(queue) == 1:
        ans = queue.popleft()
        break

    queue.popleft() # 맨 위 버리기
    queue.append(queue.popleft()) # 그 다음 맨 위 뽑아서 다시 넣기

print(ans)
