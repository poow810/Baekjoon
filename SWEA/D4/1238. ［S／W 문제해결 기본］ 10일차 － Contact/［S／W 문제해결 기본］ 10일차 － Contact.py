from collections import deque

def bfs(start):

    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        current = queue.popleft()

        for i in mp[current]:
            if visited[i] == 0:
                visited[i] = 1 + visited[current]
                queue.append(i)


for t in range(10):
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))
    V = max(arr)
    visited = [0] * (V+1)
    mp = [[] for _ in range(V+1)]
    for i in range(N):
        if i % 2 != 0:
            mp[arr[i-1]].append(arr[i])
    
    bfs(start)
    max_num = max(visited)
    lst = []
    for k in range(len(visited)):
        if visited[k] == max_num:
            lst.append(k)

    print(f"#{t+1}", max(lst))