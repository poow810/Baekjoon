def solution(array, commands):
    ans = []
    for command in commands:
        a, b, c = command[0], command[1], command[2]
        lst = array[a-1:b]
        lst.sort()
        ans.append(lst[c-1])
    
    return ans
        