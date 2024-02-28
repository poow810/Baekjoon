def dfs(start, add):
    global count

    if add == K:
        count += 1
        return

    if start > len(lst):
        return

    for i in range(start, N):
        ans.append(lst[i])
        dfs(i + 1, add + lst[i])
        ans.pop()

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    count = 0
    ans = []
    dfs(0, 0)
    print(f"#{t+1}", count)
