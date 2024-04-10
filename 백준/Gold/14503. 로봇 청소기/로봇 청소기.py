import sys


def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < M


def solution(x, y, d):
    global count 

    while True:
        if mp[x][y] == 0:
            count += 1
            mp[x][y] = 2

        flag = True
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]

            if not is_valid(nx, ny):
                continue
            
            if mp[nx][ny] == 0:
                flag = False
                d = (3+d)%4
                if mp[x+dx[d]][y+dy[d]] == 0:
                    x = x+dx[d]
                    y = y+dy[d]
                    break
        
        if flag: # 청소 x 빈칸 없는 경우
            if mp[x+dx[(d+2)%4]][y+dy[(d+2)%4]] != 1:
                x = x + dx[(d+2)%4]
                y = y + dy[(d+2)%4]
            
            else:
                return


N, M = map(int, sys.stdin.readline().split())
x, y, d = map(int, sys.stdin.readline().split())
mp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0
solution(x, y, d)
print(count)