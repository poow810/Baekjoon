import sys
from collections import deque

def bfs(start):

    queue = deque()
    queue.append(start)
    mp[start] = 1

    while queue:
        node = queue.popleft()

        if node == K:
            return
        
        for i in range(3):
            if i == 0:
                next = node - 1
            elif i == 1:
                next = node + 1
            else:
                next = node * 2
            
            if 0 <= next <= 100000:
                if mp[next] == 0:
                    mp[next] = mp[node] + 1
                    queue.append(next)

         

N, K = map(int, sys.stdin.readline().split())

mp = [0] * (100001)
bfs(N)
print(mp[K]-1)