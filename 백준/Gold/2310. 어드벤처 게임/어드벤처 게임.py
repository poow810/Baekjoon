import sys


def dfs(lv, start, money):
    global ans

    if lv > N:
        return

    if start == N-1:
        if maze[start][0] == 'T':
            if money >= int(maze[start][1]):
                ans = True
                return
            else:
                return
        else:
            ans = True
            return

    if maze[start][0] == 'E':
        for i in range(2, len(maze[start])):
            if start >= int(maze[start][i])-1:
                continue
            dfs(lv + 1, int(maze[start][i])-1, 0)
    
    elif maze[start][0] == 'L':
        for i in range(2, len(maze[start])):
            if start >= int(maze[start][i])-1:
                continue
            if money < int(maze[start][1]):
                money = int(maze[start][1])
            dfs(lv + 1, int(maze[start][i])-1, money)

    else:
        if money < int(maze[start][1]):
            return
        else:
            money -= int(maze[start][1])
            for i in range(2, len(maze[start])):
                if start >= int(maze[start][i])-1:
                    continue
                dfs(lv + 1, int(maze[start][i])-1, money)


while True:
    N = int(sys.stdin.readline())
    if N == 0:
        exit()
    
    maze = []
    for _ in range(N):
        lst = list(map(str, sys.stdin.readline().split()))
        maze.append(lst[:-1])
    
    ans = False
    dfs(0, 0, 0)
    
    if ans:
        print("Yes")
    else:
        print("No")