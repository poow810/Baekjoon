import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    start = 0
    end = N
    count = 0

    while start <= end:
        mid = (start + end) // 2
        if mid * (mid + 1) // 2 > N:
            end = mid - 1
        
        else:
            count = mid
            start = mid + 1
    
    print(count)