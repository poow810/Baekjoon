import sys


T = int(sys.stdin.readline().strip())

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    lst_1 = set(list(map(str, sys.stdin.readline().split())))
    M = int(sys.stdin.readline().strip())
    lst_2 = list(map(str, sys.stdin.readline().split()))

    for i in lst_2:
        if i in lst_1:
            print(1)
        else:
            print(0)
