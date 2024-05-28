import sys

N = int(sys.stdin.readline().strip())
mp = [[0]*100 for _ in range(100)]
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    for j in range(100-b, 100-b-10, -1):
        for k in range(a, a+10):
            mp[j][k] = 1

count = 0
for i in range(100):
    count += mp[i].count(1)

print(count)