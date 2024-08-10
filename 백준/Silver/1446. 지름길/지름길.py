import sys

N, D = map(int, sys.stdin.readline().split())
dp = [i for i in range(D+1)]

shortcut = []
for _ in range(N):
    start, end, length = map(int, sys.stdin.readline().split())
    if end - start > length:
        shortcut.append((start, end, length))
shortcut.sort()

for start, end, length in shortcut:
    for i in range(1, D+1):
        if end == i:
            dp[i] = min(dp[i], dp[start]+length)
        else:
            dp[i] = min(dp[i], dp[i-1]+1)
print(dp[D])