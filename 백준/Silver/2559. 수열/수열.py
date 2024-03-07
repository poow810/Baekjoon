import sys

N, S = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
result = []
result.append(sum(lst[:S]))

for i in range(N-S):
    result.append(result[i] - lst[i] + lst[i+S])

print(max(result))