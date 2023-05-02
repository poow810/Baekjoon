import sys
sys.setrecursionlimit(10000)

def dfs(i, j):
    array[i][j] = 0
    for dx, dy in [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]:
        nx = i + dx
        ny = j + dy

        if 0 <= nx < h and 0 <= ny <w:
            if array[nx][ny] == 1:
                dfs(nx, ny)


while True:
    w, h = map(int, input().split())
   
    if w == h == 0:
        break
    
	# graph 구현
    array = []
    for _ in range(h):
        array.append(list(map(int, input().split())))
    
    count = 0
    for i in range(h):
        for j in range(w):
            if array[i][j] == 1:
                dfs(i, j)
                count += 1
    print(count)