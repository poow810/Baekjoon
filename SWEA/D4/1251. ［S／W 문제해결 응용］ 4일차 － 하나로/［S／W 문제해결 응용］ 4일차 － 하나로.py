from heapq import heappush, heappop


def prim(start):

    pq = []
    heappush(pq, (0, start)) 
    sum_dist = 0

    while pq:
        dist, node = heappop(pq)

        if visited[node] == 1:
            continue

        visited[node] = 1
        sum_dist += dist

        for i in range(N):
            if graph[node][i] == 0 or visited[i] == 1:
                continue

            heappush(pq, (graph[node][i], i))
    
    return sum_dist
    

T = int(input())
for t in range(T):
    N = int(input())
    lst_x = list(map(int, input().split()))
    lst_y = list(map(int, input().split()))
    envi = float(input())
    graph = [[0] * N for _ in range(N)]
    visited = [0] * N

    for i in range(N):
        for j in range(N):
            graph[i][j] = (lst_x[i] - lst_x[j])**2 + (lst_y[i] - lst_y[j])**2
            graph[j][i] = (lst_x[i] - lst_x[j])**2 + (lst_y[i] - lst_y[j])**2
    
    total = prim(0)
    ans = envi*(total)
    print(f"#{t+1}", round(ans))