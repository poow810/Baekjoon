import sys

def dfs(start, lv):
    global result

    if lv == 7:
        if sum(ans) == 100:
            for i in ans:
                print(i)
            exit()
        else:
            return 

    for i in range(start, len(lst)):
        ans.append(lst[i])
        dfs(i+1, lv+1)
        ans.pop()

lst = [int(sys.stdin.readline()) for x in range (9)]
lst.sort()
ans = []
result = []
dfs(0, 0)
