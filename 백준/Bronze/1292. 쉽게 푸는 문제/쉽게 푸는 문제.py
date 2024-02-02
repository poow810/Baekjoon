import sys
A, B = map(int, sys.stdin.readline().split())

lst = []
for i in range(0, 100):
    for j in range(i):
        lst.append(i)

add = 0
for k in range(A-1, B):
    add += lst[k]

print(add)