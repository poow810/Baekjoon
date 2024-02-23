def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < M

def solution():

    max_num = 0
    for i in range(N):
        for j in range(M):
            w = mp[i][j]
            add = w
            for z in range(1, w+1):
                for k in range(4):
                    nx = i + z*dx[k]
                    ny = j + z*dy[k]

                    if not is_valid(nx, ny):
                        continue

                    add += mp[nx][ny]

            if add > max_num:
                max_num = add

    return max_num         
                    

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    mp = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    ans = solution()

    print(f"#{t+1}", ans)