import sys


def dfs(num, count):
    global min_count

    if num == 1:
        min_count = min(min_count, count)
        return
    
    if count > min_count:
        return

    if num % 3 == 0:
        dfs(num // 3, count + 1)

    if num % 2 == 0:
        dfs(num // 2, count + 1)

    dfs(num - 1, count + 1)    


N = int(sys.stdin.readline())
min_count = 1e99
dfs(N, 0)
print(min_count)