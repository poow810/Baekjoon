def solution(n, lost, reserve):
    student = [1] * (n+2)
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            continue    
        student[i] = 0
    
    for j in sorted(reserve):
        if student[j-1] == 0:
            student[j-1] = 1
        elif student[j+1] == 0:
            student[j+1] = 1
    
    print(student)
    
    return sum(student)-2
