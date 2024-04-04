import sys

N = int(sys.stdin.readline().rstrip())
lst = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    lst.append((a, b))

lst.sort(key=lambda x: x[0])
lst.sort(key=lambda x: x[1])

count = 1
min_count = lst[0][1]
for i in range(1, N):
    if lst[i][0] >= min_count:
        min_count = lst[i][1]
        count += 1

print(count)