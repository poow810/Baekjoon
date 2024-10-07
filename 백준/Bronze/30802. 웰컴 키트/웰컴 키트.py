import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
T, P = map(int, sys.stdin.readline().split())

total = sum(lst)
ans1 = 0
for i in lst:
    if i % T == 0:
        ans1 += i // T
    else:
        ans1 += i // T + 1

print(ans1)
print(total // P, total % P)