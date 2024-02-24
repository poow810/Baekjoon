def dfs(lv, idx):
    global ans

    if "".join(init) == target:
        ans = lv
        return

    for j in range(N):
        if init[j] != target[j]:
            idx = j
            break

    for i in range(idx, N):
        if init[i] == '0':
            init[i] = '1'
        else:
            init[i] = '0'    
    dfs(lv + 1, idx + 1)

T = int(input())
for t in range(T):
    target = input()
    N = len(target)
    init = list('0'*N)
    ans = 0
    idx = 0
    for i in range(N):
        if target[i] == '1':
            idx = i
            break
    dfs(0, idx)
    print(f"#{t+1}", ans)