import sys

string1 = sys.stdin.readline().strip()
string2 = sys.stdin.readline().strip()

n, m = len(string1), len(string2)
dp = [[0] * (n+1) for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        if string1[j-1] == string2[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[m][n])