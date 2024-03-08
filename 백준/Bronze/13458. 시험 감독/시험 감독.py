import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())
ref = 0

for i in range(N):
    c = 1
    if c:
        A[i] -= B
        ref += 1
        c -= 1
        if A[i] <= 0:
            continue
    
    if A[i] // C == 0:
        ref += 1
    else:
        if A[i] <= C:
            ref += 1
            continue
        ref += A[i] // C
        A[i] = A[i] % C
        if A[i] != 0 and A[i] <= C:
            ref += 1

print(ref)