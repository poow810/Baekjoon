import sys

N = int(sys.stdin.readline().strip())

mp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

mp = [num for row in mp for num in row]

start = 0
total = sum(mp)
end = max(mp)
answer = 0

while start <= end:
    mid = (start + end) // 2
    count = 0

    for i in mp:
        count += i if i < mid else mid
    
    if count >= (total / 2):
        end = mid - 1
        answer = mid
    
    else:
        start = mid + 1

print(answer)