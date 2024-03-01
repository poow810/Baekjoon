def dfs(x, y, add, c, sq):
    global max_num
    
    if add > C:
        return

    if c == M:
        if max_num < sq:
            max_num = sq
        return

    # M개 중 C를 넘지 않는 연속된 칸 찾기
    dfs(x, y, add + mp[x][y+c], c+1, sq + mp[x][y+c]**2)
    dfs(x, y, add, c+1, sq)


T = int(input())
for t in range(T):
    N, M, C = map(int, input().split())
    mp = [list(map(int, input().split())) for _ in range(N)]
    
    ans = 0
    for i in range(N):
        for j in range(N-M+1):
            max_num = 0
            dfs(i, j, 0, 0, 0)
            s1 = max_num
            for k in range(i, N):
                start_x = 0
                if i == k:
                    start_x = j + M
                for z in range(start_x, N-M+1):
                    max_num = 0
                    dfs(k, z, 0, 0, 0)
                    s2 = max_num
                    ans = max(ans, s1 + max_num)
                    
    print(f"#{t+1}", ans)
    