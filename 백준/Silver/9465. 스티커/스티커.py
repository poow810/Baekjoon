import sys

T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())
    mp = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    dp = [[0]*N for _ in range(2)]

    dp[0][0] = mp[0][0]
    dp[1][0] = mp[1][0]
    if N == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    dp[0][1] = mp[1][0] + mp[0][1]
    dp[1][1] = mp[1][1] + mp[0][0]
    if N == 2:
        print(max(dp[0][1], dp[1][1]))
        continue
    
    for i in range(2, N):
        dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + mp[0][i]
        dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + mp[1][i]
    
    
    print(max(dp[0][-1], dp[1][-1]))