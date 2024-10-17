def solution(sizes):
    
    left = []
    right = []
    
    for i in sizes:
        if i[0] >= i[1]:
            left.append(i[1])
            right.append(i[0])
        
        if i[1] > i[0]:
            left.append(i[0])
            right.append(i[1])
    
    answer = max(left) * max(right)
    return answer