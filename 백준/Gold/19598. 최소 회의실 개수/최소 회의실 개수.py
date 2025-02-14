import sys
from heapq import heappop, heappush


N = int(sys.stdin.readline().strip())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
lst.sort(key=lambda x: x[0])
hq = []

for start, end in lst:
    if not hq:
        heappush(hq, (end, start))
    
    else:
        if hq[0][0] > end and hq[0][1] < start:
            heappush(hq, (end, start))
        
        elif hq[0][0] <= start:
            heappop(hq)
            heappush(hq, (end, start))
        
        elif hq[0][0] > start:
            heappush(hq, (end, start))

print(len(hq))