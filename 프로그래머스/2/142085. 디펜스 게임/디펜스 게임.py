from heapq import heappop, heappush

def solution(n, k, enemy):
    
    answer = 0
    num = 0
    
    count = len(enemy)
    if k >= count:
        return count
    
    queue = []
    for i in enemy:
        heappush(queue, -i)
        num += i
        if num > n:
            if not k:
                break
            
            k -= 1
            num += heappop(queue)
        
        answer += 1
    
    return answer