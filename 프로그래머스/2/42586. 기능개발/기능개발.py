import math

def solution(progresses, speeds):
    
    answer = []
    end_date = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))]
    
    last_date = end_date[0]
    
    count = 0
    for i in range(len(end_date)):
        if last_date >= end_date[i]:
            count += 1
        else:
            answer.append(count)
            count = 1
            last_date = end_date[i]
        
    answer.append(count)
    return answer
