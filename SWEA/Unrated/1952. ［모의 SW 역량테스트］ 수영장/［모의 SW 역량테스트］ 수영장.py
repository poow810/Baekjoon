def dfs(lv, add):
    global min_count

    if lv >= 12:
        min_count = min(add, min_count)
        return
    
    if add >= min_count:
        return

    dfs(lv + 1, add + lst[0]*plan[lv])
    dfs(lv + 1, add + lst[1])
    dfs(lv + 3, add + lst[2])
    dfs(lv + 12, add + lst[3])

T = int(input())
for t in range(T):
    lst = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    min_count = 1e99
    dfs(0, 0)
    print(f"#{t+1}", min_count)