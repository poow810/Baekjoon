import sys


N = int(sys.stdin.readline().rstrip())
lst = []
for z in range(N):
    lst.append(int(sys.stdin.readline().rstrip()))
dp = [0] * (101)
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4, 101):
    dp[i] = dp[i - 3] + dp[i - 2]

for j in lst:
    print(dp[j])