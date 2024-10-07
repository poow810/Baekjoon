from collections import defaultdict
import sys

N = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.readline().split()))
left, right = 0, 0
fruit_count = 0

ans = 0
fruit = defaultdict(int)
while right < N:
    if fruit[lst[right]] == 0:
        fruit_count += 1
    fruit[lst[right]] += 1

    while fruit_count > 2:
        fruit[lst[left]] -= 1
        if fruit[lst[left]] == 0:
            fruit_count -= 1
        
        left += 1
    
    ans = max(ans, right - left + 1)
    right += 1

print(ans)