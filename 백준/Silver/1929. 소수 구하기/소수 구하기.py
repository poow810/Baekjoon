import sys

M, N = map(int, sys.stdin.readline().split())

lst = [x for x in range(N+1)]
m = int(N**0.5)
for i in range(2, m+1):
    if lst[i] == 0:
        continue
    for j in range(i*i, N+1, i):
        lst[j] = 0
ans = [x for x in lst[M:] if lst[x] and lst[x] != 1]
for k in ans:
    print(k)