from collections import deque

def dfs(lv, cal):
    global max_num, min_num

    if lv == len(num_lst)-1:
        if cal > max_num:
            max_num = cal
        if cal < min_num:
            min_num = cal
        return
    
    for i in range(4):
        if cal_lst[i] != 0:
            cal_lst[i] -= 1
            if i == 0:
                result = cal + num_lst[lv+1]
            elif i == 1:
                result = cal - num_lst[lv+1]
            elif i == 2:
                result = cal * num_lst[lv+1]
            else:
                result = int(cal/num_lst[lv+1])
                    
            dfs(lv + 1, result)
            cal_lst[i] += 1


T = int(input())
for t in range(T):
    N = int(input())
    cal_lst = list(map(int, input().split()))
    num_lst = list(map(int, input().split()))
    max_num, min_num = -1e99, 1e99
    dfs(0, num_lst[0])
    print(f"#{t+1}", abs(max_num-min_num))