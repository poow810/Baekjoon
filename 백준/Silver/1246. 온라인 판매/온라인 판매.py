import sys

N, M = map(int, sys.stdin.readline().split())

lst = []

for i in range(M):
    lst.append(int(sys.stdin.readline().strip()))

lst.sort()

max_price = 0
answer = 0

for i in range(M):
    if (M-i) <= N:
        if lst[i] * (M-i) > max_price:
            max_price = lst[i] * (M-i)
            answer = lst[i]
    else:
        if lst[i] * (M-i) > max_price:
            max_price = lst[i] * N

print(answer, max_price)
