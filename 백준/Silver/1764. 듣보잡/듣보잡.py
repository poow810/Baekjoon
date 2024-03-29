import sys


N, M = map(int, sys.stdin.readline().split())
dic = {}
for _ in range(N):
    a = sys.stdin.readline().rstrip()
    dic[a] = 1

count = 0
ans = []
for _ in range(M):
    b = sys.stdin.readline().rstrip()
    if b in dic:
        count += 1
        ans.append(b)

print(count)
ans.sort()
for i in ans:
    print(i)