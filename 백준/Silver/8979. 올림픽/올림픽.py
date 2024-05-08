import sys

N, K = map(int, sys.stdin.readline().split())
mp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

mp.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)
idx = [mp[i][0] for i in range(N)].index(K)

for i in range(N):
    if mp[idx][1:] == mp[i][1:]:
        print(i+1)
        break