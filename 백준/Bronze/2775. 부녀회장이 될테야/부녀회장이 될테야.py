import sys

T = int(sys.stdin.readline())
arr = [[0]*15 for _ in range(15)]

# 0층
for i in range(15):
    arr[0][i] = i + 1

# n층
for j in range(1, 15):
    for k in range(15):
        arr[j][k] = sum(arr[j-1][:k+1])


for i in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(arr[k][n-1])

# 0층 1 2 3 4 5 
# 1층 1 3 6 10 15 
# 2층 1 4 10 20 35 
# 3층 1 5 15 35 70 
