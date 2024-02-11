def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

def ocelo(x, y, color): 

    if mp[x][y] != 0: # 이미 돌이 놓였을 때, 종료
        return 

    if color == 1:
        for i in range(8):
            stack = []
            nx = dx[i] + x
            ny = dy[i] + y
            
            while is_valid(nx, ny) and mp[nx][ny] == 2:
                stack.append((nx, ny))
                nx += dx[i]
                ny += dy[i]

            if not is_valid(nx, ny):
                continue

            if mp[nx][ny] == 1:
                for a, b in stack:
                    mp[a][b] = color
                mp[x][y] = color
    
    elif color == 2:
        for i in range(8):
            stack = []
            nx = dx[i] + x
            ny = dy[i] + y

            while is_valid(nx, ny) and mp[nx][ny] == 1:
                stack.append((nx, ny))
                nx += dx[i]
                ny += dy[i]

            if not is_valid(nx, ny):
                continue

            if mp[nx][ny] == 2:
                for a, b in stack:
                    mp[a][b] = color
                mp[x][y] = color
                


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    mp = [[0] * N for _ in range(N)]
    mp[N//2][N//2], mp[N//2-1][N//2-1] = 2, 2
    mp[N//2-1][N//2], mp[N//2][N//2-1] = 1, 1
    dx = [-1, -1, -1, 0, 1, 1, 1, 0] # 왼쪽 위부터 시계 방향
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]

    count_b = 0
    count_w = 0

    for _ in range(M):
        a, b, color = map(int, input().split())
        ocelo(b-1, a-1, color)
        # if mp[x][y] == 0:
    for i in mp:
        for j in i:
            if 1 == j:
                count_b += 1
            elif 2 == j:
                count_w += 1

    print(f"#{t+1}", count_b, count_w)    