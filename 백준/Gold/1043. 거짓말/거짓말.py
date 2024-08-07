import sys

def union(x, y):
    x = find(x); y = find(y)
    if x < y:
        parents[y] = x
    
    else:
        parents[x] = y


def find(x):
    if x == parents[x]:
        return x
    return find(parents[x])

N, M = map(int, sys.stdin.readline().split())
parents = [i for i in range(N+1)]
a, *lst = map(int, sys.stdin.readline().split())

for i in lst:
    parents[i] = 0

party = []
for _ in range(M):
    a, *mp = map(int, sys.stdin.readline().split())
    party.append(mp)
    if a == 1:
        continue

    for i in range(a-1):
        union(mp[i], mp[i+1])

ans = 0
for p in party:
    for i in p:
        if find(parents[i]) == 0:
            break
    else:
        ans += 1
print(ans)