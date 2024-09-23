import sys

P = int(sys.stdin.readline())
for _ in range(P):
    T, *lst = map(int, sys.stdin.readline().split())
    count = 0

    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                count += 1

    print(T, count)