def dfs(start, end):

    stack = [start]
    visited[start] = 1

    while stack:
        cur = stack.pop()

        if visited[cur] == 0:
            visited[cur] = 1

        for i in mp[cur]:
            if visited[i] == 0:
                stack.append(i)
        
        if end == cur:
            return 1
    return 0


for t in range(10):
    N, M = map(int, input().split())
    lst = list(map(int, input().split())) # V : 노드 개수 E : 간선 개수
    mp = [[] for _ in range(101)]
    visited = [0] * (101)
    for i in range(M):
        a, b = lst[i*2], lst[i*2+1]
        mp[a].append(b)
    print(f"#{t+1}", dfs(0, 99))