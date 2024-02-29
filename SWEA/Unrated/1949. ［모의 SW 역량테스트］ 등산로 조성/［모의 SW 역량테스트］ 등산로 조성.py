def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N


def dfs(x, y, count, dig):
    global c
    
    if not is_valid(x, y):
        return
    
    visited[x][y] = 1
    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]

        if not is_valid(nx, ny):
            continue
        if visited[nx][ny] == 1:
            continue

        if mp[nx][ny] < mp[x][y]:
            if dig == 0:
                visited[nx][ny] = 1
                dfs(nx, ny, count + 1, 0)
                visited[nx][ny] = 0
            else:
                visited[nx][ny] = 1
                dfs(nx, ny, count + 1, 1)
                visited[nx][ny] = 0

        elif mp[nx][ny] >= mp[x][y] and dig == 0:
            if K >= (mp[nx][ny] - (mp[x][y]-1)):
                visited[nx][ny] = 1
                minus = mp[nx][ny] - (mp[x][y]-1)
                mp[nx][ny] -= minus
                dfs(nx, ny, count + 1, 1)
                mp[nx][ny] += minus
                visited[nx][ny] = 0
            else:
                if c < count:
                    c = count
                
        else:
            if c < count:
                c = count
                


T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    mp = [list(map(int, input().split())) for _ in range(N)]
    lst = []
    max_num = 0
    max_idx = 0
    for z in mp:
        for k in z:
            if k > max_idx:
                max_idx = k
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    c = 0

    for i in range(N):
        for j in range(N):
            visited = [[0]*N for _ in range(N)]
            if mp[i][j] == max_idx:
                dfs(i, j, 1, 0)
    if c > max_num:
        max_num = c    
    print(f"#{t+1}", max_num)