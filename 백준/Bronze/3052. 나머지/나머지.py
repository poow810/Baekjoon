import sys

n = []
for i in range(10):
    n.append(int(sys.stdin.readline()))

ans = []

for j in range(10):
    if n[j]%42 in ans:
        pass
    else:
        ans.append(n[j]%42)

print(len(ans))