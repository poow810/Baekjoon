def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

def solution(x, y):

    mp[x][y] = 1
    idx = 0
    value = 1
    while value < N**2:
        nx = x + dx[idx%4]
        ny = y + dy[idx%4]

        if not is_valid(nx, ny) or mp[nx][ny] != 0:
            idx += 1
            mp[x][y] = value
            
        else:
            value += 1
            mp[nx][ny] = value
            x = nx
            y = ny
        

T = int(input())
for t in range(T):
    N = int(input())
    mp = [[0]*N for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    solution(0, 0)
    print(f"#{t+1}")
    for i in mp:
        print(" ".join(map(str, i)))