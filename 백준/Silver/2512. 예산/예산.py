import sys
 
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

start, end = 0, max(lst)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in lst:
        if i > mid:
            total += mid
        else:
            total += i
    if total <= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)