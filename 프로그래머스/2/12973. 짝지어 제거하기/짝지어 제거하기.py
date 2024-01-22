def solution(s):
    
    n = len(s)
    
    stack = []
    for i in range(n):
        if stack and stack[-1] == s[i]:
            stack.pop()
            
        else:
            stack.append(s[i])        
    
    return int(not stack)