import sys
from heapq import heappop, heappush

N = int(sys.stdin.readline().strip())
lst = []
for _ in range(N):
    n, s, e = map(int, sys.stdin.readline().split())
    lst.append((s, e))

lst.sort()

classroom = []
heappush(classroom, lst[0][1])

for i in range(1, N):
    start, end = lst[i]
    if classroom[0] <= start:
        heappop(classroom)
    heappush(classroom, end)
    
print(len(classroom))