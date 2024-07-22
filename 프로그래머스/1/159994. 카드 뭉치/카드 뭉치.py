from collections import deque

def solution(cards1, cards2, goal):
    answer = ''
    
    queue = deque(cards1)
    queue1 = deque(cards2)
    queue2 = deque(goal)
    
    while queue2:
        if queue and queue2[0] == queue[0]:
            queue.popleft()
            queue2.popleft()
        elif queue1 and queue1[0] == queue2[0]:
            queue1.popleft()
            queue2.popleft()
        else:
            break

        
    if queue2:
        return "No"
    else:
        return "Yes"
