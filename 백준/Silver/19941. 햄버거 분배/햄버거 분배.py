import sys

N, K = map(int, sys.stdin.readline().split())
lst = list(sys.stdin.readline().strip())
check = [0] * N
count = 0

for i in range(N):
    if lst[i] == 'P':
        for j in range(max(0, i-K), min(N, i+K+1)):
            if lst[j] == 'H' and check[j] == 0:
                check[j] = 1
                count += 1
                break

print(count)
