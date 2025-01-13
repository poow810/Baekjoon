import sys

N, K = map(int, sys.stdin.readline().split())
words = []

for _ in range(N):
    words.append(sys.stdin.readline().strip())

alphabet = [0] * 26
answer = 0

def check():

    count = 0
    for word in words:
        flag = True
        for s in word:
            if not alphabet[ord(s)-97]:
                flag = False
                break
        if flag:
            count += 1

    return count
        
def dfs(lv, start):
    global answer

    if lv == K:
        answer = max(answer, check())
        return

    for i in range(start, 26):
        if not alphabet[i]:
            alphabet[i] = 1
            dfs(lv + 1, i)
            alphabet[i] = 0

if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    for c in ('a', 'n', 't', 'i', 'c'):
        alphabet[ord(c)-97] = 1
    
    dfs(5, 0)

    print(answer)
