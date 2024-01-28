import sys
# 5x5 숫자판

# 너비 우선 탐색을 하면서, 주위 숫자의 종류를 배열에 넣고
# 다음 인덱스의 수가 배열 내부의 전체 경우의 수를 돌 수 있도록
# dfs?

def is_valid(nx, ny):   # 경계 조건
    return 0 <= nx < 5 and 0 <= ny < 5

def dfs(start_num, x, y):

    if len(str(start_num)) == 6: # 길이 6이면 set에 추가
        result.add(start_num)
        return

    for k in range(4):  # 상하좌우 탐색
        nx = x + dx[k]  
        ny = y + dy[k]

        if is_valid(nx, ny):    
            new_num = str(start_num) + str(mp[nx][ny])
            dfs(new_num, nx, ny)    # 기존 number와 합쳐서 dfs 다시 호출
    

mp = []
for i in range(5):
    mp.append(list(map(int, sys.stdin.readline().split()))) 

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = set()

for i in range(len(mp)):
    for j in range(len(mp)):
        dfs(mp[i][j], i, j)

print(len(result))
