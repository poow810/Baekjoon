from collections import deque

def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

def bfs():

    ans = []
    queue = deque()
    for i in range(N):
        for j in range(N):
            count = 1
            if is_valid(i-1, j) and mp[i-1][j] == mp[i][j]+1 or is_valid(i+1, j) and mp[i+1][j] == mp[i][j]+1 or is_valid(i, j-1) and mp[i][j-1] == mp[i][j]+1 or is_valid(i, j+1) and mp[i][j+1] == mp[i][j]+1:
                queue.append((i, j))

                while queue:
                    x, y = queue.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if not is_valid(nx, ny):
                            continue

                        if mp[x][y]+1 == mp[nx][ny]:
                            queue.append((nx, ny))
                            count += 1
                ans.append((mp[i][j], count))
                                        
    return ans


T = int(input())
for t in range(T):
    N = int(input())
    mp = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    result = bfs()
    result.sort()
    max_count = 0
    for i in result:
        if max_count < i[1]:
            max_count = i[1]
    for j in result:
        if j[1] == max_count:
            print(f"#{t+1}", j[0], j[1])
            break
    