import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
ans = abs(100 - N)
if M:
    lst = set(sys.stdin.readline().split())
else:
    lst = []

for j in range(1000001):
    for z in str(j):
        if z in lst:
            break
    else:
        ans = min(ans, len(str(j)) + abs(j - N))

print(ans)