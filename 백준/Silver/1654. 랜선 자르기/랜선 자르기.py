import sys

K, N = map(int, sys.stdin.readline().split())
cm = [int(sys.stdin.readline()) for _ in range(K)]

max_cm = 0
min_cm = 1
for i in cm:
    if i > max_cm:
        max_cm = i

while min_cm <= max_cm:
    
    count = 0
    mid = (min_cm + max_cm) // 2
    for j in cm:
        count += j // mid
    
    if count < N:
        max_cm = mid - 1
    else:
        min_cm = mid + 1
    
print(min_cm-1)

