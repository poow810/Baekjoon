import sys
 
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
first = lst[0]
last = lst[0]
height = 0

if len(lst) == 1:
    height = max(first, N-last)

else:
    for i in range(len(lst)):
        if i == 0:
            x = lst[i]
        elif i == M-1:
            x = N - lst[i]
        
        else:
            dis = lst[i] - lst[i-1]

            if dis % 2 == 0:
                x = dis // 2
            else:
                x = dis // 2 + 1
        
        height = max(x, height)

print(height)