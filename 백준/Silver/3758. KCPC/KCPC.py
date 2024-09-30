import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    n, k, t, m = map(int, sys.stdin.readline().split())
    lst = [[0 for _ in range(k)] for _ in range(n)]
    submit = [0 for _ in range(n)]
    time = [0 for _ in range(n)]
    
    for z in range(m):
        i, j, s = map(int, sys.stdin.readline().split())
        lst[i-1][j-1] = max(lst[i-1][j-1], s)
        submit[i-1] += 1
        time[i-1] = z

    ans = []
    for k in range(len(lst)):
        ans.append([sum(lst[k]), submit[k], time[k], k+1])

    ans.sort(key=lambda x : (-x[0], x[1], x[2]))

    for i in range(len(ans)):
        if ans[i][3] == t:
            print(i+1)

