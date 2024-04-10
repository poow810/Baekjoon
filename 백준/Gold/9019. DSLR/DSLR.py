import sys
from collections import deque

def left(n):
    
    l = n//1000 + (n % 1000) * 10
    return l


def right(n):
    
    r = n//10 + (n % 10) * 1000
    return r


def bfs(n, end):
    
    queue = deque()
    queue.append((n, ""))
    visited[n] = 1

    while queue:
        n, string = queue.popleft()
        
        if n == end:
            print(string)
            return

        for i in range(4):
            if i == 0 :  # D
                d = (n * 2) % 10000
                if visited[d] == 0:
                    visited[d] = 1
                    queue.append((d, string+'D'))
            
            elif i == 1:
                s = (n - 1) % 10000
                if visited[s] == 0:
                    visited[s] = 1
                    queue.append((s, string+'S'))
            
            elif i == 2:
                l = left(n)
                if visited[l] == 0:
                    visited[l] = 1
                    queue.append((l, string+'L'))
            
            else:
                r = right(n)
                if visited[r] == 0:
                    visited[r] = 1
                    queue.append((r, string+'R'))


T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    visited = [0] * 10001
    bfs(a, b)
