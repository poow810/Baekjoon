import sys

A, B = sys.stdin.readline().split()
N, M = len(A), len(B)
mp = [['.'] * N for _ in range(M)]

for i in range(N):
    if A[i] in B:
        row = i
        col = B.index(A[i])
        break

for j in range(M):
    mp[j][row] = B[j]

for k in range(N):
    mp[col][k] = A[k]

for z in mp:
    print(''.join(z))