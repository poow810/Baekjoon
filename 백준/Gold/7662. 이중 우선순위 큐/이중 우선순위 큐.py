import sys
from heapq import heappop, heappush


def is_empty(dic):
    for i in dic:
        if i[1] > 0:
            return False
    return True
    

T = int(sys.stdin.readline().strip())
for _ in range(T):
    k = int(sys.stdin.readline().strip())
    max_hq = []
    min_hq = []
    dic = dict()

    for i in range(k):    
        string, n = sys.stdin.readline().split()
        n = int(n)

        if string == 'I':
            if n in dic:
                dic[n] += 1
            else:
                heappush(min_hq, n)
                heappush(max_hq, -n)
                dic[n] = 1
        
        elif string == 'D':
            if not is_empty(dic.items()):
                if n == 1:
                    while -max_hq[0] not in dic or dic[-max_hq[0]] < 1:
                        t = -heappop(max_hq)
                        if t in dic:
                            del(dic[t])
                    dic[-max_hq[0]] -= 1
                else:
                    while min_hq[0] not in dic or dic[min_hq[0]] < 1:
                        t = heappop(min_hq)
                        if t in dic:
                            del(dic[t])
                    dic[min_hq[0]] -= 1
        
    

    if is_empty(dic.items()):
        print("EMPTY")
    else:
        while min_hq[0] not in dic or dic[min_hq[0]] < 1:
            heappop(min_hq)
        while -max_hq[0] not in dic or dic[-max_hq[0]] < 1:
            heappop(max_hq)
        print(-max_hq[0], min_hq[0])