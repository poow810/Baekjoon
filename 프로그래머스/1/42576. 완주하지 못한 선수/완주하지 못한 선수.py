def solution(participant, completion):
    dic = {}
    for i in completion:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    for j in participant:
        if j not in dic or dic[j] == 0:
            return j
        else:
            dic[j] -= 1