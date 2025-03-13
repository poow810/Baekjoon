import sys

N = int(sys.stdin.readline().strip())
mp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

start = 0
total = 0
end = 0
answer = 0

for i in mp:
    if max(i) > end:
        end = max(i)
    total += sum(i)

while start <= end:
    mid = (start + end) // 2
    count = 0

    for i in mp:
        for j in i:
            if j > 0:
                if j > mid:
                    count += mid
                else:
                    count += j

    
    if count >= total / 2:
        end = mid - 1
        answer = mid
    
    else:
        start = mid + 1

print(answer)