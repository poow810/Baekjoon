import sys

def find_set(x):
    if x == parents[x]:
        return parents[x]
    
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    
    if x == y:
        return
    
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

edges = []

for _ in range(M):
    a, b, w = map(int, sys.stdin.readline().split())
    edges.append([a-1, b-1, w])

edges.sort(key=lambda x: x[2])
parents = [i for i in range(N)]

result = 0
for a, b, w in edges:
    if find_set(a) != find_set(b):
        union(a, b)
        result += w

print(result)