import sys

N = int(sys.stdin.readline())

for i in range(1, N+1):
    ans = i + sum(map(int, str(i)))
    if ans == N:
        print(i)
        break
    ans = 0
else:
    print(0)