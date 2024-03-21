from heapq import heappush, heappop


def solution(start, graph, X):

    hq = []
    visited = [int(1e99)] * (N + 1)
    heappush(hq, (0, start))
    visited[start] = 0

    while hq:
        count, cur = heappop(hq)

        if visited[cur] < count:
            continue

        for i in graph[cur]:
            next_count = i[0]
            next_node = i[1]

            new_count = next_count + count
            
            if new_count >= visited[next_node]:
                continue

            visited[next_node] = new_count
    
            heappush(hq, (new_count, next_node))
            
    return visited[X]
    

T = int(input())
for t in range(T):
    N, M, X = map(int, input().split())
    graph1 = [[] * (N+1) for _ in range(N+1)]
    graph2 = [[] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph1[a].append([c, b])

    go = []
    back = []
    for i in range(1, N+1):
        if i == X:
            continue
        go.append(solution(i, graph1, X))
    for j in range(1, N+1):
        if j == X:
            continue
        back.append(solution(X, graph1, j))
    
    ans = []
    for k in range(len(go)):
        ans.append((go[k] + back[k]))
    print(f"#{t+1}", max(ans))