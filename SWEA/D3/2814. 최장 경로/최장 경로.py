def dfs(start, count):
    global max_count

    max_count = max(max_count, count)
    visited[start] = 1

    for i in node[start]:
        if visited[i] == 0:
            dfs(i, count+1)
            visited[i] = 0


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    node = [[] for _ in range(N+1)]
    max_count = 0

    for i in range(M):
        a, b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)


    for j in range(N+1):
        if j == 0:
            continue
        visited = [0] * (N + 1)
        dfs(j, 0)

    print(f"#{t+1}", max_count+1)