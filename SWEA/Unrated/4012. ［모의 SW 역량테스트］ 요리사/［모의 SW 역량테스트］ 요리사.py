def solution(a, b):

    add1 = 0
    add2 = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            add1 += mp[a[i]][a[j]] + mp[a[j]][a[i]]
            add2 += mp[b[i]][b[j]] + mp[b[j]][b[i]]
    
    return abs(add1-add2)

def dfs(lv, start):
    global ans

    if lv == N//2:
        a, b = [], []
        for j in range(N):
            if visited[j] == 0:
                a.append(j)
            else:
                b.append(j)
        ans = min(ans, solution(a, b))
        return

    for i in range(start, N):
        if visited[i] == 0:
            visited[i] = 1
            lst.append(i)
            dfs(lv+1, i+1)
            lst.pop()
            visited[i] = 0

T = int(input())
for t in range(T):
    N = int(input())
    lst = []
    ans = 99999
    mp = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*(N)
    dfs(0, 0)

    print(f"#{t+1}", ans)