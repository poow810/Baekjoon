import sys

N, M = map(int, sys.stdin.readline().split())
dic = {}
for _ in range(N):
    word = sys.stdin.readline().strip()
    if word not in dic:
        dic[word] = [1, len(word), word]
    else:
        dic[word][0] += 1
lst = list(dic.values())
lst.sort(key = lambda x: (-x[0], -x[1], x[2]))
for i in lst:
    if len(i[2]) >= M:
        print(i[2])