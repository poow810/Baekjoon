import sys
from collections import deque
import itertools
import copy


def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N


N, M = map(int, sys.stdin.readline().split())
mp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
lst = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
chicken = []
for i in range(N):
    for j in range(N):
        if mp[i][j] == 2:
            lst.append((i, j))
        elif mp[i][j] == 1:
            chicken.append((i, j))

check = itertools.combinations(lst, M)
min_count = 1e99
for k in check:
    count = 0
    for x, y in chicken:
        min_check = 1e99
        for a, b in k:
            min_check = min(abs(x-a) + abs(y-b), min_check)

        count += min_check
    min_count = min(count, min_count)

print(min_count)
