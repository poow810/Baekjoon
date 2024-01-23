import sys

A, B, C = map(int, sys.stdin.readline().split())
num = [A, B, C]
for i in range(len(num)):
    for k in range(1, len(num)-i):
        if num[k-1] >= num[k]:
            temp = num[k-1]
            num[k-1] = num[k]
            num[k] = temp
        else:
            pass

print(num[1])