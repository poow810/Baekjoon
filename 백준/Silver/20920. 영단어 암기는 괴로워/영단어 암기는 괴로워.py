import sys
 
N, M = map(int, sys.stdin.readline().split())
dic = dict()
for i in range(N):
    word = sys.stdin.readline().strip()
    if len(word) < M:
        continue
    
    if word not in dic:
        dic[word] = [1, len(word)]
    else:
        dic[word][0] += 1

answer = sorted(dic.items(), key=lambda x: (-x[1][0], -x[1][1], x[0]), reverse=False)
for i in answer:
    print(i[0])
