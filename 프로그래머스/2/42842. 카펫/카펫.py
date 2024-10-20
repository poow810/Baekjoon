def solution(brown, yellow):
    
    yellow_x = 0
    yellow_y = 0
    
    ans = []
    
    for i in range(1, yellow+1):
        if yellow % i == 0:
            yellow_x = int(yellow/i)
            yellow_y = i
            
            if yellow_x*2 + yellow_y*2 + 4 == brown:
                ans.append((yellow_x+2, yellow_y+2))
    
    return ans[0]