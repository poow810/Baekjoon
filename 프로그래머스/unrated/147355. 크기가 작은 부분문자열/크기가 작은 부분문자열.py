def solution(t, p):
    answer = 0
    a = len(t)
    b = len(p)
    for i in range(0, a-b+1):
        if int(t[i:i+b]) <= int(p):
            answer += 1
        
    
    return answer