import sys


N, M = map(int, sys.stdin.readline().split())
lst = [int(sys.stdin.readline().strip()) for _ in range(N)]

left = max(lst)
right = sum(lst)

while left <= right:
    mid = (left + right) // 2
    money = mid
    count = 1

    for i in lst:
        if money - i < 0:
            count += 1
            money = mid
        money -= i
    
    if count > M:
        left = mid + 1
    else:
        right = mid - 1

print(mid)
