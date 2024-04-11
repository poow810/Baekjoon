import copy

def check_dfs(D, W, temp, k):  # lv는 세로행, 

    for j in range(W):
        count = 0
        flag = 2
        check = False
        for i in range(D):
            if temp[i][j] == 0:
                if flag != 0:
                    count = 0
                    flag = 0
                count += 1
            
            elif temp[i][j] == 1:
                if flag != 1:
                    count = 0
                    flag = 1
                count += 1
        
            if count >= k:
                check = True
        if check == False:
            return check
    
    return check

def film_dfs(change, lv, temp, k):
    global min_change

    if change > min_change:
        return

    if lv == D:
        if check_dfs(D, W, temp, k):
            min_change = min(min_change, change)
        return
    
    film_dfs(change, lv+1, temp, k)
    
    for i in range(W):
        temp[lv][i] = 0
    film_dfs(change + 1, lv + 1, temp, k)

    for j in range(W):
        temp[lv][j] = 1
    film_dfs(change + 1, lv + 1, temp, k)
    
    for k in range(W):
        temp[lv][k] = mp[lv][k]


T = int(input())
for t in range(T):
    D, W, K = map(int, input().split())
    mp = [list(map(int, input().split())) for _ in range(D)]
    temp = copy.deepcopy(mp)
    min_change = K
    film_dfs(0, 0, temp, K)
    print(f"#{t+1}", min_change)