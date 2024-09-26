import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
a = lst[0]
height = 0
if len(lst) == 1:
    height = max(a, N-a)

else:
    for i in range(len(lst)):
        if i == 0:
            x = lst[i]
        elif i == M-1:
            x = N - lst[i]
        else:
            tmp = lst[i] - lst[i-1]
            if tmp % 2:
                x = tmp // 2 + 1
            else:
                x = tmp // 2
        height = max(x, height)

print(height)