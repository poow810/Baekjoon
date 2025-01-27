import sys


M, N = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(lst)
answer = 0

while start <= end:
    mid = (start + end) // 2
    count = 0

    for i in lst:
        if i < mid:
            continue
        else:
            count += i // mid

    
    if count >= M:
        answer = max(mid, answer)
        start = mid + 1
    
    else:
        end = mid - 1

print(answer)