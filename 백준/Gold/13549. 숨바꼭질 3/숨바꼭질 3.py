import sys
from collections import deque

def bfs(start, end):

    dp = [-1] * 100001
    queue = deque()
    queue.append(start)
    dp[start] = 0
    
    while queue:
        node = queue.popleft()

        if node == end:
            return dp[node]

        if 0 < node*2 < 100001 and dp[node*2] == -1:
            dp[node*2] = dp[node]
            queue.appendleft(node*2)
   
        if 0 <= node - 1 < 100001 and dp[node-1] == -1:
            dp[node-1] = dp[node] + 1
            queue.append(node-1)

        if 0 <= node+1 < 100001 and dp[node+1] == -1:
            dp[node+1] = dp[node] + 1
            queue.append(node+1)



N, K = map(int, sys.stdin.readline().split())
print(bfs(N, K))