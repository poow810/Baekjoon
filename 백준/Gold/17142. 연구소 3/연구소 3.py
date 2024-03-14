# 가장 처임에 모든 바이러스는 비활성 상태이고,
# 활성 상태인 바이러슨 상하좌우 인접한 모든 빈칸으로 동시
# 복제되며, 1초가 걸린다. 연구소의 바이러스 m개를 활성 상태로
# 연구소는 빈 칸, 벽, 바이러스로 이루어져 있으며,
# 벽은 한 칸을 가득 차지한다. 활성 바이러스가 비활성 바이러스
# 가 있는 칸으로 가면 비활성 바이러스는 활성 바이러스

from collections import deque
from itertools import combinations

dirt_y = [-1, 1, 0, 0]
dirt_x = [0, 0, -1, 1]

min_time = 21e8

n, m = map(int, input().split())
my_map = [list(map(int, input().split())) for _ in range(n)]


def bfs():
    global my_flag
    while my_q:
        now_y, now_x, now_time = my_q.popleft()
        # if now_time-1 >= min_time:
        #     my_flag = 1
        #     return

        for i in range(4):
            new_y = now_y + dirt_y[i]
            new_x = now_x + dirt_x[i]
            new_time = now_time + 1
            if new_y > n - 1 or new_y < 0 or new_x > n - 1 or new_x < 0:
                continue
            if my_new_map[new_y][new_x] == -1:
                continue
            if visited[new_y][new_x] == 1:
                continue
            if my_new_map[new_y][new_x] != 0 and my_new_map[new_y][new_x] != -2:
                my_new_map[new_y][new_x] = min(my_new_map[new_y][new_x], new_time)
                continue
            visited[new_y][new_x] =1
            my_new_map[new_y][new_x] = new_time
            my_q.append([new_y, new_x, new_time])


virus_coords = []
for i in range(n):
    for j in range(n):
        if my_map[i][j] == 2:
            virus_coords.append([i, j])

my_comb_virus = list(combinations(virus_coords, m))

for my_virus in my_comb_virus:
    my_flag = 0
    my_q = deque()
    my_new_map = [[0 for _ in range(n)] for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if my_map[i][j] == 2 and [i, j] not in my_virus:
                my_new_map[i][j] = -2
            if my_map[i][j] == 1:
                my_new_map[i][j] = -1
    for j in my_virus:
        my_q.append([j[0], j[1], 1])
        my_new_map[j[0]][j[1]] = 1
        visited[j[0]][j[1]] = 1
    bfs()

    if my_flag == 1:
        continue
    else:
        my_new_flag = 0
        my_max = 0
        for i in range(n):
            for j in range(n):
                if my_new_map[i][j] == 0:
                    my_new_flag = 1
                    break
                if my_new_map[i][j] - 1 > my_max and my_map[i][j] != 2:
                    my_max = my_new_map[i][j] - 1
            if my_new_flag == 1:
                break
        if not my_new_flag:
            min_time = min(my_max, min_time)

if min_time == 21e8:
    print(-1)
else:
    print(min_time)