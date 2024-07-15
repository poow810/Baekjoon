import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline())
hp = []

for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    for num in lst:
        heappush(hp, num)
        if len(hp) > N:
            heappop(hp)

print(hp[0])