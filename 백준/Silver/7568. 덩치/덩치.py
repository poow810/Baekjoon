import sys

N = int(sys.stdin.readline())
lst = []
ans = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    lst.append((x, y))

for i in range(N):
    count = 0
    for j in range(N):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            count += 1
    ans.append(count + 1)

for j in ans:
    print(j, end=" ")