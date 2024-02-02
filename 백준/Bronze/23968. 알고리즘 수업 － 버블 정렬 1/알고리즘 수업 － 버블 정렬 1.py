import sys

N, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
count = 0
# [1, 3, 5, 2, 4]

for i in range(N-1, 0, -1):
    for j in range(0, i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
            count += 1
        
        if count == K:
            print(lst[j], lst[j+1])
            exit()

print(-1)