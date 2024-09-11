import sys

N = int(sys.stdin.readline().strip())

dist = [0] * 1001
max_high = 0
max_high_idx = 0
end_idx = 0

for i in range(N):
    L, H = map(int, sys.stdin.readline().split())
    dist[L] = H

    if max_high < H:
        max_high = H
        max_high_idx = L
    end_idx = max(end_idx, L)

stack = []
ans = 0

for j in range(0, max_high_idx + 1):
    if not stack:
        stack.append(dist[j])
    else:
        if stack[-1] < dist[j]:
            stack.append(dist[j])
    ans += stack[-1]

stack = []

for k in range(end_idx, max_high_idx, -1):
    if not stack:
        stack.append(dist[k])
    else:
        if stack[-1] < dist[k]:
            stack.append(dist[k])
    
    ans += stack[-1]

print(ans)