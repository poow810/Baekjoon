import sys


N = int(sys.stdin.readline())
lst = [0]*21

for _ in range(N):
    a, *b = map(str, sys.stdin.readline().split())

    if a =="add":
        lst[int(b[0])] = 1

    elif a == "check":
        if lst[int(b[0])]:
            print(1)
        else:
            print(0)
    elif a == "remove":
        if lst[int(b[0])]:
            lst[int(b[0])] = 0
    elif a == "toggle":
        if lst[int(b[0])]:
            lst[int(b[0])] = 0
        else:
            lst[int(b[0])] = 1
    elif a == "all":
        lst = [1]*21
    else:
        lst = [0]*21