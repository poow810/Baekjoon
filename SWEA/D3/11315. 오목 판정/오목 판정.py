T = int(input())
for t in range(T):
    N = int(input())
    mp = [list(input()) for _ in range(N)]
    dx = [0, 1, 1, 1]
    dy = [1, 1, 0, -1]


    def is_valid(nx, ny):
        return 0 <= nx < N and 0 <= ny < N

    def solution(mp, N, dx, dy):

        for i in range(N):
            for j in range(N):
                if mp[i][j] == 'o':
                    for k in range(4):
                        count = 1

                        nx = i + dx[k]
                        ny = j + dy[k]

                        if not is_valid(nx, ny):
                            continue
                        
                        while mp[nx][ny] == 'o':
                            count += 1
                            if count == 5:
                                return "YES"
                            nx += dx[k]
                            ny += dy[k]
                            if not is_valid(nx, ny):
                                break
        return "NO"

    print(f"#{t+1}", solution(mp, N, dx, dy))

