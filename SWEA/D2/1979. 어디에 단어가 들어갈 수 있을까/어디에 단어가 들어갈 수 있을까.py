def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

def solution():

    ans = 0

    for i in range(N):
        count = 0
        for j in range(N):
            if mp[i][j] == 1:
                count += 1
            if mp[i][j] == 0 or j == N-1:
                if count == K:
                    ans += 1
                count = 0
    
    for k in range(N):
        count = 0
        for z in range(N):
            if mp[z][k] == 1:
                count += 1
            if mp[z][k] == 0 or z == N-1:
                if count == K:
                    ans += 1
                count = 0 
    
    return ans



T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    mp = [list(map(int, input().split())) for _ in range(N)]
    result = solution()


    print(f"#{t+1}", result)