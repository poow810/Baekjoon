import sys


N, M = map(int, sys.stdin.readline().split())
dic = {}
for i in range(1, N+1):
    a = sys.stdin.readline().rstrip()
    dic[i] = a
dic2 = {v:k for k,v in dic.items()}
for _ in range(M):
    a = sys.stdin.readline().rstrip()
    if a.isdecimal():
        print(dic[int(a)])
    else:
        print(dic2[a])