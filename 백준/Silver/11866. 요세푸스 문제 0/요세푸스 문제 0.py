import sys
from collections import deque

def solution(N, K):
    
    queue = deque(range(1, N+1))
    result = []
    
    while len(queue) > 1:
        for _ in range(K-1):
            queue.append(queue.popleft())
        
        result.append(queue.popleft())
    result.append(queue.popleft())
    return result

N, K = map(int, sys.stdin.readline().split())
result = solution(N, K)
print("<", end="")
for i in result:
    if i == result[-1]:
        print(f"{i}", end="")
    else:
        print(f"{i}", end=", ")
        
print(">")