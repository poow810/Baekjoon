import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    W = sys.stdin.readline().strip()
    K = int(sys.stdin.readline().strip())

    dic = dict()
    for index, char in enumerate(W):
        if char not in dic:
            dic[char] = []
        dic[char].append(index)
    
    min_length = 1e99
    max_length = 0

    for i in dic.values():
        if len(i) < K:
            continue

        for j in range(len(i) - K + 1):
            length = i[j + K - 1] - i[j] + 1
            max_length = max(length, max_length)
            min_length = min(length, min_length)
        
    
    if max_length == 0:
        print(-1)
    else:
        print(min_length, max_length)
