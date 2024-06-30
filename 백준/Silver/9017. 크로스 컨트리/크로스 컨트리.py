import sys
 
T = int(sys.stdin.readline())

for t in range(T):
    dic = dict()
    N = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))

    for i in lst:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    to_remove = []
    for key in dic:
        if dic[key] < 6:
            to_remove.append(key)
    for key in to_remove:
        del dic[key]
    idx = 1
    score = dict()
    for j in range(len(lst)):
        if lst[j] not in dic:
            continue

        if lst[j] not in score:
            score[lst[j]] = [1, idx, 0]
        else:
            if score[lst[j]][0] < 4:
                score[lst[j]][0] += 1
                score[lst[j]][1] += idx
            elif score[lst[j]][0] == 4:
                score[lst[j]][0] += 1
                score[lst[j]][2] += idx
    
        idx += 1
    
    score = sorted(score.items(), key=lambda x: (x[1][1], x[1][2]))
    print(score[0][0])