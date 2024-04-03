from collections import deque

def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N


def bfs(x, y):

    queue = deque()
    queue.append((x, y))
    count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not is_valid(nx, ny):
                continue
            
            if mp[nx][ny] == mp[x][y] + 1:
                count += 1
                queue.append((nx, ny))
    return count
            

T = int(input())
for t in range(T):
    N = int(input())
    mp = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    lst = [0, 0]
    max_check = 0
    for i in range(N):
        for j in range(N):
            count = bfs(i, j)
            if count > lst[1]:
                lst[1] = count
                lst[0] = mp[i][j]
            elif count == lst[1]:
                if mp[i][j] < lst[0]:
                    lst[0] = mp[i][j]
    
    print(f"#{t+1}", lst[0], lst[1])