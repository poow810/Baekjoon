import sys
from collections import deque

T = int(sys.stdin.readline())
for t in range(T):
    N, M = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    queue = deque()
    for i in range(N):
        queue.append((i, lst[i]))
    count = 0
    while queue:
        
        a = queue[0][1]
        flag = True
    
        for j in range(len(queue)):
            if a < queue[j][1]:
                flag = False
        
        if not flag:
            queue.append(queue.popleft())
        
        else:
            count += 1
            idx, imp = queue.popleft()
            if idx == M:
                break

    print(count)