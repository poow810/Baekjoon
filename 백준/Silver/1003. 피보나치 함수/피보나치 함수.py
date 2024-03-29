import sys


def fibo(n):
    l = len(zero)
    if n >= l:
        for i in range(l, n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(zero[n], one[n])


T = int(sys.stdin.readline().rstrip())
one = [0, 1, 1]
zero = [1, 0, 1]

for _ in range(T):
    fibo(int(sys.stdin.readline().rstrip()))