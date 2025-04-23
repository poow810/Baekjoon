import sys


N, M = map(int, sys.stdin.readline().split())
lst = [int(sys.stdin.readline().strip()) for _ in range(M)]

lst.sort()

start = 1
end = max(lst)
answer = 0

while start <= end:
    mid = (start + end) // 2
    sum = 0
    
    for i in range(M):
        sum += lst[i]//mid
        if lst[i]%mid != 0:
            sum += 1
    
    if sum > N:
        start = mid + 1
    
    else:
        end = mid - 1
        answer = mid

print(answer)