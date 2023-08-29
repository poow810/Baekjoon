import sys

T = int(sys.stdin.readline())
for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    Y = N % H
    X = N // H + 1
    if Y == 0:
        Y = H
        X -= 1
    print(Y * 100 + X)