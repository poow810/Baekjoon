import sys

def dfs(lv, start, string):

    if lv == L:
        a, b = 0, 0
        for i in string:
            if i in vowel:
                a += 1
            else:
                b += 1
        
        if a > 0 and b > 1:
            print(string)
        return
    
    for i in range(start, len(lst)):
        dfs(lv + 1, i + 1, string + lst[i])


L, C = map(int, sys.stdin.readline().split())
lst = list(map(str, sys.stdin.readline().split()))
lst.sort()
vowel = ['a', 'e', 'i', 'o', 'u']
dfs(0, 0, "")
