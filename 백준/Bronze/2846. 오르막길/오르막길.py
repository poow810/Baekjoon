import sys
N = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))

add = 0
ans = []
for i in range(len(lst)-1):
    if lst[i] >= lst[i+1]:
        ans.append(add)
        add = 0
        continue
    
    else: 
        add += lst[i+1] - lst[i]

    if i == len(lst)-2:
        ans.append(add)

print(max(ans))
