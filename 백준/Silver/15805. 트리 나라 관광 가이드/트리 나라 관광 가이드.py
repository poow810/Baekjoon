import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
length = max(lst)
ans = set()

for i in range(N-1):
    if (lst[i+1], lst[i]) in ans:
        continue
    ans.add((lst[i], lst[i+1]))

res = [0]*200001
res[lst[0]] = -1
for a, b in ans:
    res[b] = a

print(length+1)
for i in range(length+1):
    print(res[i], end=" ")