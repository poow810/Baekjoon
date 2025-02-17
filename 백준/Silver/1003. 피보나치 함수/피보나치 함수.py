import sys

def dfs(n):

    zero[0], one[0] = 1, 0
    zero[1], one[1] = 0, 1

    for i in range(2, n+1):
        zero[i] = zero[i-1] + zero[i-2]
        one[i] = one[i-1] + one[i-2]


T = int(sys.stdin.readline().strip())

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    zero = [0] * (N+1)
    one = [0] * (N+1)
    if N == 0:
        print(1, 0)
    elif N == 1:
        print(0, 1)
    else:
        dfs(N)
        print(zero[N], one[N])