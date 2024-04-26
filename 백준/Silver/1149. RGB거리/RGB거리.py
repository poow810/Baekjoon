import sys

N = int(sys.stdin.readline().rstrip())
mp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(1, N):
    mp[i][0] = min(mp[i-1][1], mp[i-1][2]) + mp[i][0]
    mp[i][1] = min(mp[i-1][0], mp[i-1][2]) + mp[i][1]
    mp[i][2] = min(mp[i-1][0], mp[i-1][1]) + mp[i][2]

print(min(mp[N-1]))