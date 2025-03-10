import sys

N, K = map(int, sys.stdin.readline().split())
lst = []
for i in range(N):
    a = int(sys.stdin.readline().strip())
    if a != 0:
        lst.append(a)
lst.sort()

start = 1
end = lst[-1]
answer = 0

while start <= end:
    mid = (start + end) // 2
    count = 0

    for i in lst:
        count += i // mid
    
    if count >= K:
        start = mid + 1
        answer = mid
    
    else:
        end = mid - 1
    
print(answer)