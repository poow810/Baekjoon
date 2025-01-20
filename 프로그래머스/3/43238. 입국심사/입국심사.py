def solution(n, times):
    left = 1
    right = max(times) * n
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        check = 0
        
        for i in times:
            check += mid // i
            
            if check >= n:
                break
                
        if check >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
    
    return answer
    