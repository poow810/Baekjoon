def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

def dfs(lv, add, mp, core):
    global result

    if core > result[0]:
        result[0] = core
        result[1] = add
    elif core == result[0]:
        if result[1] > add:
            result[1] = add

    if lv == count:
        return
    
    x, y = lst[lv][0], lst[lv][1]
    for j in range(4):
        stack = []
        flag = True
        c = 0
        nx = x + dx[j]
        ny = y + dy[j]
        if mp[nx][ny] == 2:
            continue
        if mp[nx][ny] == 3:
            continue
        if mp[nx][ny] == 1:
            continue

        while is_valid(nx, ny) and mp[nx][ny] == 0 and mp[nx][ny] == 0:
            stack.append((nx, ny))
            mp[nx][ny] = 3
            c += 1
            nx += dx[j]
            ny += dy[j]
            if is_valid(nx, ny) and mp[nx][ny] == 3:
                flag = False
            if is_valid(nx, ny) and mp[nx][ny] == 1:
                flag = False
            if is_valid(nx, ny) and mp[nx][ny] == 2:
                flag = False
        
        if not flag:
            for i in stack:
                a, b = i
                mp[a][b] = 0
            continue

        dfs(lv+1, add + c, mp, core+1)
        
        for i in stack:
            a, b = i
            mp[a][b] = 0
    dfs(lv+1, add, mp, core)


T = int(input())
for t in range(T):
    N = int(input())
    mp = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if mp[i][j] == 1:
                count += 1
            if i == 0 and mp[i][j] == 1:
                mp[i][j] = 2
                count -= 1
            if j == 0 and mp[i][j] == 1:
                mp[i][j] = 2
                count -= 1
            if i == N-1 and mp[i][j] == 1:
                mp[i][j] = 2
                count -= 1
            if j == N-1 and mp[i][j] == 1:
                mp[i][j] = 2
                count -= 1
    result = [0, 0]
    lst = []
    for k in range(N):
        for z in range(N):
            if mp[k][z] == 1:
                lst.append((k, z))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dfs(0, 0, mp, 0)
    print(f"#{t+1}", result[1])