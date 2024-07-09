import sys

N = int(sys.stdin.readline())
for _ in range(N):
    n, k, t, m = map(int, sys.stdin.readline().split())
    lst = [[0 for _ in range(k)] for _ in range(n)]
    submit = [0 for _ in range(n)]
    time = [0 for _ in range(n)]
    for g in range(m):
        i, j, s = map(int, sys.stdin.readline().split())
        lst[i-1][j-1] = max(lst[i-1][j-1], s)
        time[i-1] = g
        submit[i-1] += 1
    
    ans = []
    for idx in range(len(lst)):
        ans.append([sum(lst[idx]), submit[idx], time[idx], idx])
    
    ans.sort(key=lambda x: (-x[0], x[1], x[2]))
    for i in range(len(ans)):
        if ans[i][3] == t-1:
            print(i+1)
            break