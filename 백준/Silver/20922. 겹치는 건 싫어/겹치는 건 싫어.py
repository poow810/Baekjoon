import sys

N, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
left, right = 0, 0

dp = [0] * (max(lst) + 1)
ans = 0
while right < N:
    if dp[lst[right]] < K:
        dp[lst[right]] += 1
        right += 1
    
    else:
        dp[lst[left]] -= 1
        left += 1
    
    ans = max(ans, right - left)

print(ans)