import sys

N, M = map(int, sys.stdin.readline().split())
dic = dict()
for _ in range(N):
    string = sys.stdin.readline().strip()
    if string not in dic:
        dic[string] = 1

for _ in range(M):
    lst = sys.stdin.readline().rstrip().split(',')
    for i in lst:
        if i in dic:
            dic.pop(i)
    print(len(dic))