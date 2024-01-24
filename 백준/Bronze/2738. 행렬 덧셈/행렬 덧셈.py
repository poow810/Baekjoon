import sys

N, M = map(int, sys.stdin.readline().split())
A = []
B = []
for i in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

for j in range(N):
    B.append(list(map(int, sys.stdin.readline().split())))

for k in range(N):
    for z in range(M):
        print(A[k][z]+B[k][z], end=" ")
    print()
