import sys
from heapq import heappop, heappush

def solution(x):

    if x == 0:
        if hq:
            print(-heappop(hq))
        else:
            print(0)
    else:
        heappush(hq, -x)
    

N = int(sys.stdin.readline().rstrip())
hq = []
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    solution(x)
