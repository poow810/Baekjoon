import sys
from heapq import heappop, heappush


N = int(sys.stdin.readline().rstrip())
hq = []
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())

    if x != 0 and x < 0:
        heappush(hq, (-x, False))
    elif x != 0 and x > 0:
        heappush(hq, (x, True))
    elif x == 0:
        if hq:
            a, b = heappop(hq)
            if not b:
                print(-a)
            else:
                print(a)
        else:
            print(0)
