import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    max_num = max(lst)
    team = {}
    check = [[0, 0, 0, 0] for _ in range(max_num + 1)]

    for i in range(N):
        if lst[i] not in team:
            team[lst[i]] = 1
        else:
            team[lst[i]] += 1
            if team[lst[i]] == 5:
                check[lst[i]][1] = i
                check[lst[i]][3] = lst[i]

    idx = 1
    c = 0
    while c < N:
        if team[lst[c]] >= 6:
            if check[lst[c]][2] < 4:
                check[lst[c]][2] += 1
                check[lst[c]][0] += idx
            idx += 1
        
        c += 1
    
    idx = 0
    while True:
        if check[idx][0] == 0:
            del check[idx]
        else:
            idx += 1
        if idx == len(check):
            break
    check.sort(key=lambda x:(x[0], x[1]))
    print(check[0][3])
    
    