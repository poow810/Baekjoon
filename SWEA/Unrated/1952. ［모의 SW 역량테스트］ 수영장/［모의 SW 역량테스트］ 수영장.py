def dfs(lv, add):
    global min_num
    
    if lv == 12:
        if min_num > add:
            min_num = add
        return
    
    elif lv > 12:
        return

    if add > min_num:
        return
    
    dfs(lv+1, add + lst[0]*day[lv])
    dfs(lv+1, add + lst[1])
    dfs(lv+3, add + lst[2])
    dfs(lv+12, add + lst[3])

T = int(input())
for t in range(T):
    lst = list(map(int, input().split()))
    day = list(map(int, input().split()))
    min_num = 1e99
    dfs(0, 0)

    print(f"#{t+1}", min_num)