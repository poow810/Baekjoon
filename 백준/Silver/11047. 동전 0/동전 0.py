import sys


N, K = map(int, sys.stdin.readline().split())
lst = []
for i in range(N):
    lst.append(int(sys.stdin.readline().rstrip()))

count = 0
for j in range(N-1, -1, -1):
    while K > 0:
        temp = K
        K = K - lst[j]
        if K < 0:
            K = temp
            break

        count += 1

print(count)