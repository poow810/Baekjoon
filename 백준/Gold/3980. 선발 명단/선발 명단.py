import sys

def dfs(lv, add):
    global max_num

    if lv == 11:
        max_num = max(add, max_num)
        return
    
    for i in range(11):
        if used[i] == 0 and mp[lv][i] != 0:
            used[i] = 1
            dfs(lv + 1, add + mp[lv][i])
            used[i] = 0


T = int(sys.stdin.readline())
for t in range(T):
    mp = [list(map(int, sys.stdin.readline().split())) for _ in range(11)]
    used = [0] * 11
    max_num = 0
    dfs(0, 0)
    print(max_num)