from heapq import heappush, heappop

def solution(scoville, K):
    
    hq = []
    for i in scoville:
        heappush(hq, i)
    
    count = 0
    if len(hq) == 1:
        if hq[0] >= K:
            return 0
    while hq[0] < K:
        if hq:
            first = heappop(hq)
        else:
            return -1
        if hq:
            second = heappop(hq)
        else:
            return -1
        new_score = first + second*2
        heappush(hq, new_score)
        count += 1
    
    return count
        