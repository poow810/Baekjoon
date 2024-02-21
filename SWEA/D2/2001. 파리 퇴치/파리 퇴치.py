def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

def check():

    max_add = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            add = 0
            for k in range(i, i+M):
                for z in range(j, j+M):
                    add += mp[k][z]
            if add > max_add:
                max_add = add
    return max_add


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    mp = [list(map(int, input().split())) for _ in range(N)]
    ans = check()

    print(f"#{t+1}", ans)