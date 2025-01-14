import sys

N, M = map(int, sys.stdin.readline().split())

lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline().strip()))

max_length = max(lst)
min_length = 1

while min_length <= max_length:

    mid = (min_length + max_length) // 2
    count = 0

    for num in lst:
        count += num // mid
    
    if count >= M:
        min_length = mid + 1
    else:
        max_length = mid - 1

print(min_length-1)

