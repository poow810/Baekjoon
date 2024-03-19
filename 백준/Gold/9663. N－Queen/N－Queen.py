def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N
 
def check(x, y, mp):    
 
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
 
        while is_valid(nx, ny):
            if mp[nx][ny] == 1:
                return False
            nx += dx[i]
            ny += dy[i]
    return True
 
def dfs(lv, v):
    global count
 
    if lv == N:
        count += 1
        return
 
    for i in range(N):
        if v[i] == 0 and check(lv, i, mp) == True:
            mp[lv][i] = 1
            v[i] = 1
            dfs(lv + 1, v)
            v[i] = 0
            mp[lv][i] = 0
 
 
N = int(input())
count = 0
mp = [[0]*N for _ in range(N)]
visited = [0]*N
dx = [-1, -1]
dy = [-1, 1]
dfs(0, visited)
print(count)