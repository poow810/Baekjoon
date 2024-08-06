import sys

N = int(sys.stdin.readline().strip())
max_dp = [0] * 3
min_dp = [0] * 3

max_temp = [0] * 3
min_temp = [0] * 3

for i in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    for j in range(3):
        if j == 0:
            max_temp[j] = arr[0] + max(max_dp[j], max_dp[j+1])
            min_temp[j] = arr[0] + min(min_dp[j], min_dp[j+1])
        elif j == 1:
            max_temp[j] = arr[1] + max(max_dp[j-1], max_dp[j], max_dp[j+1])
            min_temp[j] = arr[1] + min(min_dp[j-1], min_dp[j], min_dp[j+1])
        else:
            max_temp[j] = arr[2] + max(max_dp[j], max_dp[j-1])
            min_temp[j] = arr[2] + min(min_dp[j], min_dp[j-1])
    
    for k in range(3):
        max_dp[k] = max_temp[k]
        min_dp[k] = min_temp[k]


print(max(max_dp), min(min_dp))