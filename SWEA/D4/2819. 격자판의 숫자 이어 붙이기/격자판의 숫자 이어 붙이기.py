def is_valid(nx, ny):
    return 0 <= nx < 4 and 0 <= ny < 4


def dfs(lv, x, y, string):

    if lv == 6:
        check.add(string)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not is_valid(nx, ny):
            continue

        dfs(lv + 1, nx, ny, string+mp[nx][ny])


T = int(input())
for t in range(T):
    mp = [list(map(str, input().split())) for _ in range(4)]
    check = set()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        for j in range(4):
            dfs(0, i, j, mp[i][j])

    print(f"#{t+1}", len(check))