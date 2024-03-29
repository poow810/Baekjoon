import sys

N = int(sys.stdin.readline().rstrip())
dp = [0]*(301)
lst = [0]*(301)
for i in range(N):
    lst[i] = int(sys.stdin.readline().rstrip())

dp[0] = lst[0]
dp[1] = lst[0] + lst[1]
dp[2] = max(lst[0]+lst[2], lst[1]+lst[2])

for j in range(3, N):
    dp[j] = max(dp[j-3] + lst[j-1] + lst[j], dp[j-2] + lst[j])

print(dp[N-1])
