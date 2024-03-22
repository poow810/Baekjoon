import sys


N = int(sys.stdin.readline())

INF = int(1e99)
ans = INF
if N % 5 == 0:
    ans = N // 5
elif N % 3 == 0:
    ans = N // 3

count = 1
res = 0
while True:
    N -= 5
    if N < 0:
        break
    if N % 3 == 0:
        res = count + N // 3
        ans = min(ans, res)
    count += 1

if ans == INF:
    print(-1)
else:
    print(ans)