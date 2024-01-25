import sys

add = []
for i in range(5):
    a, b, c, d = map(int, sys.stdin.readline().split())
    add.append(a+b+c+d)
result = max(add)
print(add.index(result) + 1, result)