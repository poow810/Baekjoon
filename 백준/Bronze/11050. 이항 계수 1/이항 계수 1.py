import sys

N, K = map(int, sys.stdin.readline().split())


def math(N, K):
    if K == 0 or K == N:
        return 1
    return math(N-1, K-1)+ math(N-1, K)

print(math(N, K))