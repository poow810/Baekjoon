import sys
from heapq import heappop, heappush

n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
hq = []
for i in lst:
    heappush(hq, i)

for _ in range(m):
    first = heappop(hq)
    second = heappop(hq)
    add = first + second
    heappush(hq, add)
    heappush(hq, add)

ans = 0
for j in hq:
    ans += j

print(ans)