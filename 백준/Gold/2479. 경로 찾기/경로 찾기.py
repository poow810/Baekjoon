import sys
from collections import deque

def bfs(start, end):

    ans = str(start)
    queue = deque()
    queue.append((start, ans))
    visited[start] = 1

    while queue:
        cur, ans = queue.popleft()
        if cur == end:
            return ans

        for i in range(1, len(lst)):
            count = 0

            if visited[i] == 0:
                for j in range(K):
                    if lst[cur][j] != lst[i][j]:
                        count += 1
                    if count > 1:
                        break
                
                if count == 1:
                    visited[i] = 1
                    queue.append((i, ans+' '+str(i)))
    return -1


N, K = map(int, sys.stdin.readline().split())
lst = [""] + [str(sys.stdin.readline().rstrip()) for _ in range(N)]
# for i in range(N):
#     count = 0
#     a = sys.stdin.readline()
#     for j in a:
#         if j == '1':
#             count += 1
#     lst.append(count)
start, end = map(int, sys.stdin.readline().split())
visited = [0] * (N+1)
res = bfs(start, end)
if res == -1:
    print(-1)
else:
    print(res)