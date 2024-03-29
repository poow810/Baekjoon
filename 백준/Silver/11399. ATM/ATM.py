import sys


N = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
add = 0
for i in range(1, N+1):
    for j in range(i):
        add += lst[j]
print(add)