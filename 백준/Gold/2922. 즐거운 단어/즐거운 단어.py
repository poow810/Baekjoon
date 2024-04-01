import sys

def check(string):

    if 'L' not in string:
        return False
    
    for i in range(len(string)-2):
        if string[i] in vowel and string[i+1] in vowel and string[i+2] in vowel:
            return False
        if string[i] in con and string[i+1] in con and string[i+2] in con:
            return False
    
    return True


def dfs(lv, string, w):
    global ans

    if '_' not in string:
        if check(string):
            ans += w
        return
        
    for i in range(lv, len(word)):
        if string[i] == '_':
            new_string = string[:i] + 'A' + string[i+1:]
            dfs(lv+1, new_string, w*5)
            new_string = string[:i] + 'B' + string[i+1:]
            dfs(lv+1, new_string, w*20)
            new_string = string[:i] + 'L' + string[i+1:]
            dfs(lv+1, new_string, w)
            return
                   

word = sys.stdin.readline().rstrip()
vowel = ['A', 'E', 'I', 'O', 'U']
con = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
ans = 0
dfs(0, word, 1)
print(ans)