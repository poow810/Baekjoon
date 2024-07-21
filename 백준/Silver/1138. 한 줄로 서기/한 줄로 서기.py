import sys

N = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))
mp = [0] * N

for i in range(N):
    count = 0
    for j in range(N):
        if count == lst[i] and mp[j] == 0:
            mp[j] = i + 1
            break
        elif mp[j] == 0:
            count += 1


print(' '.join(map(str, mp)))