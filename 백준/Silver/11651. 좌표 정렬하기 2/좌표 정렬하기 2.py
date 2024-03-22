import sys


N = int(sys.stdin.readline())
lst = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    lst.append([a, b])

lst.sort(key=lambda x: x[0])
lst.sort(key=lambda x: x[1])

for j in lst:
    print(j[0], j[1])