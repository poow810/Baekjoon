import sys

N, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
count = 0
ans = ()
# [4, 6, 5, 1, 3, 2]
for i in range(N-1, 0, -1):
    for j in range(0, i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
            count += 1
        
        if count == K:
            ans = (lst[j], lst[j+1])
            break
    if ans:
        break
if count < K:
    print(-1)
else:
    print(ans[0], ans[1])