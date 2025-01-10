import sys

def find_squre(s):
    for i in range(N-s+1):
        for j in range(M-s+1):
            if mp[i][j] == mp[i][j+s-1] == mp[i+s-1][j] == mp[i+s-1][j+s-1]:
                return True


N, M = map(int, sys.stdin.readline().split())

mp = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

check = min(N, M)

for i in range(check, 0, -1):
    if find_squre(i):
        print(i**2)
        break