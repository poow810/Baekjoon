import sys


def dfs(lv, string):
    
    lst.append(int(string))

    if lv == 0:
        return
    
    for i in range(lv - 1, -1, -1):
        dfs(i, string+str(i))


N = int(sys.stdin.readline().strip())

lst = []
for i in range(0, 10):
    dfs(i, str(i))

lst.sort()

if N > len(lst):
    print(-1)
else:
    print(lst[N-1])