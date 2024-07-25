import sys

def dfs(string, t):
    global ans

    if len(string) == len(t):
        if string == t:
            ans = 1
        return
    
    if t[-1] == 'A':
        dfs(string, t[:-1])
    if t[0] == 'B':
        dfs(string, t[:0:-1])
    

S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()

ans = 0
dfs(S, T)
print(ans)