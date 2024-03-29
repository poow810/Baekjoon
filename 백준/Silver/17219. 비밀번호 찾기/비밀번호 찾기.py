import sys


N, M = map(int, sys.stdin.readline().split())
dic = {}
for _ in range(N):
    a, b = sys.stdin.readline().split()
    dic[a] = b

for _ in range(M):
    check = sys.stdin.readline().rstrip()
    print(dic[check])