from collections import deque, Counter

map = []


def bfs(s, i, j):
    global map
    m = len(s)
    n = len(s[0])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque([(i, j)])

    flag = False

    visit = [[False] * n for _ in range(m)]

    while q:
        x, y = q.popleft()
        visit[x][y] = True

        if map[x][y] == True:
            return True

        for nx, ny in zip(dx, dy):
            if nx + x >= m or nx + x < 0:
                flag = True
                break
            elif ny + y >= n or ny + y < 0:
                flag = True
                break
            else:
                if s[nx + x][ny + y] == "" and visit[nx + x][ny + y] == False:
                    q.append((nx + x, ny + y))
                    visit[nx + x][ny + y] = True

    # 지게차 맵 재갱신
    if flag == True:
        # map[i][j]==True
        for a in range(m):
            for b in range(n):
                if visit[a][b] == True:
                    map[a][b] == True

    return flag


def check_alpha(s, alpha):
    del_alpha = []

    global map

    map = [[False] * len(s[0]) for _ in range(len(s))]

    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == alpha:
                check = bfs(s, i, j)
                if check == True:
                    del_alpha.append((i, j))

    for x, y in del_alpha:
        s[x][y] = ""

    return s, len(del_alpha)


def all_alpha(s, alpha):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == alpha:
                s[i][j] = ""

    return s


def solution(storage, requests):
    s = []
    all_ = ""
    for stor in storage:
        s.append(list(stor))
        all_ += stor

    count_alpha = Counter(all_)

    for r in requests:
        if not r[0] in count_alpha:
            continue

        if count_alpha[r[0]] == 0:
            continue

        if len(r) == 2:
            alpha = r[0]
            count_alpha[alpha] = 0
            s = all_alpha(s, alpha)
        else:
            alpha = r
            s, num = check_alpha(s, alpha)
            count_alpha[alpha] -= num

    count = 0

    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] != "":
                count += 1

    return count