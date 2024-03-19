def dfs(lv, res):
    global max_per

    if lv == N:
        if max_per < res*100:
            max_per = res*100
        return

    if res*100 <= max_per:
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(lv + 1, res*mp[lv][i]*10**(-2))
            visited[i] = 0


T = int(input())
for t in range(T):
    N = int(input())
    mp = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_per = 0
    dfs(0, 1)
    print(f"#{t+1}", f"{max_per:.6f}")