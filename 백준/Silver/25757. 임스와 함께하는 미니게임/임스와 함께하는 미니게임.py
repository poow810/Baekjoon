import sys

N, game = map(str, sys.stdin.readline().split())
N = int(N)
check = set()
for _ in range(N):
    name = sys.stdin.readline().strip()
    check.add(name)

if game == 'Y':
    ans = 1
elif game == 'F':
    ans = 2
else:
    ans = 3

print(len(check)//ans)