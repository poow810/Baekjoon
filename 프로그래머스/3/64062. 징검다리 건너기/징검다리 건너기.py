from collections import deque

def solution(stones, k):
    left = 1
    right = max(stones) + 1
    
    while left < right - 1:
        mid = (left + right) // 2
        count = 0
        flag = True
        
        for stone in stones:
            if stone < mid:
                count += 1
            
            else:
                count = 0
                
            if count == k:
                flag = False
                break
        
        if flag:
            left = mid
        
        else:
            right = mid
    
    return left
        
            
