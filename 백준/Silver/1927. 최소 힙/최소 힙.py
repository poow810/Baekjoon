import sys
from heapq import heappop, heappush

N = int(sys.stdin.readline().strip())
lst = []
for i in range(N):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if not lst:
            print(0)
        else:
            print(heappop(lst))

    else:
        heappush(lst, x)
