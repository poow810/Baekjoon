# import sys
# sys.stdin = open('input.txt')

for _ in range(10):
    t = int(input())
    mp = [list(map(int, input().split())) for _ in range(100)]


    dx = [-1, 0, 0] 
    dy = [0, -1, 1]
    visited = [[0]*100 for _ in range(100)]

    def is_valid(nx, ny):
        return 0 <= nx < 100 and 0 <= ny < 100
    
    for i in range(100):
        for j in range(100):
            if mp[i][j] == 2:
                x, y = i, j

  
    # 인덱싱
    # idx = []
    # for i in range(len(mp[0])):
    #     if mp[0][i] == 1:
    #         idx.append(i)
    while True:
            for i in range(3):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if not is_valid(nx, ny):
                    continue                

                if visited[nx][ny] == 1:
                    continue

                if mp[nx][ny] == 0:
                    continue
    
                if mp[nx][ny] == 1:
                    x, y = nx, ny
                    visited[x][y] = 1

            if x == 0:
                break

    print(f"#{t}", y)