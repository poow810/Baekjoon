def solution(lv, sum, path):
    global num

    if lv == N+1:
        sum += abs(mp[path][0] - end[0]) + abs(mp[path][1] - end[1])
        num = min(num, sum)
        return
    
    if sum > num: 
        return

    for i in range(N+1):
        if visited[i] == 0:
            visited[i] = 1
            solution(lv + 1, sum + abs(mp[path][0] - mp[i][0]) + abs(mp[path][1] - mp[i][1]), i)
            visited[i] = 0


T = int(input())
for t in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    mp = []
    end = []
    for i in range(N+2):
        if i == 2:
            end.append(lst[i])
        elif i == 3:
            end.append(lst[i])
        if i != 1:
            a, b = lst[i*2], lst[i*2+1]
            mp.append([a, b])
    visited = [0] * (N+1)
    num = 1e99
    solution(0, 0, 0)
    print(f"#{t+1}", num)