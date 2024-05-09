import sys
from collections import deque

def bfs(num, check):
    
    queue = deque()
    count = 1
    queue.append((num, count))

    while queue:
        num, count = queue.popleft()
        if num > check:
            continue
        if num == check:
            return count
        
        for i in range(2):
            if i == 0:
                queue.append(((int(str(num) +'1')), count + 1))
            elif i == 1:
                queue.append(((num * 2), count + 1))

    return -1    
    

A, B = map(int, sys.stdin.readline().split())
print(bfs(A, B))