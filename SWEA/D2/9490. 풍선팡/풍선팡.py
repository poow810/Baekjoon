T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    mp = [list(map(int, input().split())) for _ in range(N)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def is_valid(nx, ny):
        return 0 <= nx < N and 0 <= ny < M

    def solution(x, y):
        
        lst = []
        for i in range(N):
            for j in range(M):
                add = mp[i][j]
                for z in range(1, mp[i][j] + 1):
                    for k in range(4):
                        nx = i + z * dx[k]
                        ny = j + z * dy[k]

                        if not is_valid(nx, ny):
                            continue
                
                        add += mp[nx][ny]
                lst.append(add)
                
        return lst
    
    lst = solution(0, 0)
    max_num = 0
    for i in lst:
        if i >= max_num:
            max_num = i

    print(f"#{t+1}", max_num)