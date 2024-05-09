def solution(prices):
    
    n = len(prices)
    count = [0 for _ in range(n)]

    stack = [0]
    for i in range(1, n):
        while stack and prices[stack[-1]] > prices[i]:
            c = stack.pop()
            count[c] = i-c
        
        stack.append(i)
    
    while stack:
        c = stack.pop()
        count[c] = n - 1 - c
    return count