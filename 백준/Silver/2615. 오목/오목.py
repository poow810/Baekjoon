import sys

def is_valid(nx, ny):
    return 0 <= nx < 19 and 0 <= ny < 19

mp = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]

dx = [0, 1, 1, -1]  # → ↓ ↘ ↗
dy = [1, 0, 1, 1]

answer = []
winner = 0

for i in range(19):
    for j in range(19):
        if mp[i][j] != 0:  # 바둑돌이 있는 경우만 탐색
            stone = mp[i][j]  # 현재 돌의 색깔 (1: 흑돌, 2: 백돌)

            for k in range(4):  # 4가지 방향 탐색
                count = 1
                temp = [(i, j)]

                nx, ny = i + dx[k], j + dy[k]

                while is_valid(nx, ny) and mp[nx][ny] == stone:
                    temp.append((nx, ny))
                    count += 1
                    nx += dx[k]
                    ny += dy[k]

                # 정확히 5개인지 검증 (6목이면 승리 X)
                prev_x, prev_y = i - dx[k], j - dy[k]  # 반대 방향 돌 확인
                if count == 5 and not (is_valid(prev_x, prev_y) and mp[prev_x][prev_y] == stone):
                    winner = stone
                    answer = temp
                    break  # 승자가 나오면 더 이상 검사할 필요 없음

if winner:
    print(winner)
    answer.sort(key=lambda x: (x[1], x[0]))  # y 우선 정렬
    print(answer[0][0] + 1, answer[0][1] + 1)
else:
    print(0)
