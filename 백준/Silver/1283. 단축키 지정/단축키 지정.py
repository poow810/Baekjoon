import sys


def check_1(string):
    lst = string.split(' ')
    
    flag = False
    idx_1 = 0
    idx_2 = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j].upper() not in dic and j == 0:
                dic[lst[i][j].upper()] = 1
                flag = True
                idx_1 = i
                idx_2 = j
                break
        
        if flag:
            break
    if not flag:
        return False
    
    new_string = ""
    for i in range(len(lst)):
        if i == idx_1:
            new = lst[i][0:idx_2]+'[' +lst[i][idx_2]+ ']' + lst[i][idx_2+1:]
            new_string += new + " "
        else:
            new_string += lst[i]  + " "  

    return new_string


def check_2(string):
    lst = string.split(' ')
    
    flag = False
    idx_1 = 0
    idx_2 = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j].upper() not in dic:
                dic[lst[i][j].upper()] = 1
                flag = True
                idx_1 = i
                idx_2 = j
                break
        
        if flag:
            break
    if not flag:
        return False
    
    new_string = ""
    for i in range(len(lst)):
        if i == idx_1:
            new = lst[i][0:idx_2]+'[' +lst[i][idx_2]+ ']' + lst[i][idx_2+1:]
            new_string += new + " "
        else:
            new_string += lst[i]  + " "  

    return new_string
    
N = int(sys.stdin.readline())
dic = {}
ans = []

for _ in range(N):
    string = sys.stdin.readline().rstrip()
    check = check_1(string)
    if check:
        ans.append(check)
    else:
        check2 = check_2(string)
        if check2:
            ans.append(check2)
        else:
            ans.append(string)


for i in ans:
    print(i.rstrip())