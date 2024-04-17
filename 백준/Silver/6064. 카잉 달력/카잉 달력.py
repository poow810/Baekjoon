import sys


def solution(m, n, x, y):

    while x <= m * n:
        if (x-y) % n == 0:
            return x
        x += m
    return -1

t = int(sys.stdin.readline().rstrip())
for i in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())
    print(solution(m, n, x, y))