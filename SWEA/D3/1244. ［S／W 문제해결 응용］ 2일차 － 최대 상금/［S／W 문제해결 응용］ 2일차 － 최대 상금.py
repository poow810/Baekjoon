def dfs(lv, lst):
    global max_num

    if tuple(lst) not in visited[lv]:
        visited[lv].add(tuple(lst))
    else:
        return
    
    if lv == N:
        for i in visited[lv]:
            if max_num < int("".join(map(str, i))):
                max_num = int("".join(map(str, i)))
        return

    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            lst[j], lst[i] = lst[i], lst[j]
            dfs(lv + 1, lst)
            lst[j], lst[i] = lst[i], lst[j]


T = int(input())
for t in range(T):
    tar, N = map(int, input().split())
    lst = list(map(int, str(tar)))
    visited = [set() for _ in range(N+1)]
    max_num = 0
    dfs(0, lst)
    print(f"#{t+1}", max_num)