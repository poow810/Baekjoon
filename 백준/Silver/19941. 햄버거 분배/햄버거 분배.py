import sys

N, K = map(int, sys.stdin.readline().split())
string = list(sys.stdin.readline().strip())
check = [0]*(N)
count = 0

for i in range(N):
    if string[i] == 'P':
        for j in range(max(0, i-K), min(N, i+K+1)):
            if string[j] == 'H':
                string[j] = 0
                count += 1
                break
print(count)