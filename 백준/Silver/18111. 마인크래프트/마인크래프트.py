import sys


N, M, B = map(int, sys.stdin.readline().split())
mp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = 1e99
res = 0
for i in range(257):
    add = 0
    minus = 0
    for j in range(N):
        for k in range(M):
            if mp[j][k] > i:
                minus += mp[j][k] - i
            else:
                add += i - mp[j][k]
    
    if add > minus + B:
        continue

    count = minus*2 + add
    if count <= ans:
        ans = count
        res = i

print(ans, res)