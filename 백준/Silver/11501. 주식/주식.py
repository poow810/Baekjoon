import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    lst.reverse()

    max_num = lst[0]
    ans = 0

    for i in range(1, N):
        if lst[i] > max_num:
            max_num = lst[i]
            continue
        
        ans += max_num - lst[i]
    
    print(ans)