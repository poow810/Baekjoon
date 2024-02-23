def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

def solution():

    max_num = 0
    for i in range(N-1):
        for j in range(N-1):
            add = 0
            for z in range(i, i+M):
                for k in range(j, j+M):

                    if not is_valid(z, k):
                        continue
                    add += mp[z][k]

            if add > max_num:
                max_num = add

    return max_num         
                    

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    mp = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    ans = solution()

    print(f"#{t+1}", ans)