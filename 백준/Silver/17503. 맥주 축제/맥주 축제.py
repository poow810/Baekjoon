import sys
from heapq import heappop, heappush

N, M, K = map(int, sys.stdin.readline().split())

lst = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
hq = []

lst.sort(key=lambda x: x[1])
preference = 0
level = -1

for pre, lv in lst:
    preference += pre
    heappush(hq, pre)

    if len(hq) > N:
        a = heappop(hq)
        preference -= a
    
    if len(hq) == N and preference >= M:
        level = lv
        break

    
print(level)