def dfs(lv, add):
    global min_add
    
    if add >= min_add:
        return
    
    if add >= B:
        min_add = min(min_add, add)

    if lv == N:
        return

    dfs(lv + 1, add + lst[lv])
    dfs(lv + 1, add)


T = int(input())
for t in range(T):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    visited = [0]*N
    min_add = 1e99
    dfs(0, 0)
    print(f"#{t+1}", min_add-B)