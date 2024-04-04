import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline().rstrip())
hq = []

for _ in range(N):
    a = int(sys.stdin.readline().rstrip())
    if a == 0:
        if not hq:
            print(0)
        else:
            print(heappop(hq))
    else:
        heappush(hq, a)

