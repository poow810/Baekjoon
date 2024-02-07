T = int(input())
for t in range(T):

    N, M = map(int, input().split())
    mp = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def is_valid(nx, ny):
        return 0 <= nx < N and 0 <= ny < M


    max_count = []
    for i in range(N):
        for j in range(M):
            if mp[i][j] == 1:
                for k in range(4):
                    count = 1
                    nx = i + dx[k]
                    ny = j + dy[k]

                    while is_valid(nx, ny) and mp[nx][ny] == 1:
                        count += 1
                        nx += dx[k]
                        ny += dy[k]
                    
                    max_count.append(count)

    max_num = 0
    for i in max_count:
        if max_num < i:
            max_num = i

    print(f"#{t+1}", max_num)