def solution(diffs, times, limit):
    left = diffs[0]
    right = max(diffs)
    answer = 0
    
    while left <= right:
        mid = (left+right) // 2
        count = 0
        
        for i in range(len(diffs)):
            if diffs[i] <= mid:
                count += times[i]
            
            else:
                count += (diffs[i] - mid) * (times[i-1] + times[i]) + times[i]
        
        if count <= limit:
            right = mid - 1
            answer = mid
        
        else:
            left = mid + 1
    
    return answer
            
        