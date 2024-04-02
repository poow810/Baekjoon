import sys


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    dic = {}
    for i in range(n):
        wear = list(sys.stdin.readline().split())
        if wear[1] in dic:
            dic[wear[1]].append(wear[0])
        else:
            dic[wear[1]] = [wear[0]]
    
    count = 1

    for z in dic:
        count *= (len(dic[z])+1)
    print(count-1)