import sys
from collections import deque

N = int(sys.stdin.readline())
lst1 = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
lst2 = list(map(int, sys.stdin.readline().split()))

dic = {}
for i in lst1:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
for j in lst2:
    if j in dic:
        print(dic[j], end = " ")
    else:
        print(0, end = " ")