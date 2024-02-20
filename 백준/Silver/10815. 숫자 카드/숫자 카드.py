import sys

N = int(sys.stdin.readline())
sang = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

dic = {}
for i in sang:
    dic[i] = 1

for j in check:
    if j in dic:
        print(1, end=" ")
    else:
        print(0, end=" ")