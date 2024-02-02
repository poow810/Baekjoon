import sys

N, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

count = 0
for i in range(len(lst)-1, 0, -1):
    max_idx = i
    for j in range(0, i):
        if lst[max_idx] < lst[j]:
            max_idx = j

    if not i == max_idx:

        lst[i], lst[max_idx] = lst[max_idx], lst[i]
        count += 1
        
    if count == K:
        print(lst[max_idx], lst[i])
        exit()

print(-1)