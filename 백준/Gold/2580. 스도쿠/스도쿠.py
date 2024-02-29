import sys

def checkRow(x, y, num):

    for i in range(9):
        if i != x:
            if mp[i][y] == num:
                return False
    return True

def checkCol(x, y, num):

    for i in range(9):
        if i != y:
            if mp[x][i] == num:
                return False
    return True
            
def checkSquare(x, y, num):
    
    for i in range(x//3*3, x//3*3 + 3):
        for j in range(y//3*3, y//3*3 + 3):
            if (i, j) != (x, y):
                if mp[i][j] == num:
                    return False
    return True

def dfs(idx):

    if idx == len(lst):
        for j in mp:
            print(" ".join(map(str, j)))
        exit()


    # 숫자 넣고 나서, 가로, 세로, 네모를 탐색하여 검증 -> visited 배열이 이미 1 인지

    for i in range(1, 10):
        x, y = lst[idx][0], lst[idx][1]

        if checkRow(x, y, i) and checkCol(x, y, i) and checkSquare(x, y, i):
            mp[x][y] = i
            dfs(idx+1)
            mp[x][y] = 0


mp = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
lst = []
for i in range(9):
    for j in range(9):
        if mp[i][j] == 0:
            lst.append((i, j))

dfs(0)
